#let maketitle(
  title: str,
  date: datetime,
  authors: (),
  type: (),
  doc,
) = {
  set page(paper: "a4", margin: (
    x: 1.135in,
    y: 1.345in

  ))
  set text(font: "TeX Gyre Pagella")
  place(
    top + left,
    image("rust-logo-blk.svg"),
  )
  place(
    horizon + left,
    grid(
      columns: 2,
      rows: 1,
      align: top,
      gutter: 1em,
      rect(
        stroke: none,
        inset: 0em,
        width: 100%,
        stack(
          dir: ttb,
          spacing: 1em,
          text(title, weight: 700, size: 25pt),
        ),
      ),
      stack(
        dir: ttb,
        spacing: 1em,
        [Compiled and presented by the Rust Survey Team],
        text(size: 10pt)[
          #smallcaps[Report Dated] #date.display("[weekday repr:long], [day]th [month repr:long] [year]")
        ],
      ),
    ),
  )
  pagebreak()
  show outline.entry: set block(above: 1.2em)
  outline(title: text(size: 20pt, weight: 700)[Contents #v(1.2em)])
  pagebreak()
  show heading.where(level: 1): set text(font: "TeX Gyre Pagella", size: 20pt)
  set heading(numbering: "I.") // For Level 1 headings (e.g., 1, 2, 3)
  set heading(numbering: "I.1.")
  set page(columns: 2)
  doc
}

#let acute(x) = x + "\u{301}"

#show: doc => maketitle(
  authors: ([Jakub Ber#acute("a")nek], "apiraino"),
  date: datetime.today(),
  type: "Report Template",
  title: "The State of Rust Survey Report, 2024",
  doc,
)
= Executive Summary
