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

### As you have indicated that you're no longer using Rust, what prompted you to participate in this survey?

Type: select all that apply (optional)

- I plan to return to using Rust in the future
- I consider myself part of the Rust community
- Specifically to provide feedback on why I stopped using Rust
- To provide feedback on Rust in general
- Curiosity
- Other (open response)

> **justification**
>
> Useful in understanding why non-users contribute;

> **SURVEY FLOW**
>
> Skip to `## Your opinions about Rust` section

## For non-Rust users

### As you have indicated that you have not used Rust, what prompted you to participate in this survey?

Type: select all that apply (optional)

- I plan to use Rust in the future
- I consider myself part of the Rust community
- Specifically to provide feedback on WHY I do not use Rust
- Curiosity
- Other (open response)

> **justification**
>
> Useful in understanding why non-users contribute to the survey

> **SURVEY FLOW**
>
> Skip to `## Your opinions about Rust` section

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

### How would you rate your Rust expertise?

Type: select one

- I can't read or write Rust
- I can write simple programs in Rust
- I can write useful, production-ready code but it is a struggle
- I am productive writing Rust
- I am an expert

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
- During 2022
- During 2020 or 2021
- During 2018 or 2019
- During 2016 or 2017
- During 2015 or before

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

**Note**: this is specifically about which systems you use for development *not* all the 
systems you target.

Type: select all that apply (optional)

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

### On the primary machine you compile Rust code on, how many CPUs are there?

Please count *logical* CPUs here, not cores or sockets. You can get this number by running the following commands from the command line:

- Linux: `nproc`
- macOS: `sysctl -n hw.ncpu`
- Windows Command Prompt: `echo %NUMBER_OF_PROCESSORS%`
- Windows PowerShell: `(Get-CimInstance Win32_ComputerSystem).NumberOfLogicalProcessors`

Type: free form (number, optional)

> **justification**
>
> Question added by Josh Triplett. The answers can help tune parallel rustc:
>
> - When we encounter a scalability issue that starts at a certain number of CPUs, it'll be good to know what proportion of the Rust community is affected.
> - It'll help when tuning algorithms or build systems whose memory usage may depend on the number of CPUs present.
> - It'll help with prioritization around whether to make something go faster by throwing more CPUs at it or by optimizing on the same number of CPUs.
> - It'll help avoid assumptions that rust developers might otherwise make about how universal the caliber of hardware they have is.

### Which operating systems or runtimes do you develop Rust software for?

**Note**: this is specifically about which operating system or runtime you **target** not which system you use
for development nor which specific architectures (e.g., x86 vs ARM) you target.

Type: select all that apply (optional)

- Linux (desktop or server)
- Windows
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

### Which version(s) of Rust do you use for local development?

Type: select all that apply (optional)

- Current stable version
- Previous stable version
- A specific version of stable Rust equal to or newer than 1.47
- A specific version of stable Rust older than 1.47
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
> We ask specifically about version 1.47 since it is, at the time of the survey, the 
> version that was released ~1 year prior. Additionally, at the time of this writing
> all major Linux distros have a version equal to or newer than this version.

### Which version(s) of Rust do you use in automated testing (e.g., CI)?

Type: select all that apply (optional)

REPEAT

> **justification**
>
> See the previous question.

### If you use nightly, why?

Type: select all that apply (optional)

- I don't use nightly
- Out of habit
- For a particular language feature or set of language features I need
- I like to have access to all the latest features
- To help test the nightly version for bugs
- For testing in CI
- A crate dependency I use requires it
- A tool I use requires it
- Other (open response)

> **justification**
>
> We'd like to know what are the common reasons people use nightly
> so that we can better understand where testers are coming from.

### If you use beta, why?

Type: select all that apply (optional)

- I don't use beta
- Out of habit
- To adopt stabilized language features as early as possible
- To help test the beta version for bugs
- For testing in CI
- Other (open response)

> **justification**
>
> Same justification as the question about nightly but for beta.

### In which ways do you install Rust?

Type: select all that apply (optional)

- Rustup (where Rustup is installed from rust-lang.org or you built it from source)
- Rustup (where Rustup is installed using any package manager)
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

### Which editor or IDE setup do you use with Rust code on a regular basis?

Type: select all that apply (optional)

- VS Code
- vi/vim/neovim
- IntelliJ/CLion/other JetBrains IDE
- Emacs
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

### Which debuggers do you use for debugging Rust programs on a regular basis?

Type: select all that apply (optional)

- GDB
- LLDB
- Visual Studio
- WinDBG
- VS Code (using any debugger extension)
- IntelliJ/CLion/other JetBrains IDE
- RR/Pernosco
- 'println' debugging (or using any logging or tracing crate, etc.)
- Other (open response)

> **justification**
>
> It is good to know how many users use a debugging tool, and which tool they use.
> This information could influence priorities for the compiler and tools teams.
>
> Note that there is some overlap between the answers, e.g., VS Code uses either a
> GDB or LLDB plugin, but I think that is OK, we can take this into account when
> interpreting the answers and we will get an indication of user's perceptions of
> their tools.

### Please indicate how vital to your workflow each of the following tools are when programming with Rust:

Type: matrix (optional)

Tools:

- clippy
- cargo
- rustdoc/cargo doc
- rustup
- play.rust-lang.org
- miri
- rustfmt/cargo fmt
- bindgen

Rating:

- Essential
- Somewhat important
- Not important
- I have no experience with this tool

> **justification**
>
> Understanding how important certain tools are to the community and *more importantly* to 
> certain subsections of the community is important. This can also help us understand how
> popular certain tools are as well as how important lesser used tools are to their users.

### In which of the following ways have you participated in the Rust community in the last 6 months:

Note that the following forms of participation do not include code related activities (i.e., writing, reviewing, or discussing code). Such pariticpation is asked about in later questions.

Type: select all that apply (optional)

- I have produced informational content about Rust (e.g., blogged, live streamed, made a YouTube video, presented at a conference/meetup, etc.)
- On several occasions I have consumed informational content about Rust (e.g., blogs, live streams, YouTube videos, etc.)
- On several occasions I have read comments about Rust content on "news" sites (e.g., Hacker News, reddit.com/r/rust, lobste.rs/t/rust, etc.)
- On several occasions I have commented on Rust content on "news" sites (e.g., Hacker News, reddit.com/r/rust, lobste.rs/t/rust, etc.)
- On several occasions I have read official Rust communication channels (e.g., This Week in Rust, the official Rust blog, the Rust Twitter account, etc.)
- On several occasions I have participated in conversations about Rust on social media (Twitter, Facebook, LinkedIn, etc.)
- I have participated in Rust community forums or chats (e.g., users.rust-lang.org, Rust Discord, a local Rust chat community, etc.)
- I have attended a Rust meetup or conference (virtual or in-person)

> **justification**
>
> We'd like to get a picture of _how_ people participate in the Rust community. In
> particular we can use this information to do cohort analysis on highly "active"
> community members in comparison to less active community members.

### Roughly how often do you contribute to the Rust project?

Type: matrix (optional)

Activities:

- Comment on, contribute to discussion of, or provide edits to an open RFC
- Create a new thread or comment on internals.rust-lang.org
- Discuss the Rust project in an official chat (either Zulip or Discord)
- Open an issue on any repo in the rust-lang GitHub organization
- Contribute code changes (including tests) to the Rust compiler (rust-lang/rust)
- Contribute code changes (including tests) to any other project in the rust-lang GitHub organization
- Contribute non-code changes (documentation, comments, etc.) to any project in the rust-lang GitHub organization

Frequency:
- More frequently than weekly
- Weekly
- Monthly
- Less frequently than monthly
- Never but have tried to
- Never and have never tried to

> **justification**
>
> We want to understand the nature of contribution to the Rust project both
> to better understand the shape of community involvement and for cohort analysis.

### How often have you felt explicitly welcome in the Rust community?

Type: matrix

Activities:

- *Official* Rust community forums or chats (users.rust-lang.org, internals.rust-lang.org, the official Rust Discord, or the Rust Zulip)
- *Unofficial* Rust community forums or chats (e.g., reddit.com/r/rust, Hacker News, the Rust *Community* Discord, etc.)
- Attending a Rust conference
- Attending a Rust meetup or local community event
- Discussion (issues, pull requests, etc.) on a repository *inside* the rust-lang GitHub organization
- Discussion (issues, pull requests, etc.) on a repository *outside* of the rust-lang GitHub organization

Choices:

- I've *often* felt welcome
- I *sometimes* feel welcome
- I *never* feel welcome
- I've never participated in this activity

> **justification**
>
> We'd like to know where people are feeling welcome and the degree to which they are feeling welcome.

### How often have you felt *un*welcome in the Rust community?

Type: matrix (optional)

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
> We'd like to know where people are feeling unwelcome and the degree to which they are feeling unwelcome. This can 
> help us better understand the free from responses that will come in the next question.

### If you indicated that you did not feel welcome in the Rust community, are there any details about your experience that you would like to share with us?

Type: free form (optional)

> **justification**
> 
> More detail on the type of situations where people have felt unwelcome can let us better 
> address these issues in the future.

### Which of the following activities do you find helpful or effective for learning Rust or improving your Rust skills?

Type: matrix (optional)

Activities:

- Reading books or other written material geared towards learning Rust
- Watching videos, streams, etc. geared towards learning Rust
- Attending an organized training session or course (in person or virtual)
- Doing Rust coding exercises or challenges created to help learn Rust
- Building a non-trivial project in Rust or contributing to an open source project

Choices:

- Very helpful
- Somewhat helpful
- Not helpful
- I have no experience with this activity

> **justification**
>
> We'd like to confirm what learning materials are popular with the community. This
> combined with some cohort analysis can tell us about how particular subsections
> of the community prefer to learn.

## Rust at work

### To what extent is Rust currently being used by your company?

Type: select one

- My company uses Rust for a large portion of production projects
- My company uses Rust for a small portion of production projects
- My company uses Rust only for non-production projects (e.g., tooling)
- My company has actively experimented with Rust
- My company has seriously considered, but not experimented with, using Rust
- My company has not seriously considered Rust for any use
- I am unsure whether my company has considered using or currently uses Rust
- I don't work for a company or my company does not develop software of any kind [`NEXT`](#rust-in-education)

> **justification**
>
> We want to establish how reliant companies are on Rust.

### Approximately how many total developers does your company employ?

**Note**: don't worry about being exact here! Go with you gut.

Type: select one (optional)

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

Type: select one (optional)

- Yes
- No
- I don't know

> This question assess hiring sentiment. Although there is intrinsic uncertainty, it is easy to answer and forward looking.
> It will also be interesting to see what the demand for Rust skills from companies is over time.

### In what technology domain(s) is Rust used at your company?

If you've previously answered that your company is not actively using Rust, you can leave this question blank.

Type: select all that apply (optional)

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
- Programming languages and related tools (including compilers, IDEs, standard libraries, etc.)
- Robotics
- Computer security
- Scientific and/or numeric computing
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

### Are you using Rust at work?

Type: select one

- Yes, for the majority of my coding
- Yes, it's one of a number of languages I use and I use it regularly
- Yes, but I only use it occasionally
- No [`NEXT`](#rust-in-education)

> **justification**
>
> We want to establish what percentage of those who could possibly use Rust in a professional setting
> are using Rust in a professional setting. This is most interesting over time.
> Answers to this question should be combined with whether the respondent has ever used Rust.


### Rate how much the following statements are reasons why your team uses Rust at work

Type: matrix (optional)

Statements:

- For its performance (i.e., speed, memory footprint, etc.) characteristics
- We need precise control over exactly how our software runs
- Its security and safety properties are important to us
- It allows us to build relatively correct and bug free software
- We find it enjoyable or fun to program in Rust
- We already know Rust so it's our default choice
- We find it easy to prototype with
- We must interact with existing Rust code

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

### Are there any additional reasons why your team uses Rust at work?

Type: free form (optional)

> **justification**
>
> Follow up to the question before to gain more insights.

### Please rate your agreement with the following statements regarding your team's experience using Rust at work.

Type: matrix (optional)

Statements:

- Using Rust has helped us achieve our goals
- Adopting Rust has been challenging
- Overall, adopting Rust has slowed down our team
- Using Rust has been worth the cost of adoption
- We're likely to use Rust again in the future

Rating:

- Agree
- Neither agree nor disagree
- Disagree

> **justification**
>
> Future potential adopters may want to know how often other's have encountered success.

### What about your usage of Rust has been challenging?

Type: free form (optional)

> **justification**
>
> This an opportunity to learn from adopters at companies what they struggle with when adopting Rust.

## Rust in Education

### Are you currently, or have you in the last year, taken a course or training which uses or teaches Rust?

Type: select one

- Yes
- No [`NEXT`](#your-opinions-about-rust)

> **justification**
>
> This question is primarily used to funnel respondents into the more specific questions about the kinds of educational activities they've been a part of.

### Where is/was the course or activity taught?

Type: select one (optional)

- University or other tertiary institute
- High school or secondary school
- A course through an online "continuing education" provider (e.g., Udemy, Coursera, edX, LinkedIn Learning, etc.)
- A bootcamp or other vocational-focused educational institute
- A short training course offered through your employer or contracted by your employer

> **justification**
>
> We want to know where Rust is being taught.

### Which best describes your course or activity?

Type: select one (optional)

- A course teaching exclusively how to program in Rust
- A course teaching how to program in Rust and other languages
- A computer science course (e.g., operating systems, algorithms, etc.) course which uses Rust (and potentially other languages)
- Other type of course where Rust was used

> **justification**
>
> We want to know how Rust is being taught.

### Is/was Rust mandated for your course or activity, or did you choose it yourself?

Type: select one (optional)

- Rust was mandated
- I chose to use Rust

> **justification**
>
> Together with the above question, we want to know how Rust is being taught.

## Your opinions about Rust

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
- Project governance does not scale to match the size/requirements of the community
- Developers/maintainers of the language are not properly supported
- I'm not worried
- Other (open response)

> **justification**
>
> Would be useful for leadership to understand the community's fears.

### Please rate your agreement with the following statements about Rust.

Type: matrix (optional)

Statements:

- Rust provides a real benefit over other programming languages
- Rust is significantly more complicated to program in than other programming languages
- Rust requires significantly more effort to learn than other programming languages
- Rust code tends to contain significantly fewer bugs than equivalent code written in another programming language would have
- Rust is risky to use in production
- Rust makes me more productive
- Rust is fun to use

Rating:

- Agree
- Neither agree nor disagree
- Disagree

> **justification**
>
> There are several "truisms" about Rust that we'd like to get perspective on how true these are for users of Rust.
>
> Note that answers here can be subject to survivorship bias and so extra care should be taken with interpreting results.

### In your opinion, how do you find the following aspects of Rust?

Type: matrix (optional)

Aspects:

- Compile times
- Binary size
- Memory usage (i.e., how much RAM rustc uses when compiling)
- Disk space usage (e.g., the size of target folder)
- Bugs in the compiler (i.e., ICEs a.k.a. internal compiler errors, miscompilations, etc.)
- Compiler error messages
- IDE experience
- Debugging experience
- Available tools and support
- Async programming
- GUI development
- Rust language and standard library documentation

Options:

- Great
- Good enough
- Could be better
- Seriously lacking
- Unsure

> **justification**
>
> This question gathers data on the communities perceptions of certain aspects of Rust at this point in time.

### In your opinion, have the following aspects of Rust gotten better or worse over the past year?

Type: matrix (optional)

Aspects:

REPEAT

Options:

- Much better
- Better  
- Remained the same  
- Worse
- Much worse
- Unsure

> **justification**
>
> This question gathers data on the communities perceptions of certain aspects of Rust over the last year.

### Do you agree with the following statements on Rust stability?

Type: matrix (optional)

Statements:

- I can upgrade the *stable* compiler version without fear of my code failing to compile
- I can upgrade the *nightly* compiler version without fear of my code failing to compile
- I can upgrade the *stable* compiler version without fear of my code taking longer to compile
- I can upgrade the *nightly* compiler version without fear of my code taking longer to compile
- Upgrading to a new *stable* compiler version requires either no changes or extremely small & easy changes to my code
- Upgrading to a new *nightly* compiler version requires either no changes or extremely small & easy changes to my code

Rating:

- Agree
- Neither agree nor disagree
- Disagree

> **justification**
>
> When want to get an impression of how stable the compiler *feels*. Impressions are more important than hard numbers as
> not all users define stability in the same way the compiler does. For example, experiencing compiler performance regressions
> in a new version of the compiler isn't breaking official stability guarantees but it can feel just as painful as an
> actual breaking change.

### Do you agree with the following statements on Rust employment?

Type: matrix (optional)

Statements:

- It is easy for qualified applicants to find jobs which use Rust for the majority of programming
- Existing Rust jobs are attractive
- Learning Rust provides me with skills that employers seek
- I feel qualified to apply for at least some advertised Rust jobs

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
- No [`NEXT`](#are-you-a-full--or-part-time-student)
- I prefer not to say [`NEXT`](#are-you-a-full--or-part-time-student)

### Which of the following underrepresented or marginalized groups in technology do you consider yourself a part of?

Please share only what you are comfortable sharing. This will help us better serve underrepresented and marginalized groups, better understand how well our outreach efforts are going, and more.

Type: select all that apply (optional)

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

Type: select one (optional)

- Often
- Sometimes
- Never

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

Type: select one

- Yes
- No [`NEXT`](#excluding-rust-what-is-your-experience-with-other-kinds-of-programming-languages)

### Do you write or design software in your work?

Type: select one

- Yes, primarily as an individual contributor (i.e., non-manager)
- I primarily manage others who do
- No [`NEXT`](#excluding-rust-what-is-your-experience-with-other-kinds-of-programming-languages)

### How long have you worked in software professionally?

Type: select one (optional)

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

### Which category best describes your current employer's industry?

Type: select all that apply (optional)

- Advertising
- Aerospace
- Automotive
- Business software
- Consumer software
- Consulting
- Computer hardware
- Defense
- Energy
- Education/Academia
- Entertainment or Media
- Finance
- Gaming
- Government
- Healthcare
- Manufacturing
- Music
- Railway
- Research & Development
- Retail
- Telecommunications
- Transportation
- I'm not employed
- Other (open response)

> **justification**
>
> We want to see what industries have what representation in the Rust community.
> While it's impossible to be precise here, we want to get a general idea.
> This list is largely adopted from this [Wikipedia article](https://en.wikipedia.org/wiki/Outline_of_industry).

### Which categories best describes the tech domain(s) you currently write or design software in?

Type: select all that apply (optional)

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
- Programming languages and related tools (including compilers, IDEs, standard libraries, etc.)
- Robotics
- Computer security
- Scientific and/or numeric computing
- Server-side or "backend" application
- Simulation
- Web application frontend
- WebAssembly
- Other (open response)

> **justification**
>
> We want to see generally what tech areas respondents work in. In addition to general categories,
> we include some technology categories that are known to be popular in the Rust community.
> This can help us get more insight into what respondents are working on. For instance, if a respondent
> answers their employer works in automotive but they are working on mobile phone applications and not 
> embedded devices, we might conclude different things than if they are working on embedded devices.

### Excluding Rust, what is your experience with other kinds of programming languages?

Type: matrix (optional)

Languages:

- Assembly language (of any variety)
- Languages with manual memory management (e.g., C, C++, Objective-C without ARC)
- Statically typed object oriented languages with garbage collection (e.g., Java, C#, Go)
- Statically typed functional programming languages (e.g., Haskell, ML)
- Dynamically typed functional programming languages (e.g., Lisp, Clojure, Elixir)
- Statically typed languages with newer expressive type systems (e.g., Swift, Kotlin, Scala)
- Dynamically typed languages (e.g., JavaScript, Ruby, Python, PHP, Perl)

Experience:

- I've never used nor am I familiar with any language in this category
- I have a basic familiarity with at least one language in this category
- I am comfortable using at least one language in this category
- I am an expert in at least one language in this category

> **justification**
>
> For cohort analysis it is interesting to know what other language "families"
> respondents are familiar with. It is more illustrative which types of languages
> respondents are familiar with than the specific language.

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
> We'd like to get a geographic understanding of where the community is. The form of the question allows us to be fairly precise about this
> though there will still be some challenges (e.g., someone who lives in East Russia has similar timezones to East Asia not West Russia).

### As you selected "Other" from the list of countries above, please enter your territory of residence below:

Type: free form (optional)

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

## Anything else?

### Is there anything else you'd like to tell us?

Type: free form (optional)

> **justification**
>
> While it's unlikely we'll receive any one piece of feedback from this question that will prove to be super useful, 
> having it in the survey can still be useful. It can help us decide on new questions or perspectives that we want to
> try to capture in future surveys. It also gives respondents a place to give thanks or share a particular opinion they
> hold which can be useful in and of itself.
