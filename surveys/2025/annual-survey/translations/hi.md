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
> cargo team expressed interest in this, see https://rust-lang.zulipchat.com/#narrow/stream/246057-t-cargo/topic/Rust.20survery.202023/near/393816653

### आप Rust projects बनाने के लिए crates कहाँ से डाउनलोड करते हैं?

Type: select all that apply (optional)

- crates.io
- Custom/local/company registry
- Mirror of crates.io
- Git repositories
- मुझे नहीं पता
- अन्य

> **justification**
>
> It could be interesting to know how many people use crates.io vs some custom/local/company registry, and how many people are even aware of what registry do they use. See issue surveys#236.

### क्या आप compiler error codes का उपयोग करते हैं?

Rust compiler कुछ compiler errors को error codes निर्दिष्ट करता है (उदाहरण के लिए *E0308* या *E0509*)। एक [Rust error codes index](https://doc.rust-lang.org/error_codes/error-index.html) है जो इन errors को एकत्र करता है और उनका एक सामान्य विवरण प्रदान करता है। आप इन error descriptions तक पहुंच सकते हैं, उदाहरण के लिए `rustc --explain <error-code>` का उपयोग करके, [documentation](https://doc.rust-lang.org/error_codes/error-index.html) में या [Rust Playground](https://play.rust-lang.org) के माध्यम से।

Type: select one (optional)

- मैं compiler error index descriptions पढ़ता हूँ और उन्हें उपयोगी पाता हूँ
- मैंने compiler error index descriptions की जांच की लेकिन उन्हें उपयोगी नहीं पाया
- मुझे नहीं पता था कि एक compiler error index है
- अन्य (खुला उत्तर)

> **justification**
>
> We are currently discussing whether we should keep error codes in the compiler or not. This would be useful as a way to gauge general interest in this feature.

## Rust समुदाय

### आप निम्नलिखित Rust समुदाय गतिविधियों में लगभग कितनी बार संलग्न होते हैं?

Type: matrix (optional)

Activities:

- Rust के बारे में सूचनात्मक सामग्री का निर्माण करना (उदाहरण के लिए, ब्लॉग लिखना, live stream करना, YouTube video बनाना, conference/meetup में प्रस्तुत करना, आदि)
- Rust के बारे में सूचनात्मक सामग्री का उपभोग करना (उदाहरण के लिए, ब्लॉग, live streams, YouTube videos, आदि)
- आधिकारिक Rust communication channels पढ़ना (उदाहरण के लिए, This Week in Rust, आधिकारिक Rust blog, Rust Bluesky account, आदि)
- सोशल मीडिया या वेबसाइटों पर Rust के बारे में बातचीत में भाग लेना (Hacker News, r/rust, Twitter, LinkedIn, आदि)
- एक Rust meetup या conference में भाग लेना (virtual या in-person)
- एक open RFC पर लिखना, टिप्पणी करना, चर्चा में योगदान देना, या संपादन प्रदान करना
- एक आधिकारिक chat या forum में Rust project पर चर्चा करना (internals.rust-lang.org, Rust Zulip, आदि)
- rust-lang GitHub organization में किसी भी repo पर एक issue खोलना
- किसी भी open-source Rust project में code changes (tests सहित) का योगदान करना
- किसी भी open-source Rust project में non-code changes (documentation, comments, आदि) का योगदान करना

Frequency:

- साप्ताहिक से अधिक बार
- साप्ताहिक
- मासिक या कम बार
- कभी नहीं

> **justification**
>
> We want to understand the nature of contribution to the Rust project both
> to better understand the shape of community involvement and for cohort analysis.

### निम्नलिखित Rust समुदाय स्थानों में आपका अनुभव कैसा रहा है?

Type: matrix

Community Spaces:

- *आधिकारिक* Rust community forums या chats (users.rust-lang.org, internals.rust-lang.org, आधिकारिक Rust Discord, या Rust Zulip)
- *गैर-आधिकारिक* Rust community forums या chats (उदाहरण के लिए, reddit.com/r/rust, Hacker News, Rust *Community* Discord, आदि)
- Rust software development के एक विशिष्ट क्षेत्र पर केंद्रित समुदाय (उदाहरण के लिए game development, audio, आदि)
- Rust conferences
- Rust meetups या स्थानीय community events
- rust-lang GitHub organization के *अंदर* एक repository पर discussions (issues, pull requests, आदि)
- rust-lang GitHub organization के *बाहर* एक repository पर discussions (issues, pull requests, आदि)

Choices:

- मैं स्वागत महसूस करता हूँ
- मैं विशेष रूप से स्वागत या अप्रिय महसूस नहीं करता
- मैं अप्रिय महसूस करता हूँ
- मैंने कभी इस गतिविधि में भाग नहीं लिया है

> **justification**
>
> We'd like to know where people are feeling welcome and the degree to which they are feeling welcome.

### यदि आपने संकेत दिया है कि आप Rust समुदाय में स्वागत महसूस नहीं करते हैं, तो क्या आप अपने अनुभव के बारे में कोई विवरण हमारे साथ साझा करना चाहेंगे?

Type: free form (optional)

> **justification**
>
> More detail on the type of situations where people have felt unwelcome can let us better
> address these issues in the future.

## काम पर Rust

### क्या आप full- या part-time नियोजित हैं (paid internships सहित)?

Type: select one

- हाँ
- नहीं [`NEXT`](#please-share-your-assessment-of-the-following-statements-on-rust-employment)

### क्या आप अपने काम में software लिखते या डिज़ाइन करते हैं?

Type: select one (optional)

- हाँ, मुख्य रूप से एक individual contributor के रूप में (अर्थात, non-manager)
- मैं मुख्य रूप से दूसरों का प्रबंधन करता हूँ जो करते हैं
- नहीं [`NEXT`](#to-what-extent-is-rust-currently-being-used-by-your-organisation)

### क्या आप व्यक्तिगत रूप से काम पर Rust का उपयोग कर रहे हैं?

Type: select one

- हाँ, मेरे coding के अधिकांश हिस्से के लिए
- हाँ, औसतन सप्ताह में कुछ बार
- हाँ, लेकिन मैं इसे केवल कभी-कभी उपयोग करता हूँ
- नहीं

> **justification**
>
> We want to establish what percentage of those who could possibly use Rust in a professional setting
> are using Rust in a professional setting. This is most interesting over time.
> Answers to this question should be combined with whether the respondent has ever used Rust.

### आपकी organisation द्वारा Rust का वर्तमान में किस हद तक उपयोग किया जा रहा है?

Type: select one

- मेरी organisation Rust का non-trivial उपयोग करती है (उदाहरण के लिए, production में या महत्वपूर्ण tooling में उपयोग किया गया)
- मेरी organisation ने Rust के साथ प्रयोग किया है या इसका उपयोग करने पर विचार कर रही है
- मेरी organisation ने किसी भी उपयोग के लिए Rust पर गंभीरता से विचार नहीं किया है [`NEXT`](#approximately-how-many-total-developers-does-your-organisation-employ)
- मेरी organisation ने Rust पर विचार किया लेकिन इसका उपयोग नहीं करने का निर्णय लिया [`NEXT`](#approximately-how-many-total-developers-does-your-organisation-employ)
- मुझे यकीन नहीं है कि मेरी organisation ने Rust का उपयोग करने पर विचार किया है या वर्तमान में इसका उपयोग करती है [`NEXT`](#approximately-how-many-total-developers-does-your-organisation-employ)
- मैं किसी organisation के लिए काम नहीं करता या मेरी organisation किसी भी प्रकार का software विकसित नहीं करती [`NEXT`](#please-share-your-assessment-of-the-following-statements-on-rust-employment)

> **justification**
>
> We want to establish how reliant companies are on Rust.

### निम्नलिखित statements में से कौन से काम पर Rust का उपयोग करने के आपके अनुभव पर लागू होते हैं?

Type: select all that apply (optional)

Statements:

- Rust का उपयोग करने से हमें अपने लक्ष्यों को प्राप्त करने में मदद मिली है
- Rust को अपनाना चुनौतीपूर्ण रहा है
- कुल मिलाकर, Rust को अपनाने ने हमारी team को धीमा कर दिया है
- Rust का उपयोग करना adoption की लागत के लायक रहा है
- हम भविष्य में फिर से Rust का उपयोग करने की संभावना रखते हैं

> **justification**
>
> Future potential adopters may want to know how often other's have encountered success.

### निम्नलिखित statements में से कौन से कारण हैं कि आप काम पर Rust का उपयोग क्यों करते हैं?

Type: select all that apply (optional)

Statements:

- इसके performance (अर्थात, गति, memory footprint, आदि) characteristics के लिए
- हमें अपने software के चलने के तरीके पर सटीक नियंत्रण की आवश्यकता है
- इसके security और safety properties हमारे लिए महत्वपूर्ण हैं
- यह हमें अपेक्षाकृत सही और bug-free software बनाने की अनुमति देता है
- हमें Rust में प्रोग्रामिंग करना आनंददायक या मजेदार लगता है
- हम पहले से ही Rust जानते हैं इसलिए यह हमारा default choice है
- हम इसे prototype करने में आसान पाते हैं
- हमें existing Rust code के साथ interact करना होगा

> **justification**
>
> The Rust community and potential adopters of Rust have a lot of assumptions of why one would choose Rust for a project.
> This question can help confirm or challenge our assumptions and see how they change over time.

### आपके Rust के उपयोग में क्या चुनौतीपूर्ण रहा है?

Type: free form (optional)

> **justification**
>
> This an opportunity to learn from adopters at companies what they struggle with when adopting Rust.

### आपकी organisation में किस technology domain(s) में Rust का उपयोग किया जाता है?

Type: select all that apply (optional)

- Audio programming
- Automotive
- Blockchain
- Cloud computing applications
- Cloud computing infrastructure या utilities
- Computer graphics
- Computer games
- Computer networking
- Computer security
- Data science
- Database implementation
- Desktop computer application frontend
- Desktop computer या mobile phone libraries या services
- Distributed systems
- Embedded devices (ऑपरेटिंग सिस्टम के साथ)
- Embedded devices (bare metal)
- HPC (High-performance [Super]Computing)
- IoT (Internet of Things)
- Machine learning
- Mobile phone application frontend
- Programming languages और संबंधित tools (compilers, IDEs, standard libraries, आदि सहित)
- Robotics
- Scientific और/या numerical computing
- Server-side या "backend" application
- Simulation
- Web application frontend
- WebAssembly
- अन्य (खुला उत्तर)

> **justification**
>
> We want to know roughly what technology stacks are being most often used.
>
> This can be ambiguous and hard to answer. For example, if you're building an operating
> system for a mobile phone, is that embedded, mobile, or something else?
> We want to understand the "shape" of Rust usage, and this question tries to get at that
> by allowing the respondent to select multiple answers.

### आपकी organisation में लगभग कितने कुल developers कार्यरत हैं?

**नोट**: यहाँ सटीक होने की चिंता न करें! अपनी instinct के साथ जाएं।

Type: select one (optional)

- 10 से कम
- 11-49
- 50-99
- 100-500
- 500-1,000
- 1,000-10,000
- 10,000 से अधिक

> **justification**
>
> This question is not that interesting on its own, but it can be used as a sort of cohort for understanding how answers
> change depending on the size of the development effort at a company.
>
> Previously this question used "employees" instead of "developers". It is more appropriate for us to ask about the amount
> of developers at a company vs. the amount of people employed in total.

### क्या आपकी organisation अगले वर्ष Rust developers को नियुक्त करने की योजना बना रही है?

Type: select one (optional)

- हाँ
- नहीं (यह अन्य developers को नियुक्त करने की योजना बना रही है)
- नहीं (यह किसी भी developers को नियुक्त करने की योजना नहीं बना रही है)
- मुझे नहीं पता

> **justification**
>
> This question assess hiring sentiment. Although there is intrinsic uncertainty, it is easy to answer and forward looking.
> It will also be interesting to see what the demand for Rust skills from companies is over time.

### कृपया Rust employment पर निम्नलिखित statements के बारे में अपना assessment साझा करें

Type: matrix (optional)

Statements:

- Junior programmers के लिए ऐसी jobs ढूंढना आसान है जो programming के अधिकांश हिस्से के लिए Rust का उपयोग करती हैं
- Senior programmers के लिए ऐसी jobs ढूंढना आसान है जो programming के अधिकांश हिस्से के लिए Rust का उपयोग करती हैं
- Existing Rust jobs आकर्षक हैं

Rating:

- Agree
- Neither agree nor disagree
- Disagree

> **justification**
>
> The flip side of the question asking whether the respondent's company plans on hiring Rust developers, we
> want to know how respondents feel the level of demand for and quality of Rust jobs are.

## Rust के बारे में आपकी राय

### निम्नलिखित statements में से कौन से Rust के बारे में आपको सच लगते हैं?

Type: select all that apply (optional)

Statements:

- Rust अन्य programming languages पर एक वास्तविक लाभ प्रदान करता है
- Rust अन्य programming languages की तुलना में प्रोग्रामिंग करने में काफी अधिक जटिल है
- Rust को सीखने के लिए अन्य programming languages की तुलना में काफी अधिक प्रयास की आवश्यकता होती है
- Rust code में आमतौर पर काफी कम bugs होते हैं जो किसी अन्य programming language में लिखे गए समकक्ष code में होंगे
- Production में Rust का उपयोग करना जोखिम भरा है
- Rust मुझे अधिक उत्पादक बनाता है
- Rust का उपयोग करना मजेदार है

> **justification**
>
> There are several "truisms" about Rust that we'd like to get perspective on how true these are for users of Rust.
>
> Note that answers here can be subject to survivorship bias and so extra care should be taken with interpreting results.

### Rust के भविष्य के लिए आपकी सबसे बड़ी चिंताएँ क्या हैं?

Type: select all that apply (optional)

- Tech industry में पर्याप्त उपयोग नहीं
- बड़ी companies से बहुत अधिक रुचि
- Ecosystem में पर्याप्त open source contributions नहीं
- एक विशिष्ट feature जो मैं चाहता हूँ उसे नहीं जोड़ता
- Rust पर्याप्त तेज़ी से विकसित नहीं होता
- भाषा की अस्थिरता
- एक alternative द्वारा प्रतिस्थापित
- बहुत जटिल हो जाता है
- Tools और documentation पर्याप्त accessible नहीं हैं (उदाहरण के लिए, भाषा के कारण या screen readers के साथ असंगतता)
- Rust Foundation Rust project को ठीक से support नहीं कर रहा है (उदाहरण के लिए financial, infrastructure, legal aspects में)
- Project governance समुदाय के आकार/आवश्यकताओं से मेल खाने के लिए scale नहीं करता
- भाषा के developers/maintainers को ठीक से support नहीं मिल रहा है
- मैं चिंतित नहीं हूँ
- अन्य (खुला उत्तर)

> **justification**
>
> Would be useful for leadership to understand the community's fears.

## आपके बारे में

See [who](./design/who.md).

निम्नलिखित प्रश्नों के आपके उत्तर हमारे reviewers को cohort analyses आयोजित करने में मदद करेंगे और हमें Rust समुदाय को बेहतर ढंग से समझने में मदद करेंगे। कृपया अपने comfort level के अनुसार उत्तर दें।

### क्या आप अपने आप को technology में एक ऐसे समूह का सदस्य मानते हैं जो underrepresented या marginalized है?

Type: select one

- हाँ
- नहीं [`NEXT`](#are-you-a-full--or-part-time-student)
- मैं नहीं कहना चाहूंगा [`NEXT`](#are-you-a-full--or-part-time-student)

### Technology में निम्नलिखित underrepresented या marginalized groups में से आप अपने आप को किसका हिस्सा मानते हैं?

Type: select all that apply (optional)

- Cultural beliefs
- Disabled (शारीरिक, मानसिक, या अन्यथा)
- Neurodivergent
- Educational background
- Language
- Lesbian, gay, bisexual, queer या अन्यथा non-heterosexual
- Non-binary gender
- औसत developers की तुलना में बड़े या छोटे जिन्हें मैं जानता हूँ
- Political beliefs
- Racial या ethnic minority
- Religious beliefs
- Trans
- Woman या woman के रूप में माना जाता है
- अन्य (खुला उत्तर)

### क्या आप एक full- या part-time student हैं?

Type: select one (optional)

- नहीं
- हाँ, secondary/high school में
- हाँ, bachelor's/undergraduate program में
- हाँ, master's program में
- हाँ, doctorate program में
- हाँ, vocational program में
- हाँ, अन्य (खुला उत्तर)

> **justification**
>
> This will be important for cohort analysis. In particular, we want to
> understand how students at different points in their education view
> topics related to Rust.

### आप कितने समय से प्रोग्रामिंग कर रहे हैं (किसी भी भाषा में, किसी भी कारण से)?

Type: select one (optional)

- < 1 वर्ष
- < 3 वर्ष
- < 5 वर्ष
- < 10 वर्ष
- > 10 वर्ष

### आप कहाँ रहते हैं?

Type: select one (optional)

- देशों की सूची [`NEXT`](#in-what-ways-are-you-comfortable-communicating-about-technical-topics-in-english)
- अन्य

> **justification**
>
> We'd like to get a geographic understanding of where the community is. To have more structure, a free-form answer
> is not used, and instead we use the country definition according to UN.

### जैसा कि आपने ऊपर देशों की सूची से "अन्य" चुना है, कृपया नीचे अपने निवास के क्षेत्र को दर्ज करें:

Type: free form

### आप English में technical topics के बारे में किन तरीकों से communicate करने में सहज हैं?

Type: select all that apply (optional)

- मैं English में spoken technical conversation करने में सहज और सक्षम महसूस करता हूँ
- मैं English में written technical conversation करने में सहज और सक्षम महसूस करता हूँ
- मैं English में technical documentation पढ़ने में सहज और सक्षम महसूस करता हूँ
- मैं English में एक technical talk (उदाहरण के लिए, conference या meetup में) consume करने में सहज और सक्षम महसूस करता हूँ
- मैं English में written technical educational material (उदाहरण के लिए, technical books, blog posts, आदि) consume करने में सहज और सक्षम महसूस करता हूँ

> **justification**
>
> We want to understand self reported feeling of comfort and capability of communication
> of English since a large portion of the Rust community is and likely will always be in English.

### आप existing technical content (उदाहरण के लिए blog posts, documentation, आदि) consume करते समय किस भाषा(ओं) में सबसे सहज हैं?

**महत्वपूर्ण**: आपका उत्तर आपकी **preference** को दर्शाना चाहिए और **नहीं** जिसमें आप communicate करने में सक्षम हैं। उदाहरण के लिए, यदि आप English और Korean दोनों में technical communication consume करने में सहज और सक्षम महसूस करते हैं, लेकिन आप हमेशा Korean पसंद करते हैं, तो आपको *केवल* Korean का उत्तर देना चाहिए क्योंकि वह आपकी preference है।

Type: select all that apply (optional)

- Chinese
- English
- French
- German
- Hindi
- Japanese
- Korean
- Portuguese
- Russian
- Spanish
- Ukrainian
- अन्य (खुला उत्तर)

> **justification**
>
> We want to understand *preference* of technical communication and how that differs
> from their abilities to consume technical communication in English.
> The languages selected are those which got 50 or more responses in 2021.

## और कुछ?

### क्या आप हमें कुछ और बताना चाहेंगे?

Type: free form (optional)

> **justification**
>
> While it's unlikely we'll receive any one piece of feedback from this question that will prove to be super useful,
> having it in the survey can still be useful. It can help us decide on new questions or perspectives that we want to
> try to capture in future surveys. It also gives respondents a place to give thanks or share a particular opinion they
> hold which can be useful in and of itself. 