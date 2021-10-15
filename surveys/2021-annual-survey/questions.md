# Survey questions

Whether or not you use Rust Programming Language <https://rust-lang.org> today, we want to hear from you!

The Rust Community Team has created this survey to help us gauge how we're doing, what can be improved, and how we can best engage with all of you as we move forward.

This is your chance to have a say in the development priorities for Rust.

Unless you choose to enter your email, your answers will be anonymous. Any personal data you submit as a part of this survey will be handled in accordance with our policy as described in our Frequently Asked Questions:

https://github.com/rust-community/team/wiki/State-of-the-Rust-Language-Community-Survey-FAQ

We estimate it will take about 10-15 minutes to complete.

> TODOs:
>
> - Ensure that the survey actually takes 10-15 minutes

## Rust Usage

### Do you use Rust?

Type: select one

- Yes, I use Rust [`NEXT`](#your-rust-experience)
- No, I don't currently use Rust, but I have in the past [`NEXT`](#for-previous-rust-users)
- No, I have never used Rust [`NEXT`](#for-non-rust-users)

> **justification**
>
> Fundamental for cohort analysis

## For previous Rust users

### As you have indicated that you're no longer using Rust, what prompted you to participate in this survey?

Type: select all that apply

- I plan to return to using Rust in the future.
- I consider myself part of the Rust Community.
- Specifically to provide feedback on why I stopped using Rust.
- To provide feedback on Rust in general.
- Curiosity.
- Other (open response)

> **justification**
>
> Useful in understanding why non-users contribute;

> **SURVEY FLOW**
>
> Skip to `## About You` section

## For non-Rust users

### As you have indicated that you have not used Rust, what prompted you to participate in this survey?

Type: select all that apply

- I plan to use Rust in the future.
- I consider myself part of the Rust Community.
- Specifically to provide feedback on WHY I do not use Rust.
- Curiosity.
- Other (open response)

> **justification**
>
> Useful in understanding why non-users contribute to the survey

> **SURVEY FLOW**
>
> Skip to `## About You` section

## Your Rust experience

### When did you learn to program in Rust?

**Note**: while you may continue to try to improve your Rust skills, for this question assume "learning to program in Rust"
means spending the *majority* of your time with Rust consuming learning materials or coding *in order to learn* (as opposed to achieving
some other goal). If your learning process spans several of the listed time periods, pick the one where you felt you learned *the most*.

Type: select one

- I'm still *actively* trying to learn Rust
- During 2021
- During 2019 or 2020
- During 2017 or 2018
- During 2015 or 2016
- During 2014 or before

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

### How would you rate your Rust expertise?

Type: select one

- I can't write or read Rust
- I can write simple programs in Rust
- I can write useful, production-ready code but it is a struggle
- I am productive writing Rust
- I'm an expert

> **justification**
>
> Useful for cohort analysis, i.e., for other questions we can query if answers are significantly different for beginners vs advanced users.

### Which of the following activities do you find helpful or effective for learning Rust or improving your Rust skills?

Type: select all that apply

- Reading books or other written material geared towards learning Rust
- Watching videos, streams, etc. geared towards learning Rust
- Attending an organized training session or course (in person or virtual)
- Doing Rust coding exercises or challenges created to help learn Rust
- Building a non-trivial project in Rust or contributing to an open source project

> **justification**
>
> We'd like to confirm what learning materials are popular with the community. This
> combined with some cohort analysis can tell us about how particular subsections
> of the community prefer to learn.

### How often do you use Rust?

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

### How much do you agree with the following statements

Type: matrix

Statements:

- Rust provides a real benefit over other programming languages
- Rust is complicated to use
- Rust is complicated to learn
- Rust is risky to use in production
- Rust makes me more productive
- Rust is fun to use

Rating:

- Strongly agree
- Agree
- Neither agree nor disagree
- Disagree
- Strongly disagree

> **justification**
>
> There are several "truisms" about Rust that we'd like to get perspective on how true these are for users of Rust.
>
> Note that answers here can be subject to survivorship bias and so extra care should be taken with interpreting results.

### Which operating systems do you use regularly for Rust *development*?

Note: this is specifically about which systems you use for development *not* all the 
systems you target.

Type: select all that apply

- Linux
- Windows
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

### On the primary machine you compile Rust code on, how many logical CPU threads do you have?

Please count logical CPUs here, not cores or sockets. You can get this number by running the following commands from the command line:

- Linux: `nproc`
- macOS: `sysctl -n hw.ncpu`
- Windows Command Prompt: `echo %NUMBER_OF_PROCESSORS%`
- Windows PowerShell: `(Get-CimInstance Win32_ComputerSystem).NumberOfLogicalProcessors`

Type: free form (optional).

> **justification**
>
> Question added by Josh Triplett. The answers can help tune parallel rustc:
>
> - When we encounter a scalability issue that starts at a certain number of CPUs, it'll be good to know what proportion of the Rust community is affected.
> - It'll help when tuning algorithms or build systems whose memory usage may depend on the number of CPUs present.
> - It'll help with prioritization around whether to make something go faster by throwing more CPUs at it or by optimizing on the same number of CPUs.
> - It'll help avoid assumptions that rust developers might otherwise make about how universal the caliber of hardware they have is.

### Which operating systems do you develop Rust software for?

Note: this is specifically about which systems you **target** not which system you use
for development.

Type: select all that apply

- Linux (desktop or server)
- Windows
- Mac OS
- iOS
- Android
- Embedded platforms (with an operating system)
- Embedded platforms (bare metal)
- Other (open response)

> **justification**
>
> This question can be used to figure out roughly what systems are being targeted as well as 
> what OS stack is being developed against (i.e., desktop/server OS, mobile OS, embedded OS, bare metal)
>
> We're using "Linux" here rather than "*nix" or similar, with the same
> justification as in the "Which operating systems do you use" question.

### Which version(s) of Rust do you use for local development?

Type: select all that apply

- Current stable version
- Previous stable version
- Some other specific version of stable Rust
- Beta release
- Latest nightly
- A specific version of nightly
- Custom fork
- I don't know
- Other (open response)

> **justification**
>
> Together with the following question, we can better determine what the spread of 
> version usage is across the community.

### Which version(s) of Rust do you use in automated testing (e.g., CI)?

Type: select all that apply

*Same answers as above*

> **justification**
>
> See the previous question.

### Please rate how much you agree with the following statements on Rust stability.

Type: matrix

Statements:

- I can upgrade the *stable* compiler version without fear of my code failing to compile.
- I can upgrade the *nightly* compiler version without fear of my code failing to compile.
- I can upgrade the *stable* compiler version without fear of my code taking longer to compile.
- I can upgrade the *nightly* compiler version without fear of my code taking longer to compile.
- Upgrading to a new *stable* compiler version requires either no changes or extremely small & easy changes to my code.
- Upgrading to a new *nightly* compiler version requires either no changes or extremely small & easy changes to my code.

Rating:

- Strongly agree
- Agree
- Neither agree nor disagree
- Disagree
- Strongly disagree
- No opinion

> **justification**
>
> When want to get an impression of how stable the compiler *feels*. Impressions are more important than hard numbers as
> not all users define stability in the same way the compiler does. For example, experiencing compiler performance regressions
> in a new version of the compiler isn't breaking official stability guarantees but it can feel just as painful as an
> actual breaking change.

### If you use nightly, why?

Type: select all that apply

- I don't use nightly
- Out of habit
- For a particular language feature or set of language features I need
- To help test the nightly version for bugs
- For testing in CI
- A dependency I use requires it
- Other (open response)

> **justification**
>
> We'd like to know what are the common reasons people use nightly
> so that we can better understand where testers are coming from.

### If you use beta, why?

Type: select all that apply

- I don't use beta
- Out of habit
- To adopt stabilized language features as early as possible
- To help test the beta version for bugs
- For testing in CI
- Other (open response)

> **justification**
>
> Same justification as the question about nightly but for beta.

### What ways do you install Rust?

Type: select all that apply

- rustup
- Linux distribution package
- Homebrew
- Official rust-lang.org tarballs
- Official Windows .msi installers
- Official macOS .pkg installers
- From source
- Other (open response)

> **justification**
>
> Since many of these sources are not under project control, it can be hard to know where
> people are getting their Rust compiler from.

### In your opinion, how do you find the following aspects of Rust?

Type: matrix

Aspects:

- Compile times
- Binary size
- Disk space (e.g., the size of `target` folder)
- Bugs in the compiler (i.e., ICEs a.k.a. internal compiler errors, miscompilations, etc.)
- Compilation error messages
- IDE experience
- Available tools and support
- Async programming
- GUI development
- Rust language and standard library documentation

Options:

- Great
- Good enough
- Could be better
- Seriously lacking

> **justification**
>
> This question gathers data on the communities perceptions of certain aspects of Rust at this point in time.

### In your opinion, have the following aspects of Rust gotten better or worse over the past year?

Type: matrix

Aspects:

*same aspects as the previous question*

Options:

- Much better
- Better  
- Remained the same  
- Worse
- Much Worse
- Unsure

> **justification**
>
> This question gathers data on the communities perceptions of certain aspects of Rust over the last year.

### Please indicate how vital to your workflow each of the following tools are when programming with Rust:

Type: matrix

Options:

- Essential
- Somewhat important
- Not important
- I have no experience with this tool

Tools:

- clippy
- cargo
- rustdoc
- rustup
- play.rust-lang.org
- miri
- rustfmt
- bindgen

> **justification**
>
> Understanding how important certain tools are to the community and *more importantly* to 
> certain subsections of the community is important.

### Which editor or IDE setup do you use on a regular basis?

Type: select all that apply

- VS Code
- vi/vim/neovim
- IntelliJ Rust
- Emacs
- Sublime
- Visual Studio
- Xcode
- Atom
- CLion
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

### In which of the following ways have you participated in the Rust community in the last 6 months:

Type: select all that apply

- I have produced informational content about Rust (e.g., blogged, live streamed, made a YouTube video, etc.).
- On several occasions I have consumed informational content about Rust (e.g., blogs, live streams, YouTube videos, etc.).
- On several occasions I have read *comments* about Rust content on "news" sites (e.g., Hacker News, reddit.com/r/rust, lobste.rs/t/rust, etc.)
- On several occasions I have *commented* on Rust content on "news" sites (e.g., Hacker News, reddit.com/r/rust, lobste.rs/t/rust, etc.)
- On several occasions I have read official Rust communication channels (e.g., This Week in Rust, the official Rust blog, the Rust Twitter account, etc.)
- On several occasions I have participated in conversations about Rust on social media (Twitter, Facebook, LinkedIn, etc.)
- I have participated in Rust community forums or chats (e.g., users.rust-lang.org, Rust Discord, a local Rust chat community, etc.)
- I have attended a Rust meetup or conference (virtual or in-person).

> **justification**
>
> We'd like to get a picture of _how_ people participate in the Rust community. In
> particular we can use this information to do cohort analysis on highly "active"
> community members in comparison to less active community members.

### How often have you felt *un*welcome in the Rust community?

Type: matrix

Activities:

- *Official* Rust community forums or chats (users.rust-lang.org, internals.rust-lang.org, the official Rust Discord, or the Rust Zulip)
- *Unofficial* Rust community forums or chats (e.g., reddit.com/r/rust, Hacker News, the Rust *Community* Discord, etc.)
- Attending a Rust conference
- Attending a Rust meetup or local community event
- Discussion (issues, pull requests, etc.) on a repository *inside* the rust-lang GitHub organization
- Discussion (issues, pull requests, etc.) on a repository *outside* of the rust-lang GitHub organization

Choices:

- I've *often* felt unwelcome
- I *sometimes* feel unwelcome
- I *never* feel unwelcome
- I've never participated in this activity

> **justification**
>
> We'd like to know if any of the officially moderated spaces in the Rust community tend to produce feelings
> of unwelcome which made indicate that we need to more aggressively moderate those spaces.

### If you indicated that you did not feel welcome in the Rust community, are there any details about your experience that you would like to share with us?

Type: free form (optional)

> **justification**
> 
> More detail on the type of situations where people have felt unwelcome can let us better 
> address these issues in the future.

### Roughly how often do you actively contribute to the Rust project?

Activities:

- Comment on, contribute to discussion of, or provide edits to an open RFC
- Create a new thread or comment on internals.rust-lang.org
- Discuss Rust project  in an official chat (either Zulip or Discord)
- Open an issue on any repo in the rust-lang GitHub org
- Contribute code changes (including tests) to the Rust compiler (rust-lang/rust)
- Contribute code changes (including tests) to any other project in the rust-lang GitHub org
- Contribute non-code changes (documentation, comments, etc.) to any project in the rust-lang GitHub org.

Type: select one

- Daily
- Weekly
- Monthly
- Less frequently than monthly
- Never but have tried to
- Never and have never tried to

> **justification**
>
> We want to understand the nature of contribution to the Rust project both
> to better understand the shape of community involvement and for cohort analysis.

### How many open-source and non-personal Rust projects do you currently maintain?

- Non-personal: at least one other person also contributes and the project is meant for others and not just yourself.
- Maintain: you have review and merge privileges

Type: select one

- 0
- 1
- 2-4
- 5-10
- More than 10

> **justification**
>
> We would like to know the rough make up of those who are using Rust in general
> vs those who actively participate in development of open source Rust projects.

### How many open-source and non-personal Rust projects do you currently contribute to (not including those you maintain)?

- Non-personal: at least one other person also contributes and the project is meant for others and not just yourself.
- Contribute: you *regularly* provide code, tests, documentation, issues, etc.
- Maintain: you have review and merge privileges

Type: select one

- 0
- 1
- 2-4
- 5-10
- More than 10

> **justification**
>
> We would like to know the rough make up of those who are using Rust in general
> vs those who actively participate in development of open source Rust projects.

## Rust at work

> This section is largely in service of the [contexts](./design/contexts.md) design document.

### Are you using Rust at work?

Type: select one

- Yes, for the majority of my coding
- Yes, it's one of a number of languages I use and I use it regularly
- Yes, but I only use it occasionally
- No

> **justification**
>
> We want to establish what percentage of those who could possibly use Rust in a professional setting
> are using Rust in a professional setting. This is most interesting over time.
> Answers to this question should be combined with whether the respondent has ever used Rust.

### To what extent is Rust currently being used by your company?

Type: select one

- My company uses Rust for a large portion of production projects.
- My company uses Rust for a small portion of production projects.
- My company uses Rust only for non-production projects (e.g., tooling).
- My company has actively experimented with Rust
- My company has seriously considered, but not experimented with, using Rust.
- My company has not seriously considered Rust for any use.
- I am unsure whether my company has considered using or currently uses Rust.
- I don't work for a company or my company does not develop software of any kind.

> **justification**
>
> We want to establish how reliant companies are on Rust.

### In what technology domains is Rust used at your company?

Type: select all that apply

- Server-side application
- Desktop application
- Mobile application
- Web application
- Embedded application
- Other (open response)

> **justification**
>
> We want to known roughly what technology stacks are being most often used.
>
> **challenges**
>
> This can be ambiguous and hard to answer. For example, if you're building an operating
> system for a mobile phone, is that embedded, mobile, or something else.
> We want to understand the "shape" of Rust usage, and this question only gets at that
> in one particular way.

### Approximately how many total developers does your company employ?

Note: don't worry about being exact here! Go with you gut.

Type: select one

- Under 10
- 11-49
- 50-99
- 100-500
- 500-1,000
- 1,000-10,000
- Over 10,000

> This question is not that interesting on its own, but it can be used as a sort of co-hort for understanding how answers 
> change depending on the size of the development effort at a company.
>
> Previously this question used "employees" instead of "developers". It is more appropriate for us to ask about the amount
> of developers at a company vs. the amount of people employed in total.

### Is your company planning on hiring Rust developers in the next year?

Type: select one

- Yes
- No
- I don't know or I don't work at company that would hire software developers.

> This question assess hiring sentiment. Although there is intrinsic uncertainty, it is easy to answer and forward looking.
> It will also be interesting to see what the demand for Rust skills from companies is over time.

### Rate how much the follow statements are reasons your team use Rust at work.

Type: matrix

Statements:

- We use Rust for its performance (i.e., speed, memory footprint, etc.) characteristics.
- We use Rust because we need *precise control* over exactly how our software runs.
- Rust security and safety properties are important to us.
- Rust allows us to build relatively correct and bug free software.
- We find it enjoyable or fun to program in Rust.
- We already know Rust so it's our default choice.
- We find it easy to prototype with.
- Other (open response)

Rating:

- Strongly agree
- Agree
- Neither agree nor disagree
- Disagree
- Strongly disagree

> **justification**
>
> The Rust community and potential adopters of Rust have a lot of assumptions of why one would choose Rust for a project.
> This question can help confirm or challenge our assumptions and see how they change over time.

### Please rate your experience using Rust at work.

Type: matrix

Statements:

- Using Rust has helped us achieve our goals
- Adopting Rust has been challenging
- Overall, adopting Rust has slowed down our team
- Using Rust has been worth the cost of adoption
- We're likely to use Rust again in the future

Rating:

- Strongly agree
- Agree
- Neither agree nor disagree
- Disagree
- Strongly disagree

> **justification**
>
> Future potential adopters may want to know how often other's have encountered success.

### What about your usage of Rust has been challenging?

Type: free form

> **justification**
>
> This an opportunity to learn from adopters at companies what they struggle with when adopting Rust.
>
> **SURVEY FLOW**
>
> Only show this question if the respondent indicated their adoption was not a smashing success.

## Rust in education

> This section is largely in service of the [contexts](./design/contexts.md) design document.

### Have you taken in the past year or are you currently taking a course or training which uses or teaches Rust?

Type: select one

- Yes [`NEXT`](#where-is-the-course-or-activity-taught)
- No [`NEXT`](#what-is-your-biggest-worry-for-the-future-of-rust)

> **justification**
>
> This question is primarily used to funnel respondents into the more specific questions about the kinds of educational activities they've been a part of.

### Where is the course or activity taught?

Type: select one

- University or other tertiary institute
- High school or secondary school
- A course through an *online* "continuing education" provider (e.g., Udemy, Coursera, edX, LinkedIn Learning, etc.)
- A bootcamp or other vocational-focused educational institute
- A short training course offered through your employer or contracted by your employer

> **justification**
>
> We want to know where Rust is being taught.

### Which best describes your course or activity?

Type: select one

- A course teaching exclusively how to program in Rust
- A course teaching how to program in Rust and other languages
- A computer science course (e.g., operating systems, algorithms, etc.) course which uses Rust (and potentially other languages)
- Other type of course where Rust was used

> **justification**
>
> We want to know how Rust is being taught.

### Is Rust mandated for your course or activity, or did you choose it yourself?

Type: select one

- Rust was mandated
- I chose to use Rust

> **justification**
>
> Together with the above question, we want to know how Rust is being taught.

## Your opinions about Rust

### What are your biggest worries for the future of Rust?

Type: select all that apply

- Not enough usage in industry
- Too much interest from big companies
- Not enough open source contributions to the ecosystem
- Doesn't add a specific feature I want
- Rust doesn't evolve quickly enough
- Instability of the language
- Superseded by an alternative
- Becomes too complex
- Tools and documentation are not accessible enough (e.g., due to language or incompatibility with screen readers)
- Other (open response)
- I'm not worried

> **justification**
>
> Would be useful for leadership to understand the community's fears.

### How much do you agree with the following statements on Rust employment?

Type: matrix

Statements:

- It is easy for qualified applicants to find jobs which use Rust for the majority of programming
- Existing Rust jobs are attractive
- Learning Rust provides me with skills that employers seek
- I feel qualified to apply for at least some advertised Rust jobs

Rating:

- Strongly agree
- Agree
- Neither agree nor disagree
- Disagree
- Strong disagree

> **justification**
>
> The flip side of the question asking whether the respondent's company plans on hiring Rust developers, we
> want to know how respondents feel the level of demand for and quality of Rust jobs are.

## Demographics

> For methodological purposes, the bulk of the demographics should be at the end of the survey (unless acting as filter/flow questions above)
> They're both easy to complete (beneficial at the end) and somewhat personal (but at this point folks are invested and we've built 'trust')
> Can also be problematic at start if we're asking all easy, personal questions and then get to the harder ones - easy to drop out.

## About you

See [who](./design/who.md).

The following are primarily for cohort analysis, secondarily for understanding the shape of the community.

### Do you consider yourself a member of an underrepresented or marginalized group in technology?

Please share only what you are comfortable sharing. This will help us better serve underrepresented and marginalized groups, better understand how well our outreach efforts are going, and more.

Type: select all that apply (optional)

- No [`NEXT`](#if-you-find-it-difficult-to-participate-in-the-rust-community-and-feel-comfortable-giving-more-details-please-tell-us-what-makes-it-difficult)
- Yes, but I prefer not to say which
- Cultural beliefs
- Disabled or person with disability (including physical, mental, and other)
- Educational background
- Language
- Lesbian, gay, bisexual, queer or otherwise non-heterosexual
- Non-binary gender
- Older or younger than the average developers I know
- Political beliefs
- Racial or ethnic minority
- Religious beliefs
- Trans
- Woman or perceived as a woman
- Other (open response)

### Do you feel your belonging to an underrepresented or marginalized group in technology makes it difficult for you to participate in the Rust community?

Type: select one

- Often
- Sometimes
- Never

### If you find it difficult to participate in the Rust community, and feel comfortable giving more details, please tell us what makes it difficult

Type: free form.

### Are you a full- or part-time student?

Type: select one

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

### Are you employed full- or part-time (including paid internships)?

> Optional

Type: select one

- Yes
- No [`NEXT`](#excluding-rust-what-is-your-experience-with-other-kinds-of-programming-languages)

### Which category best describes your current employer's industry?

Type: select all that apply

- Advertising
- Aerospace
- Automotive
- Business software
- Computer hardware
- Consumer software
- Energy
- Education/Academia
- Entertainment or Media
- Finance
- Gaming
- Government
- Healthcare
- Manufacturing
- Military
- Music
- Retail
- Telecommunications
- Transportation
- Other (open response)

> **justification**
>
> We want to see what industries have what representation in the Rust community.
> While it's impossible to be precise here, we want to get a general idea.
> This list is largely adopted from this [Wikipedia article](https://en.wikipedia.org/wiki/Outline_of_industry).

### Do you write or design software in your work?

Type: select one

- Yes, primarily as an individual contributor (i.e., non-manager).
- I primarily manage others who do.
- No [`NEXT`](#excluding-rust-what-is-your-experience-with-other-kinds-of-programming-languages)

### Which categories best describes the tech domain(s) you currently write or design software in?

Type: select all that apply

- Audio programming
- Blockchain
- Cloud computing applications
- Cloud computing infrastructure or utilities
- Computer graphics
- Data science
- Desktop computer application frontend
- Desktop computer or mobile phone libraries or services
- Distributed systems
- Embedded devices (with operating systems)
- Embedded devices (bare metal)
- HPC (High-performance [Super]Computing)
- IoT (Internet of Things)
- Machine learning
- Mobile phone application frontend
- Computer networking
- Robotics
- Computer security
- Scientific and/or numeric computing
- Server-side or "backend" application
- Simulation
- Web application frontend
- WebAssembly

> **justification**
>
> We want to see generally what tech areas respondents work in. In addition to general categories,
> we include some technology categories that are known to be popular in the Rust community.
> This can help us get more insight into what respondents are working on. For instance, if a respondent
> answers their employer works in automotive but they are working on mobile phone applications and not 
> embedded devices, we might conclude different things than if they are working on embedded devices.

### How long have you worked in software professionally?

Type: select one

- <= 1 year
- 1 - 3 years
- 3 - 5 years
- 5 - 10 years
- 10 - 20 years
- > 20 years

> **justification**
>
> For cohort analysis it is important to understand length of time in the software
> industry as this can have an impact on perceptions.
>
> The ranges of years chosen are a best attempt at capturing different "stages" in a person's professional career.

### Excluding Rust, what is your experience with other kinds of programming languages?

Type: matrix

Languages:

- Assembly language (of any variety)
- Languages with manual memory management (e.g., C, C++, Objective-C without ARC)
- Statically typed object oriented languages with garbage collection (e.g., Java, C#, Go)
- Statically typed functional programming languages (e.g., Haskell, ML)
- Dynamically typed functional programming languages (e.g., Lisp, Clojure, Elixir)
- Statically typed languages with newer expressive type systems (e.g., Swift, Kotlin, Scala)
- Dynamically typed languages (e.g., Javascript, Ruby, Python, PHP, Perl)

Experience:

- I've never used nor am I familiar with any language in this category
- I have a basic familiarity with at least one language in this category
- I am comfortable using at least one language in this category
- I have expertise in at least one language in this category

> **justification**
>
> For cohort analysis it is interesting to know what other language "families"
> respondents are familiar with. It is more illustrative which types of languages
> respondents are familiar with than the specific language.

### How long have you been programming (in any language, for any reason)?

Type: select one

- < 1 year
- < 3 years
- < 5 years
- < 10 year
- > 10 years

### Where do you live?

Type: select one (optional)

- *all UN member states*
- *two observer states (Vatican City and Palestine)*
- Other (open response)

> **justification**
>
> We'd like to get a geographic understanding of where the community is. The form of the question allows us to be fairly precise about this
> though there will still be some challenges (e.g., someone who lives in East Russia has similar timezones to East Asia not West Russia).

### In what ways are you comfortable communicating about technical topics in English?

Type: select all that apply

- I feel comfortable and capable of having a *spoken* technical conversation in English
- I feel comfortable and capable of having a *written* technical conversation in English
- I feel comfortable and capable of reading technical documentation in English
- I feel comfortable and capable of consuming a technical talk (e.g., at a conference or meetup) in English
- I feel comfortable and capable of consuming a written technical educational material (e.g., technical books, blog posts, etc.) in English

> **justification**
>
> We want to understand self reported feeling of comfort and capability of communication
> of English since a large portion of the Rust community is and likely will always be in English.

### What is/are your **preferred** language(s) for the following forms of technical communication?

**IMPORTANT**: The answers should reflect your **preference** and **not** what you are capable of communicating in. For example, if you feel comfortable and capable of consuming technical communication in both English and Korean, but you always prefer Korean, you should *only* answer Korean as that is your preference.

Type: matrix

Forms of communication:

- *spoken* technical conversation
- *written* technical conversation
- technical documentation
- technical talks
- written technical education material

Languages:

- Chinese
- Spanish
- English
- Hindi
- Bengali
- Portuguese
- Russian
- Japanese
- Turkish
- Korean
- French
- German
- Vietnamese
- Urdu
- Other (open response)

> **justification**
>
> We want to understand *preference* of technical communication and how that differs
> from their abilities to consume technical communication in English.
> The languages selected are based on all national languages that are members of
> the top 20 most spoken languages in the world.
