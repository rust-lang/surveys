# Survey questions

Whether or not you use Rust Programming Language <https://rust-lang.org> today, we want to hear from you!

The Rust Community Team has created this survey to help us gauge how we're doing, what can be improved, and how we can best engage with all of you as we move forward.

This is your chance to have a say in the development priorities of Rust.

Your answers will be anonymous. Any personal data you submit as a part of this survey will be handled in accordance with our policy as described in our [Frequently Asked Questions](https://github.com/rust-lang/surveys/blob/main/documents/Community-Survey-FAQ.md).

We estimate it will take about 10-25 minutes to complete.

## Rust Usage

### Do you use Rust?

Type: select one

- Yes, I use Rust (for any purpose, even if you're just learning) [`NEXT`](#your-rust-experience)
- No, I don't currently use Rust, but I have in the past [`NEXT`](#for-previous-rust-users)
- No, I have never used Rust [`NEXT`](#for-non-rust-users)

> **justification**
>
> Fundamental for cohort analysis

## For previous Rust users

### Why did you stop using Rust?

Type: select all that apply

- Missing language features
- Missing libraries
- Missing tools
- Too difficult or complex to become productive writing it
- Community was rude, unwelcoming, or otherwise off-putting
- I prefer to use another language
- I no longer have the opportunity to use Rust due to factors outside of my control
- Other

### Tell us more:

Type: free text

> **SURVEY FLOW**
>
> Skip to `### To what extent is Rust currently being used by your company?`


## For non-Rust users

### Why don't you use Rust?

Type: select all that apply

- Rust did not help me achieve my goals
- Missing language features
- Missing libraries
- Missing tools
- Too difficult to learn or learning will take too much time
- Community was rude, unwelcoming, or otherwise off-putting
- I prefer to use another language
- I can't use Rust due to factors outside of my control
- I haven't got around to it
- Other

### Tell us more:

Type: free text

> **SURVEY FLOW**
>
> Skip to `### To what extent is Rust currently being used by your company?`

## Your Rust experience

### On average, how often do you use Rust?

Type: select one

- Daily or nearly so
- Weekly or nearly so
- Monthly or nearly so
- Rarely

> **justification**
>
> This can be useful demographic information as a proxy for how "important" Rust is
> in someone's technical life.
>
> We deliberately use calendar time for this question to gauge how "serious" the
> programmer's use of Rust is. This does mean that we will group together, for example,
> those who program once a week but always in Rust and those who program daily but
> use Rust once a week.

### On average, how often do you do coding/design work in general?

Type: select one

- Daily or nearly so
- Weekly or nearly so
- Monthly or nearly so
- Rarely

> **justification**
>
> Could be interesting to understand the *absolute* coding/design experience of the cohort and then compare it with *relative* Rust experience, see comment: https://github.com/rust-lang/surveys/pull/234/files#r1347513327

### How would you rate your Rust expertise?

Type: select one

- I can't write Rust code
- I can write simple programs in Rust
- I can write useful, non-trivial programs, but it is a struggle
- I am productive writing Rust

> **justification**
>
> Useful for cohort analysis, i.e., for other questions we can query if answers are significantly different for beginners vs advanced users.
>
> Previously this question was a 1-10 ranking. Having specific labels can help with consistency across responses. Additionally, having 10 choices
> was too specific (i.e., what's the difference between a 7 and 8?) where as with the new answers, we have a better idea of what the differences 
> between answers actually mean.

### When did you learn to program in Rust?

**Note**: while you may continue to try to improve your Rust skills, for this question assume "learning to program in Rust"
means spending the *majority* of your time with Rust consuming learning materials or coding *in order to learn* (as opposed to achieving
some other goal). If your learning process spans several of the listed time periods, pick the one where you felt you learned *the most*.

Type: select one (optional)

- I'm still *actively* trying to learn Rust
- During 2023
- During 2021 or 2022
- During 2019 or 2020
- During 2017 or 2018
- During 2016 or before

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

### Which operating systems do you use regularly for Rust development?

**Note**: this is specifically about which systems you personally use for development *not* all the 
systems you target.

Type: select all that apply (optional)

- Linux
- Windows 10/11
- Windows 8 or older
- Windows Subsystem for Linux
- Mac OS
- Other (open response)

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

### Which operating systems or runtimes do you develop Rust software for?

**Note**: this is specifically about which operating system or runtime you **target** not which system you use
for development nor which specific architectures (e.g., x86 vs ARM) you target.

Type: select all that apply (optional)

- Linux (desktop or server)
- Windows 10/11
- Windows 8 or older
- Mac OS
- iOS
- Android
- Embedded platforms (with an operating system)
- Embedded platforms (bare metal)
- WebAssembly
- Explicitly platform-independent (e.g., a library which does not interact with the operating system)
- Other (open response)

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

### Which version(s) of Rust do you use for development (excluding CI and other automated testing)?

Type: select all that apply (optional)

- Current stable version
- Previous stable version
- A specific version of stable Rust equal to or newer than 1.67
- A specific version of stable Rust older than 1.67
- Beta release
- Latest nightly
- A specific version of nightly
- Custom fork
- I don't know
- Other

> **justification**
>
> Together with the following question, we can better determine what the spread of 
> version usage is across the community.
> We ask specifically about version 1.67 since it is, at the time of the survey, the 
> version that was released ~1 year prior. Additionally, at the time of this writing
> all major Linux distros have a version equal to or newer than this version.

### If you use nightly for any tasks, why?

Type: select all that apply (optional)

- I don't use nightly
- Out of habit
- For a particular language feature or set of language features I need
- I like to have access to all the latest features
- To help test the nightly version for bugs
- To provide design feedback on nightly features
- For testing in CI
- A crate dependency I use requires it
- A tool I use requires it
- To have faster compile times
- Other (open response)

> **justification**
>
> We'd like to know what are the common reasons people use nightly
> so that we can better understand where testers are coming from.

### What is the oldest version of Rust you use for any development task?

Excluding testing to ensure your code works on that compiler version.

Type: select one (optional)

1.76 (nightly), 1.75 (nightly), and then every version from 1.74 to 1.0 in descending order, and "a pre-1.0 version"

> **justification**
>
> To get real data on how many people use older versions of the toolchain to
> inform discussion on MSRVs.

### Which editor or IDE setup do you use with Rust code on a regular basis?

Type: select all that apply (optional)

- VS Code
- vi/vim/neovim
- IntelliJ/CLion/other JetBrains IDE + Rust plugin
- Rust Rover (dedicated IntelliJ Rust IDE)
- Emacs (or derivatives like Doom Emacs, Spacemacs, etc.)
- Sublime Text
- Visual Studio
- Xcode
- Atom
- Other (open response)

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

## The Rust community

### Roughly how often do you participate in the Rust community?

Type: matrix (optional)

Activities:

- Produce informational content about Rust (e.g., blogged, live streamed, made a YouTube video, presented at a conference/meetup, etc.)
- Consume informational content about Rust (e.g., blogs, live streams, YouTube videos, etc.)
- Read official Rust communication channels (e.g., This Week in Rust, the official Rust blog, the Rust Twitter account, etc.)
- Participate in conversations about Rust on social media or websites (Hacker News, r/rust, Twitter, LinkedIn, etc.)
- Attend a Rust meetup or conference (virtual or in-person)
- Write, comment on, contribute to discussion of, or provide edits to an open RFC
- Discuss the Rust project in an official chat (internals.rust-lang.org, rust-lang Zulip, etc.)
- Open an issue on any project in the rust-lang GitHub organization
- Contribute code changes (including tests) to any project in the rust-lang GitHub organization
- Contribute non-code changes (documentation, comments, etc.) to any project in the rust-lang GitHub organization

Frequency:
- More frequently than weekly
- Weekly
- Monthly or less frequently
- Never

> **justification**
>
> We want to understand the nature of contribution to the Rust project both
> to better understand the shape of community involvement and for cohort analysis.

### How do you feel in the Rust community?

Type: matrix

Activities:

- *Official* Rust community forums or chats (users.rust-lang.org, internals.rust-lang.org, the official Rust Discord, or the Rust Zulip)
- *Unofficial* Rust community forums or chats (e.g., reddit.com/r/rust, Hacker News, the Rust *Community* Discord, etc.)
- Community focused on a specific area of Rust software development (e.g. game development, audio, etc.)
- Attending a Rust conference
- Attending a Rust meetup or local community event
- Discussion (issues, pull requests, etc.) on a repository *inside* the rust-lang GitHub organization
- Discussion (issues, pull requests, etc.) on a Rust repository *outside* of the rust-lang GitHub organization

Choices:

- I feel welcome
- I do not feel particularly welcome or unwelcome
- I feel unwelcome
- I've never participated in this activity

> **justification**
>
> We'd like to know where people are feeling welcome and the degree to which they are feeling welcome.


### If you indicated that you did not feel welcome in the Rust community, are there any details about your experience that you would like to share with us?

Type: free form (optional)

> **justification**
> 
> More detail on the type of situations where people have felt unwelcome can let us better 
> address these issues in the future.

## Rust in Education

### Are you currently, or have you in the last year, taken a course or training which uses or teaches Rust?

Type: select one (optional)

- Yes, through a university, school, or other educational institution
- Yes, through my employer, contractor, or consultancy
- No

> **justification**
>
> This question is primarily used to funnel respondents into the more specific questions about the kinds of educational activities they've been a part of.

### If you consumed learning material about Rust, which kind of material did you consume?

Type: select all that apply (optional)

- Books ("The Rust Programming Language", "Rust for Rustaceans", etc.)
- Online exercises (Rustlings, Rust by Example, etc.)
- Videos
- Online courses, webinars
- Other (please specify)

> **justification**
> Justification: getting data here seems helpful for guiding users / recommending public content.

## Rust at work

### Are you employed full- or part-time (including paid internships)?

Type: select one

- Yes
- No [`NEXT`](#your-opinions-about-rust)

### Do you write or design software in your work?

Type: select one (optional)

- Yes, primarily as an individual contributor (i.e., non-manager)
- I primarily manage others who do
- No [`NEXT`](#your-opinions-about-rust)

### Are you personally using Rust at work?

Type: select one

- Yes, for the majority of my coding
- Yes, but I only use it occasionally
- No [`NEXT`](#to-what-extent-is-rust-currently-being-used-by-your-company)

> **justification**
>
> We want to establish what percentage of those who could possibly use Rust in a professional setting
> are using Rust in a professional setting. This is most interesting over time.
> Answers to this question should be combined with whether the respondent has ever used Rust.


### Which of the following statements are reasons why you use Rust at work?

Type: select all that apply (optional)

Statements:

- For its performance (i.e., speed, memory footprint, etc.) characteristics
- We need precise control over exactly how our software runs
- Its security and safety properties are important to us
- It allows us to build relatively correct and bug free software
- We find it enjoyable or fun to program in Rust
- We already know Rust so it's our default choice
- We find it easy to prototype with
- We must interact with existing Rust code

> **justification**
>
> The Rust community and potential adopters of Rust have a lot of assumptions of why one would choose Rust for a project.
> This question can help confirm or challenge our assumptions and see how they change over time.


### Which of the following statements apply to your experience using Rust at work?

Type: select all that apply (optional)

Statements:

- Using Rust has helped us achieve our goals
- Adopting Rust has been challenging
- Overall, adopting Rust has slowed down our team
- Using Rust has been worth the cost of adoption
- We're likely to use Rust again in the future

> **justification**
>
> Future potential adopters may want to know how often other's have encountered success.

### What about your usage of Rust has been challenging?

Type: free form (optional)

> **justification**
>
> This an opportunity to learn from adopters at companies what they struggle with when adopting Rust.


### To what extent is Rust currently being used by your company?

Type: select one

- My company makes non-trivial use of Rust (e.g., used in production or in significant tooling)
- My company has experimented with Rust or is considering using it
- My company has not seriously considered Rust for any use [`NEXT`](#approximately-how-many-total-developers-does-your-company-employ)
- I am unsure whether my company has considered using or currently uses Rust [`NEXT`](#approximately-how-many-total-developers-does-your-company-employ)

> **justification**
>
> We want to establish how reliant companies are on Rust.


### In what technology domain(s) is Rust used at your company?

If you've previously answered that your company is not actively using Rust, you can leave this question blank.

Type: select all that apply (optional)

- Audio programming
- Blockchain
- Cloud computing applications
- Cloud computing infrastructure or utilities
- Command Line Interfaces (CLI)
- Computer graphics
- Computer games
- Computer networking
- Computer security
- Data science
- Database implementation
- Desktop computer application frontend
- Desktop computer or mobile phone libraries or services
- Distributed systems
- Embedded devices (with operating systems)
- Embedded devices (bare metal)
- HPC (High-performance [Super]Computing)
- IoT (Internet of Things)
- Machine learning or AI
- Mobile phone application frontend
- Programming languages and related tools (including compilers, IDEs, standard libraries, etc.)
- Robotics
- Scientific and/or numerical computing
- Server-side or "backend" application
- Simulation
- Web application frontend
- WebAssembly
- Other (open response)

> **justification**
>
> We want to known roughly what technology stacks are being most often used.
>
> This can be ambiguous and hard to answer. For example, if you're building an operating
> system for a mobile phone, is that embedded, mobile, or something else?
> We want to understand the "shape" of Rust usage, and this question tries to get at that
> by allowing the respondent to select multiple answers.

### Approximately how many total developers does your company employ?

**Note**: don't worry about being exact here! Go with you gut.

Type: select one (optional)

- Under 10
- 10-99
- 100-1,000
- 1,000-10,000
- Over 10,000

> This question is not that interesting on its own, but it can be used as a sort of cohort for understanding how answers
> change depending on the size of the development effort at a company.
>
> Previously this question used "employees" instead of "developers". It is more appropriate for us to ask about the amount
> of developers at a company vs. the amount of people employed in total.

### Is your company planning on hiring Rust developers in the next year?

Type: select one (optional)

- Yes
- No (it is planning to hire other developers)
- No (it is not planning to hire any developers)
- I don't know

> This question assess hiring sentiment. Although there is intrinsic uncertainty, it is easy to answer and forward looking.
> It will also be interesting to see what the demand for Rust skills from companies is over time.

## Your opinions about Rust

### Which of the following statements about Rust do you feel are true?

Type: select all that apply (optional)

Statements:

- Rust provides a real benefit over other programming languages
- Rust is significantly more complicated to program in than other programming languages
- Rust requires significantly more effort to learn than other programming languages
- Rust code tends to contain significantly fewer bugs than equivalent code written in another programming language would have
- Rust is risky to use in production
- Rust makes me more productive
- Rust is fun to use

> **justification**
>
> There are several "truisms" about Rust that we'd like to get perspective on how true these are for users of Rust.
>
> Note that answers here can be subject to survivorship bias and so extra care should be taken with interpreting results.


### What are your biggest worries for the future of Rust?

Type: select all that apply (optional)

- Not enough usage in industry
- Too much interest from big companies
- Not enough open source contributions to the ecosystem
- Doesn't add a specific feature I want
- Rust doesn't evolve quickly enough
- Instability of the language
- Superseded by an alternative
- Becomes too complex
- Tools and documentation are not accessible enough (e.g., due to language or incompatibility with screen readers)
- Rust Foundation not supporting the Rust project properly (e.g. in financial, infrastructure, legal aspects)
- Project governance does not scale to match the size/requirements of the community
- Developers/maintainers of the language are not properly supported
- I'm not worried
- Other (open response)

> **justification**
>
> Would be useful for leadership to understand the community's fears.

### In your opinion, how would you prioritise work on the following aspects of Rust?

Type: ordered list (optional)

Aspects:

- Runtime performance
- Compile times
- Binary size
- Memory usage (i.e., how much RAM rustc uses when compiling)
- Disk space usage (e.g., the size of target folder)
- Bugs in the compiler (i.e., ICEs a.k.a. internal compiler errors, miscompilations, etc.)
- Compiler error messages
- IDE experience
- Debugging experience
- Documentation (rustdoc, docs.rs)
- Build system (cargo)
- Package management (crates.io)
- New language features
- Rust language and standard library documentation

> **justification**
>
> This question gathers data on the communities perceptions of certain aspects of Rust at this point in time.

### Which unimplemented or (nightly only) features are you looking for to be stabilized?

Please mention here features for the *Rust compiler* that are currently behind a feature gate (only available using an unstable/nightly release of the Rust compiler) or a feature that is missing and in your opinion would be beneficial to the Rust ecosystem or to your work. This list excludes other tooling around the compiler such as cargo, rustup, rustfmt, etc.

Type: ordered list (optional)

Nightly or unstable feature:

- I wish the Rust project to not add major new features (or slow down the pace of development)
- Specialization ([RFC#1210](https://github.com/rust-lang/rust/issues/31844))
- Generators/coroutines ([RFC#2033](https://github.com/rust-lang/rust/issues/43122))
- Async closures ([RFC#2532](https://github.com/rust-lang/rust/issues/62290))
- If/while let chains ([eRFC#2497](https://github.com/rust-lang/rust/issues/53667))
- Try blocks ([RFC#243](https://github.com/rust-lang/rust/issues/31436))
- Never type ([RFC#1216](https://github.com/rust-lang/rust/issues/35121))
- Improved traits (trait alias, implied bounds, associated type defaults)
- Improved const (generic const expressions, const expr for custom types, const trait methods)
- Compile time reflection (variadic generics)
- Enum variant types ([RFC#2593](https://github.com/rust-lang/lang-team/issues/122))
- Allocator trait, better OOM handling (https://github.com/rust-lang/rust/issues/32838)
- Stable ABI (https://github.com/rust-lang/rust/issues/111423)
- Other (please specify)

> **justification**
>
> Allow the cohort to mention specific language features they might be eagerly waiting for, see https://github.com/rust-lang/surveys/pull/234/files#r1347633041

### Which of these problems do you recall encountering within the last year?

Type: select all that apply (optional)

- Implementing things on tuples
- Splitting things across crates
- Having to do iterator implementations manually
- Not being able to do enough in const fn
- Needing to drop down to C ABI for rust plugins
- Async
- Traits and generics
- Borrow checker
- Macros
- Other (please specify)

> **justification**
>
> Conversely, try asking which /problems/ they encountered and let the Rust project figure out what is needed to improve in these areas

### How do you build your Rust projects?

Type: select all that apply (optional)

Aspects:

- I use Cargo
- I use some other build system
- I combine Cargo and another build system
- If you combine Cargo with (or just use) other build systems, which ones? (open response)

> **justification**
>
> cargo team expressed interest in this, see https://rust-lang.zulipchat.com/#narrow/stream/246057-t-cargo/topic/Rust.20survery.202023/near/393816653

### How do you download crates to build Rust projects?

Type: matrix (optional)

Aspects:
- I use crates.io
- I use a custom/local/company registry
- I use a mirror of crates.io
- I don't know

> **justification**
>
> It could be interesting to know how many people use crates.io vs some custom/local/company registry, and how many people are even aware of what registry do they use. See issue surveys#236.

### Do you agree with the following statements on Rust stability?

Type: matrix (optional)

Statements:

- I can upgrade the *stable* compiler version without fear of my code failing to compile
- I can upgrade the *nightly* compiler version without fear of my code failing to compile
- Upgrading to a new *stable* compiler version requires either no changes or extremely small & easy changes to my code
- Upgrading to a new *nightly* compiler version requires either no changes or extremely small & easy changes to my code

Rating:

- Agree
- Disagree

> **justification**
>
> When want to get an impression of how stable the compiler *feels*. Impressions are more important than hard numbers as
> not all users define stability in the same way the compiler does.

### Do you agree with the following statements on Rust employment?

Type: matrix (optional)

Statements:

- It is easy for qualified applicants to find jobs which use Rust for the majority of programming
- Existing Rust jobs are attractive

Rating:

- Agree
- Neither agree nor disagree
- Disagree

> **justification**
>
> The flip side of the question asking whether the respondent's company plans on hiring Rust developers, we
> want to know how respondents feel the level of demand for and quality of Rust jobs are.

## About you

See [who](./design/who.md).

The following are primarily for cohort analysis, secondarily for understanding the shape of the community.

For methodological purposes, the bulk of the demographics should be at the end of the survey (unless acting as filter/flow questions above).
They're both easy to complete (beneficial at the end) and somewhat personal (but at this point folks are invested and we've built 'trust').
Can also be problematic at start if we're asking all easy, personal questions and then get to the harder ones - easy to drop out.

### Do you consider yourself a member of a group which is underrepresented or marginalized in technology?

Please share only what you are comfortable sharing. This will help us better serve underrepresented and marginalized groups, better understand how well our outreach efforts are going, and more.

Type: select one

- Yes
- No
- I prefer not to say

### Do you consider yourself part of any of the following underrepresented or marginalized groups?

Please share only what you are comfortable sharing. This will help us better serve underrepresented and marginalized groups, better understand how well our outreach efforts are going, and more.

Type: select all that apply (optional)

- Cultural beliefs
- Disabled (physically, mentally or otherwise)
- Neurodivergent
- Educational background
- Language
- Lesbian, gay, bisexual, queer or otherwise non-heterosexual
- Non-binary gender
- Older than the average developer I know
- Younger than the average developer I know
- Political beliefs
- Racial or ethnic minority
- Religious beliefs
- Trans
- Woman or perceived as a woman
- Other (open response)

### Are you a full- or part-time student?

Type: select one (optional)

- No
- Yes, in secondary/high school
- Yes, in a bachelor's/undergraduate program
- Yes, in a master's program
- Yes, in a doctorate program
- Yes, in a vocational program
- Yes, other

> **justification**
>
> This will be important for cohort analysis. In particular, we want to
> understand how students at different points in their education view
> topics related to Rust.

### How long have you been programming (in any language, for any reason)?

Type: select one (optional)

- < 1 year
- < 3 years
- < 5 years
- < 10 year
- > 10 years

### Where do you live?

Type: select one (optional)

- *all UN member states*
- *two observer states (Vatican City and Palestine)*
- Taiwan
- Other

> **justification**
>
> We'd like to get a geographic understanding of where the community is. To have more structure, a free-form answer
> is not used, and instead we use the country definition according to UN.

### In what ways are you comfortable communicating about technical topics in English?

Type: select all that apply (optional)

- I feel comfortable and capable of having a spoken technical conversation in English
- I feel comfortable and capable of having a written technical conversation in English
- I feel comfortable and capable of reading technical documentation in English
- I feel comfortable and capable of consuming a technical talk (e.g., at a conference or meetup) in English
- I feel comfortable and capable of consuming a written technical educational material (e.g., technical books, blog posts, etc.) in English

> **justification**
>
> We want to understand self reported feeling of comfort and capability of communication
> of English since a large portion of the Rust community is and likely will always be in English.

### What is/are your preferred language(s) for technical communication?

**IMPORTANT**: Your answer should reflect your **preference** and **not** what you are capable of communicating in. For example, if you feel comfortable and capable of consuming technical communication in both English and Korean, but you always prefer Korean, you should *only* answer Korean as that is your preference.

Type: select all that apply (optional)

- Chinese
- English
- French
- German
- Hindi
- Japanese
- Korean
- Polish
- Portuguese
- Russian
- Spanish
- Other (open response)

> **justification**
>
> We want to understand *preference* of technical communication and how that differs
> from their abilities to consume technical communication in English.
> The languages selected are those which got 50 or more responses in 2021.

## Anything else?

### Is there anything else you'd like to tell us?

Type: free form (optional)

> **justification**
>
> While it's unlikely we'll receive any one piece of feedback from this question that will prove to be super useful, 
> having it in the survey can still be useful. It can help us decide on new questions or perspectives that we want to
> try to capture in future surveys. It also gives respondents a place to give thanks or share a particular opinion they
> hold which can be useful in and of itself.
