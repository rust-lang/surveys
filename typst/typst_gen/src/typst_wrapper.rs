use std::{
    collections::HashMap,
    path::PathBuf,
    sync::{Arc, LazyLock, Mutex},
};

use typst::{
    Library, LibraryExt, World,
    diag::{FileError, FileResult},
    foundations::{Bytes, Datetime},
    syntax::{FileId, Source},
    text::{Font, FontBook},
    utils::LazyHash,
};
use typst_kit::fonts::{FontSearcher, FontSlot};

static LIBRARY: LazyLock<LazyHash<Library>> = LazyLock::new(|| LazyHash::new(Library::default()));

#[derive(Debug)]
pub struct Typst {
    root: PathBuf,
    source: Source,
    book: LazyHash<FontBook>,
    fonts: Vec<FontSlot>,
    /// Datetime.
    time: time::OffsetDateTime,

    files: Arc<Mutex<HashMap<typst::syntax::FileId, TypstFile>>>,
}

#[derive(Debug, Clone)]
pub struct TypstFile {
    bytes: typst::foundations::Bytes,
    src: Option<Source>,
}

impl TypstFile {
    pub fn new(bytes: typst::foundations::Bytes, src: Option<Source>) -> Self {
        Self { bytes, src }
    }

    fn source(&mut self, id: FileId) -> FileResult<Source> {
        let source = if let Some(source) = &self.src {
            source
        } else {
            let contents = std::str::from_utf8(&self.bytes).map_err(|_| FileError::InvalidUtf8)?;
            let contents = contents.trim_start_matches('\u{feff}');
            let source = Source::new(id, contents.into());
            self.src.insert(source)
        };
        Ok(source.clone())
    }
}

impl Typst {
    pub fn new(root: PathBuf, text: &str) -> Self {
        let fonts = FontSearcher::new().include_system_fonts(true).search();
        Self {
            root,
            source: Source::detached(text),
            book: LazyHash::new(fonts.book),
            fonts: fonts.fonts,
            time: time::OffsetDateTime::now_utc(),
            files: Arc::new(Mutex::new(HashMap::new())),
        }
    }
    fn file(&self, id: FileId) -> FileResult<TypstFile> {
        let mut files = self.files.lock().map_err(|_| FileError::AccessDenied)?;
        if let Some(entry) = files.get(&id) {
            return Ok(entry.clone());
        }
        let path = if id.package().is_some() {
            unimplemented!("Support for downloading packages is not implemented")
        } else {
            // Fetching file from disk
            id.vpath().resolve(&self.root)
        }
        .ok_or(FileError::AccessDenied)?;

        let content = std::fs::read(&path).map_err(|error| FileError::from_io(error, &path))?;
        Ok(files
            .entry(id)
            .or_insert(TypstFile::new(Bytes::new(content), None))
            .clone())
    }
}

impl World for Typst {
    /// Standard library.
    fn library(&self) -> &LazyHash<Library> {
        &LIBRARY
    }

    /// Metadata about all known Books.
    fn book(&self) -> &LazyHash<FontBook> {
        &self.book
    }

    /// Accessing the main source file.
    fn main(&self) -> FileId {
        self.source.id()
    }

    /// Accessing a specified source file (based on `FileId`).
    fn source(&self, id: FileId) -> FileResult<Source> {
        if id == self.source.id() {
            Ok(self.source.clone())
        } else {
            self.file(id)?.source(id)
        }
    }

    /// Accessing a specified file (non-file).
    fn file(&self, id: FileId) -> FileResult<Bytes> {
        self.file(id).map(|file| file.bytes.clone())
    }

    /// Accessing a specified font per index of font book.
    fn font(&self, id: usize) -> Option<Font> {
        self.fonts[id].get()
    }

    /// Get the current date.
    ///
    /// Optionally, an offset in hours is given.
    fn today(&self, offset: Option<i64>) -> Option<Datetime> {
        let offset = offset.unwrap_or(0);
        let offset = time::UtcOffset::from_hms(offset.try_into().ok()?, 0, 0).ok()?;
        let time = self.time.checked_to_offset(offset)?;
        Some(Datetime::Date(time.date()))
    }
}
