# सर्वेक्षण प्रश्न

चाहे आप आज Rust Programming Language <https://rust-lang.org> का उपयोग करते हों या नहीं, हम आपसे सुनना चाहते हैं!

Rust Survey Team ने यह सर्वेक्षण बनाया है ताकि हम समझ सकें कि Rust समुदाय कैसा दिखता है, हम कैसा कर रहे हैं, क्या सुधार किया जा सकता है, और हम आगे बढ़ते हुए आप सभी के साथ कैसे सर्वोत्तम रूप से जुड़ सकते हैं।

आपके उत्तर गुमनाम होंगे। इस सर्वेक्षण के हिस्से के रूप में आप जो कोई भी व्यक्तिगत डेटा जमा करते हैं, उसे हमारी नीति के अनुसार संभाला जाएगा जैसा कि हमारे [Frequently Asked Questions](https://github.com/rust-lang/surveys/blob/main/documents/Community-Survey-FAQ.md) में वर्णित है।

हम अनुमान लगाते हैं कि इसे पूरा करने में लगभग 10-25 मिनट लगेंगे।

## Rust उपयोग

### क्या आप Rust का उपयोग करते हैं?

Type: select one

- हाँ, मैं Rust का उपयोग करता हूँ (किसी भी उद्देश्य के लिए, भले ही आप सिर्फ सीख रहे हों) [`NEXT`](#your-rust-experience)
- नहीं, मैं वर्तमान में Rust का उपयोग नहीं करता, लेकिन मैंने अतीत में किया है [`NEXT`](#for-previous-rust-users)
- नहीं, मैंने कभी Rust का उपयोग नहीं किया है [`NEXT`](#for-non-rust-users)

> **justification**
>
> Fundamental for cohort analysis

## पूर्व Rust उपयोगकर्ताओं के लिए

### जैसा कि आपने संकेत दिया है कि आप वर्तमान में Rust का उपयोग नहीं कर रहे हैं, क्यों नहीं?

Type: select all that apply

- भाषा सुविधाएँ गायब हैं
- लाइब्रेरीज़ गायब हैं
- उपकरण गायब हैं
- सीखना बहुत कठिन है
- समुदाय असभ्य, अप्रिय, या अन्यथा निराशाजनक था
- मैं किसी अन्य भाषा का उपयोग करना पसंद करता हूँ
- मेरे नियंत्रण से बाहर के कारकों के कारण मुझे अब Rust का उपयोग करने का अवसर नहीं मिल रहा है
- मैं भविष्य में एक अवसर आने पर इसका उपयोग करने की योजना बना रहा हूँ
- अन्य

### हमें और बताएँ:

Type: free form (optional)

> **SURVEY FLOW**
>
> Skip to `### Are you employed full- or part-time (including paid internships)?`

## गैर-Rust उपयोगकर्ताओं के लिए

### आप Rust का उपयोग क्यों नहीं करते?

Type: select all that apply

- Rust मुझे अपने लक्ष्यों को प्राप्त करने में मदद नहीं करता
- भाषा सुविधाएँ गायब हैं
- लाइब्रेरीज़ गायब हैं
- उपकरण गायब हैं
- सीखना बहुत कठिन है या सीखने में बहुत अधिक समय लगेगा
- समुदाय असभ्य, अप्रिय, या अन्यथा निराशाजनक था
- मैं किसी अन्य भाषा का उपयोग करना पसंद करता हूँ
- मैं अपने नियंत्रण से बाहर के कारकों के कारण Rust का उपयोग नहीं कर सकता
- मुझे अभी तक इसका मौका नहीं मिला है
- अन्य

### हमें और बताएँ:

Type: free form (optional)

> **SURVEY FLOW**
>
> Skip to `### Are you employed full- or part-time (including paid internships)?`

## Rust उपयोग और सीखने का अनुभव

### औसतन, आप कितनी बार Rust का उपयोग करते हैं?

Type: select one

- दैनिक या लगभग दैनिक
- साप्ताहिक या लगभग साप्ताहिक
- मासिक या लगभग मासिक
- कभी-कभार

> **justification**
>
> This can be useful demographic information as a proxy for how "important" Rust is
> in someone's technical life.
>
> We deliberately use calendar time for this question to gauge how "serious" the
> programmer's use of Rust is. This does mean that we will group together, for example,
> those who program once a week but always in Rust and those who program daily but
> use Rust once a week.

### आप अपनी Rust विशेषज्ञता को कैसे रेट करेंगे?

Type: select one

- मैं Rust कोड नहीं लिख सकता
- मैं Rust में सरल प्रोग्राम लिख सकता हूँ
- मैं उपयोगी, production-ready कोड लिख सकता हूँ, लेकिन यह एक संघर्ष है
- मैं Rust लिखने में उत्पादक हूँ

> **justification**
>
> Useful for cohort analysis, i.e., for other questions we can query if answers are significantly different for beginners vs advanced users.
>
> Previously this question was a 1-10 ranking. Having specific labels can help with consistency across responses. Additionally, having 10 choices
> was too specific (i.e., what's the difference between a 7 and 8?) where as with the new answers, we have a better idea of what the differences
> between answers actually mean.

### आपने Rust में प्रोग्रामिंग कब सीखी?

**नोट**: जबकि आप अपने Rust कौशल में सुधार करने की कोशिश जारी रख सकते हैं, इस प्रश्न के लिए मान लें कि "Rust में प्रोग्रामिंग सीखना"
का मतलब है Rust के साथ अपना *अधिकांश* समय सीखने की सामग्री का उपभोग करना या *सीखने के लिए* कोडिंग करना (किसी अन्य लक्ष्य को प्राप्त करने के विपरीत)। यदि आपकी सीखने की प्रक्रिया सूचीबद्ध समय अवधियों में से कई को कवर करती है, तो वह चुनें जहाँ आपने *सबसे अधिक* सीखा।

Type: select one (optional)

- मैं अभी भी *सक्रिय रूप से* Rust सीखने की कोशिश कर रहा हूँ
- 2025 के दौरान
- 2023 या 2024 के दौरान
- 2021 या 2022 के दौरान
- 2019 या 2020 के दौरान
- 2018 या उससे पहले

> **justification**
>
> Useful for cohort analysis, i.e., for other questions we can understand if *when* someone learned Rust impacts their views on things.
>
> The time periods used as answers try to reflect the major "epochs" of Rust history (i.e., pre-1.0, 2015 edition pre and post new error style,
> and 2018 edition) as well as the most recent past. We use whole years even though this doesn't line up perfectly with these epochs. Learning
> Rust in early 2015 was likely similar to the experience of learning Rust post 1.0 while before that the language was changing rapidly.
> We explicitly use years instead of asking for which Rust edition someone learned because the former is often much easier for respondents to know.
> It's also helpful to be more specific than an edition, and it's fairly easy to know which edition someone likely used based on the year they
> learned Rust.

### यदि आपने Rust के बारे में सीखने की सामग्री का उपभोग किया है, तो आपने किस प्रकार की सामग्री का उपभोग किया?

Type: select all that apply (optional)

- पुस्तकें ("The Rust Programming Language", "Rust for Rustaceans", आदि)
- ऑनलाइन अभ्यास (Rustlings, 100 Exercises To Learn Rust, आदि)
- वीडियो या live-streams
- ब्लॉग पोस्ट
- दस्तावेज़ीकरण
- Rust crates का स्रोत कोड
- ऑनलाइन पाठ्यक्रम, वेबिनार
- व्यक्तिगत प्रशिक्षण
- विश्वविद्यालय सीखने की सामग्री
- अन्य (कृपया निर्दिष्ट करें)

> **justification**
>
> Getting data here seems helpful for guiding users / recommending public content.

### क्या आप वर्तमान में एक ऐसा पाठ्यक्रम ले रहे हैं जो Rust का उपयोग करता है या सिखाता है या क्या आपने पिछले वर्ष में इस प्रकार का पाठ्यक्रम लिया है?

Type: select one (optional)

- हाँ, एक विश्वविद्यालय, स्कूल, या अन्य शैक्षणिक संस्थान के माध्यम से
- हाँ, मेरे नियोक्ता, ठेकेदार, या सलाहकार के माध्यम से
- नहीं

> **justification**
>
> This question is primarily used to funnel respondents into the more specific questions about the kinds of educational activities they've been a part of.

## तकनीकी प्रश्न

### आप Rust विकास के लिए नियमित रूप से कौन से ऑपरेटिंग सिस्टम का उपयोग करते हैं?

**नोट**: यह विशेष रूप से उन सिस्टमों के बारे में है जिनका आप व्यक्तिगत रूप से विकास के लिए उपयोग करते हैं, *नहीं* उन सभी सिस्टमों के बारे में जिन्हें आप लक्षित करते हैं।

Type: select all that apply (optional)

- Linux
- Windows 10/11
- Windows 8.1 या पुराना
- Windows Subsystem for Linux
- macOS
- अन्य (खुला उत्तर)

> **justification**
>
> In general we'd like to know which operating systems are most used as dev machines in the community.
>
> We're using "Linux" here rather than grouping all UNIXes together, to allow
> us to gauge interest in specific other UNIXes via the fill-in-the-blank
> "other" option. If we grouped UNIXes together, users of other UNIX systems
> wouldn't be visible; let's try to capture the level of interest in those
> systems. As with many questions with an open "other" response; if any
> specific answer appears frequently, we can add it to future surveys to reduce
> the amount of work needed to process responses.

### आप किन ऑपरेटिंग सिस्टम या runtimes के लिए Rust सॉफ़्टवेयर विकसित करते हैं?

**नोट**: यह विशेष रूप से उस ऑपरेटिंग सिस्टम या runtime के बारे में है जिसे आप **लक्षित** करते हैं, न कि उस सिस्टम के बारे में जिसका आप
विकास के लिए उपयोग करते हैं और न ही उन विशिष्ट आर्किटेक्चर (जैसे, x86 vs ARM) के बारे में जिन्हें आप लक्षित करते हैं।

Type: select all that apply (optional)

- Linux (डेस्कटॉप या सर्वर)
- Windows 10/11
- Windows 8.1 या पुराना
- macOS
- iOS
- Android
- Embedded platforms (ऑपरेटिंग सिस्टम के साथ)
- Embedded platforms (bare metal)
- WebAssembly (ब्राउज़र के लिए)
- WebAssembly (अन्य hosts के लिए)
- स्पष्ट रूप से platform-independent (उदाहरण के लिए, एक लाइब्रेरी जो ऑपरेटिंग सिस्टम के साथ बातचीत नहीं करती)
- अन्य (खुला उत्तर)

> **justification**
>
> This question can be used to figure out roughly what systems are being targeted as well as
> what OS stack is being developed against (i.e., desktop/server OS, mobile OS, embedded OS, bare metal)
>
> We're using "Linux" here rather than "*nix" or similar, with the same
> justification as in the "Which operating systems do you use" question.
>
> We specifically care about the runtime environment being targeted. ISA and other machine specifics are
> not what matters.

### आप नियमित रूप से Rust कोड के साथ कौन सा editor या IDE setup उपयोग करते हैं?

Type: select all that apply (optional)

- VS Code
- vi/vim/neovim
- IntelliJ/CLion/other JetBrains IDE + Rust plugin
- Rust Rover (dedicated IntelliJ Rust IDE)
- Emacs (या derivatives जैसे Doom Emacs, Spacemacs, आदि)
- Sublime Text
- Visual Studio
- Xcode
- Atom
- Helix
- Zed
- अन्य (खुला उत्तर)

> **justification**
>
> It is good to know which editor is the most preferred for Rust development. This
> can change investment strategies for further IDE development.
>
> Note: previously this question included different 'drivers' of the Rust IDE
> experience (e.g., racer, rls, rust-analyzer). Development has consolidated on
> rust-analyzer, and so it's not necessary to find out which is being used.
> If we are curious how far along adoption of rust-analyzer is, we can ask that
> in a separate question, though this is likely easier to find out through download
> numbers.

### आप विकास के लिए Rust के कौन से version(s) का उपयोग करते हैं?

Type: select all that apply (optional)

- वर्तमान stable version
- पिछली stable version
- 1.83 के बराबर या नए stable Rust का एक विशिष्ट version
- 1.83 से पुराने stable Rust का एक विशिष्ट version
- Beta release
- Latest nightly
- Nightly का एक विशिष्ट version
- Custom fork
- मुझे नहीं पता
- अन्य

> **justification**
>
> Together with the following question, we can better determine what the spread of
> version usage is across the community.
> We ask specifically about version 1.83 since it is, at the time of the survey, the
> version that was released ~1 year prior. Additionally, at the time of this writing
> all major Linux distros have a version equal to or newer than this version.

### यदि आप nightly का उपयोग करते हैं, तो क्यों?

Type: select all that apply (optional)

- मैं nightly का उपयोग नहीं करता
- आदत से बाहर
- एक विशिष्ट भाषा सुविधा या भाषा सुविधाओं के सेट के लिए जिसकी मुझे आवश्यकता है
- मुझे सभी latest सुविधाओं तक पहुंच पसंद है
- nightly version में bugs के लिए परीक्षण करने में मदद करने के लिए
- nightly सुविधाओं पर design feedback प्रदान करने के लिए
- CI में परीक्षण के लिए
- एक crate dependency जिसका मैं उपयोग करता हूँ उसे इसकी आवश्यकता है
- एक उपकरण जिसका मैं उपयोग करता हूँ उसे इसकी आवश्यकता है
- तेज़ compile times के लिए
- अन्य (खुला उत्तर)

> **justification**
>
> We'd like to know what are the common reasons people use nightly
> so that we can better understand where testers are coming from.

### किसी भी विकास कार्य के लिए आप जिस Rust का सबसे पुराना version उपयोग करते हैं वह क्या है?

(यह सुनिश्चित करने के लिए परीक्षण को छोड़कर कि आपका कोड उस compiler version पर काम करता है।)

Type: select one (optional)

- 1.93 (nightly), और फिर 1.92 से 1.0 तक descending order में हर version, और "a pre-1.0 version"

> **justification**
>
> To get real data on how many people use older versions of the toolchain to
> inform discussion on MSRVs.

### क्या आप Rust stability पर निम्नलिखित statements से सहमत हैं?

Type: matrix (optional)

Statements:

- मैं अपने कोड के compile होने में विफल होने के डर के बिना *stable* compiler version को upgrade कर सकता हूँ
- मैं अपने कोड के compile होने में विफल होने के डर के बिना *nightly* compiler version को upgrade कर सकता हूँ
- एक नए *stable* compiler version में upgrade करने के लिए मेरे कोड में या तो कोई बदलाव नहीं या बेहद छोटे और आसान बदलावों की आवश्यकता होती है
- एक नए *nightly* compiler version में upgrade करने के लिए मेरे कोड में या तो कोई बदलाव नहीं या बेहद छोटे और आसान बदलावों की आवश्यकता होती है

Rating:

- Agree
- Disagree

> **justification**
>
> When want to get an impression of how stable the compiler *feels*. Impressions are more important than hard numbers as
> not all users define stability in the same way the compiler does.

### Rust कितनी तेज़ी से विकसित होता है, इस पर आपकी क्या राय है?

हम जानना चाहते हैं कि आप Rust भाषा के विकास की गति को कैसे देखते हैं।

Type: select one (optional)

- Rust पहले से ही बहुत जटिल है, इसे अधिक महत्वपूर्ण सुविधाएँ नहीं जोड़नी चाहिए या stabilize नहीं करनी चाहिए
- Rust बहुत तेज़ी से बदलता है, मैं चाहूंगा कि यह विकास की गति धीमी कर दे
- मैं विकास की वर्तमान गति से संतुष्ट हूँ
- Rust बहुत धीमी गति से बदलता है, मैं चाहूंगा कि यह सुविधाओं को तेज़ी से जोड़े या stabilize करे
- मुझे नहीं पता या मुझे परवाह नहीं है
- अन्य (खुला उत्तर)

> **justification**
>
> We want to find out if people prefer stability and fewer changes, or if they want to see more features being
> implemented or stabilized.

### कौन सी unimplemented (या केवल nightly) सुविधाएँ हैं जिन्हें आप stabilize होने की उम्मीद कर रहे हैं?

कृपया *Rust compiler या standard library* सुविधाओं का उल्लेख करें जो वर्तमान में अस्थिर हैं (केवल Rust compiler के nightly release का उपयोग करके उपलब्ध) या गायब हैं जो आपकी राय में Rust ecosystem या आपके लिए फायदेमंद होंगी। यह सूची compiler के आसपास के अन्य tooling जैसे cargo, rustup, rustfmt, आदि को बाहर करती है।

Type: matrix (optional)

Features:

- [Specialization](https://github.com/rust-lang/rust/issues/31844)
- [Generators/coroutines](https://github.com/rust-lang/rust/issues/43122)
- [Async generators/coroutines](https://github.com/rust-lang/rust/pull/118420)
- [Try blocks](https://github.com/rust-lang/rust/issues/31436)
- [Never type](https://github.com/rust-lang/rust/issues/35121)
- [Trait aliases](https://github.com/rust-lang/rfcs/blob/master/text/1733-trait-alias.md)
- [Type Alias Impl Trait (TAIT)](https://rust-lang.github.io/rfcs/2515-type_alias_impl_trait.html)
- [Associated type defaults](https://rust-lang.github.io/rfcs/2532-associated-type-defaults.html)
- [Generic const expressions](https://github.com/rust-lang/rust/issues/76560)
- [Const trait methods](https://github.com/rust-lang/rust/issues/67792)
- [Declarative (macro_rules!) attributes (#[attr]) and derives (#[derive(Trait)])](https://github.com/rust-lang/rust/issues/143549)
- Compile time reflection
- Variadic generics
- [Arbitrary self types](https://github.com/rust-lang/rfcs/blob/master/text/3519-arbitrary-self-types-v2.md)
- [Enum variant types](https://github.com/rust-lang/lang-team/issues/122)
- [Allocator trait and better OOM handling](https://github.com/rust-lang/rust/issues/32838)
- [Stable ABI](https://github.com/rust-lang/rust/issues/111423)
- [Portable SIMD](https://github.com/rust-lang/portable-simd)

Priority:

- Would unblock my use-case
- Would improve my code
- Don't need it
- Don't know what it is

### क्या ऊपर उल्लिखित सुविधाओं के अलावा कोई सुविधाएँ हैं जिन्हें आप prioritize करना चाहेंगे?

Type: free form (optional)

> **justification**
>
> Allow the cohort to mention specific language features they might be eagerly waiting for, see https://github.com/rust-lang/surveys/pull/234/files#r1347633041

### Rust के निम्नलिखित पहलुओं में से कौन से आपकी प्रोग्रामिंग उत्पादकता के लिए non-trivial समस्याएँ पेश करते हैं?

केवल उन चुनौतियों का आकलन करें जो आपको लगता है कि आपके काम को प्रभावित कर रही हैं। यदि आप किसी दी गई पंक्ति के लिए कुछ भी चयन नहीं करते हैं, तो हम मानेंगे कि आप उस पहलू के बारे में नहीं जानते या आपको परवाह नहीं है।

Type: matrix (optional)

Challenges:

- विभिन्न आकारों के tuples के लिए logic लागू करना
- crates में कोड को विभाजित करना (उदाहरण के लिए orphan rule)
- Iterator को manually लागू करना होना
- const fn में पर्याप्त नहीं कर पाना
- Dynamic library plugins लागू करना
- अन्य भाषाओं के साथ अंतरसंचालन (उदाहरण के लिए C या C++)
- Async कोड के साथ structured concurrency प्राप्त करना
- Executor-agnostic async कोड लिखना
- सही unsafe कोड लिखना
- Borrow checker वैध कोड की अनुमति नहीं दे रहा
- धीमी runtime performance
- धीमी compilation
- Compiled artifacts का बड़ा binary size
- उच्च disk space usage (उदाहरण के लिए target folder का आकार)
- Compiler bugs का सामना करना (उदाहरण के लिए ICEs a.k.a. internal compiler errors या miscompilations)
- अस्पष्ट/अस्पष्ट compiler error messages का सामना करना
- Subpar IDE support (उदाहरण के लिए कुछ errors नहीं दिखाए जाते या analysis धीमी है)
- Subpar debugging experience (उदाहरण के लिए missing value visualizations या async stacktraces)
- Rust भाषा या standard library का दस्तावेज़ीकरण की कमी

Options:

- Big problem for me
- Could be improved, but does not limit me
- Not an issue for me at all

> **justification**
>
> This question tries to get insights on what people wish the Rust project would improve.

### क्या ऊपर उल्लिखित चुनौतियों के अलावा कोई चुनौतियाँ हैं जो आपकी Rust प्रोग्रामिंग उत्पादकता को प्रभावित करती हैं?

Type: free form (optional)

> **justification**
>
> Allow the cohort to mention other challenges.

### पिछले 12 महीनों में stabilize हुई कौन सी सुविधाएँ आप सबसे अधिक उपयोग करते हैं?

कोष्ठक में text दिखाता है कि किस Rust version में सुविधा को stabilize किया गया था।

Type: matrix (optional)

Features:

- [Strict provenance API](https://blog.rust-lang.org/2025/01/09/Rust-1.84.0/#strict-provenance-apis) (1.84)
- [Async closures](https://blog.rust-lang.org/2025/02/20/Rust-1.85.0/#async-closures) (1.85)
- [diagnostic::do_not_recommend](https://blog.rust-lang.org/2025/02/20/Rust-1.85.0/#hiding-trait-implementations-from-diagnostics) (1.85)
- [Trait upcasting](https://blog.rust-lang.org/2025/04/03/Rust-1.86.0/#trait-upcasting) (1.86)
- [Anonymous pipes](https://blog.rust-lang.org/2025/05/15/Rust-1.87.0/#anonymous-pipes) (1.87)
- [Let chains](https://blog.rust-lang.org/2025/06/26/Rust-1.88.0/#let-chains) (1.88)
- [Naked functions](https://blog.rust-lang.org/2025/06/26/Rust-1.88.0/#naked-functions) (1.88)

Usage:

- I use it or plan to use it
- I cannot use this feature yet
- I do not need this feature
- I did not know it was stabilized
- I do not know what it is

### आप अपने Rust projects को कैसे build करते हैं?

Type: select all that apply (optional)

- मैं Cargo का उपयोग करता हूँ
- मैं किसी अन्य build system का उपयोग करता हूँ
- मैं Cargo और किसी अन्य build system को जोड़ता हूँ
- यदि आप Cargo के साथ (या केवल) अन्य build systems का उपयोग करते हैं, तो आप कौन से उपयोग करते हैं? (खुला उत्तर)

> **justification**
>
> cargo team expressed 