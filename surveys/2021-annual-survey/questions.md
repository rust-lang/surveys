# Опрос

Вне зависимости от того, используете ли вы язык программирования Rust <https://rust-lang.org>, мы хотим услышать вас!

Команда сообщества Rust создало этот опрос для оценки того, как идут дела в целом, что можно улучшить и каким наилучшим образом мы можем взаимодействовать вместе по мере развития.

Это ваш шанс, чтобы высказаться о приоритетах развитя Rust.

До тех пор, пока вы не указали ваш адрес элекронной почты, ваши ответы будут анонимны. Любые персональные данные, отправленные в рамках данного опроса, будут обработаны в соответствии с нашей политикой, которая описана в Часто Задаваемых Вопросах. 

https://github.com/rust-community/team/wiki/State-of-the-Rust-Language-Community-Survey-FAQ

Мы предполагаем, что опрос займёт примерно 10-25.

## Использование Rust

### Используете ли вы Rust?

Type: select one

- Да, я использую Rust (для различных целей, включая его изучение) [`NEXT`](#your-rust-experience)
- Нет, я не использую Rust на текущий момент, но использовал ранее [`NEXT`](#for-previous-rust-users)
- Нет, я ни разу не использовал Rust [`NEXT`](#for-non-rust-users)

> **justification**
>
> Fundamental for cohort analysis

## Для использовавших ранее Rust пользователей

### Так как вы указали, что более не используете Rust, что побудило вас на участие в опросе?

Type: select all that apply (optional)

- Я планирую снова использовать Rust в будущем.
- Я считаю себя частью сообщества Rust.
- Специально, чтобы высказать причину, по которой перестал использовать Rust.
- Чтобы оставить отзыв о Rust в целом.
- Любопытство.
- Другое (свободный ответ)

> **justification**
>
> Useful in understanding why non-users contribute;

> **SURVEY FLOW**
>
> Skip to `## Your opinions about Rust` section

## Для неиспользующих Rust

### Так как вы указали, что вы ни разу не использовали Rust, что побудило вас на участие в опросе?

Type: select all that apply (optional)

- Я планирую использовать Rust в будущем.
- Я считаю себя частью сообщества Rust.
- Специально, чтобы высказать причину, по которой не использую Rust.
- Любопытство.
- Другое (свободный ответ)

> **justification**
>
> Useful in understanding why non-users contribute to the survey

> **SURVEY FLOW**
>
> Skip to `## Your opinions about Rust` section

## Ваш опыт использования Rust

### В среднем, как часто вы используете Rust?

Type: select one

- Ежедневно или близко к этому
- Еженедельно или близко к этому
- Ежемесячно или близко к этому
- Редко

> **justification**
>
> This can be useful demographic information as a proxy for how "important" Rust is
> in someone's technical life.
>
> We deliberately use calendar time for this question to gauge how "serious" the
> programmer's use of Rust is. This does mean that we will group together, for example,
> those who program once a week but always in Rust and those who program daily but
> use Rust once a week.

### Как бы вы оценили своё знание Rust?

Type: select one

- Я не могу писать или читать код на Rust
- Я могу писать простые приложения на Rust
- Я могу писать полезный, готовый к работе код, но испытываю трудности
- Я успешно пишу на Rust
- Я эксперт

> **justification**
>
> Useful for cohort analysis, i.e., for other questions we can query if answers are significantly different for beginners vs advanced users.
>
> Previously this question was a 1-10 ranking. Having specific labels can help with consistency across responses. Additionally, having 10 choices
> was too specific (i.e., what's the difference between a 7 and 8?) where as with the new answers, we have a better idea of what the differences 
> between answers actually mean.

### When did you learn to program in Rust?
### Когда вы начали учиться программировать на Rust?

**Примечание**: в то время, как вы можете продолжать улучшать свои навыки владения Rust, ответ на этот вопрос предполагает под "учёбой разработки на Rust"
понимается трата *большей части* вашего времени на Rust, используя учебные материалы или программируя *в целях учёбы* (в отличие от достижения какой-либо
другой цели). Елси ваш процесс учёбы распространяется на несколько указанных промежутов, укажите тот, во время которого вы усвоили *больше всего*.

Type: select one (optional)

- Я всё ещё *активно* пытаюсь учить Rust
- В 2021
- В 2019 или 2020
- В 2017 или 2018
- В 2015 или 2016
- В 2014 или ранее

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

### Какую операционную систему вы регулярно используете для *разработки* на Rust?

Примечание: этот вопрос о том, какую операционную систему вы используете для разработки,
а не те, на которых предполагается использование приложений.

Type: select all that apply (optional)

- Linux
- Windows
- Windows Subsystem for Linux
- Mac OS
- Другое (свободный ответ)

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

Пожалуйста, укажите количество *логических* ядер процессора вместо физических или сокетов. Вы моежете получить это число, выполнив одну из приведённых ниже команд в командной строке:

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

### Для каких операционных систем или сред вы разрабатываете программное обеспечение на Rust?

Note: this is specifically about which operating system or runtime you **target** not which system you use
for development nor which specific architectures (e.g., x86 vs ARM) you target.

Type: select all that apply (optional)

- Linux (настольный или серверный)
- Windows
- Mac OS
- iOS
- Android
- Embedded platforms (с операционной системой)
- Embedded platforms (без операционной системы)
- WebAssembly
- Без явной зависимости к какой-либо платформе (например, не использующая функции операционной системы библиотека)
- Другое (свободный ответ)

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

- Текущая стабильная версия
- Предыдущая стаблиьная версия
- Стабильная верся Rust 1.47 или новее
- Стабильная версия Rust старше 1.47
- Бета версия
- Последняя ночная версия
- Определённая ночная версия
- Пользовательская версия
- Я не знаю
- Другое (свободный ответ)

> **justification**
>
> Together with the following question, we can better determine what the spread of 
> version usage is across the community.
> We ask specifically about version 1.47 since it is, at the time of the survey, the 
> version that was released ~1 year prior. Additionally, at the time of this writing
> all major Linux distros have a version equal to or newer than this version.

### Какие версии Rust вы используете для автоматизированного тестирования (например, CI)?

Type: select all that apply (optional)

REPEAT

> **justification**
>
> See the previous question.

### Если используете ночную версию, почему?

Type: select all that apply (optional)

- Я не использую ночную версию
- Привычка
- Для какой-то определённой или ряда используемых возможнойстей языка
- Мне нравится иметь доступ ко всем последним новшествам
- Для помощи в нахождении ошибок в ночной версии
- Для тестирования в CI
- Используемый мной пакет требует этого
- Используемый мной инструмент требует этого
- Другое (свободный ответ)

> **justification**
>
> We'd like to know what are the common reasons people use nightly
> so that we can better understand where testers are coming from.

### Если вы используете бета версию, почему?

Type: select all that apply (optional)

- Я не использую бета версию
- Привычка
- Для помощи в стабилизации возможностей языка как можно раньше
- Для помощи в нахождении ошибок в бета версии
- Для тестирования в CI
- Другое (свободный ответ)

> **justification**
>
> Same justification as the question about nightly but for beta.

### Каким образом вы устанавливаете Rust?

Type: select all that apply (optional)

- Rustup (where Rustup is installed from rust-lang.org or you built it from source)
- Rustup (where Rustup is installed using any package manager)
- Linux distribution package
- Homebrew
- Official rust-lang.org tarballs
- Official Windows .msi installers
- Official macOS .pkg installers
- Из исходного кода
- Другое (свободный ответ)

> **justification**
>
> Since many of these sources are not under project control, it can be hard to know where
> people are getting their Rust compiler from.

### Какой редактор или IDE вы регулярно используете для работы с кодом на Rust?

Type: select all that apply (optional)

- VS Code
- vi/vim/neovim
- IntelliJ/CLion/иная Jet Brains IDE
- Emacs
- Sublime Text
- Visual Studio
- Xcode
- Atom
- Другое (свободный ответ)

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

### Какими отладчиками вы регулярно пользуетесь при отладке Rust приложений?

Type: select all that apply (optional)

- GDB
- LLDB
- Visual Studio
- WinDBG
- VS Code (с любым расширением для отладки)
- IntelliJ/CLion/other Jet Brains IDE
- RR/Pernosco
- 'println' отладка (или иное с использованием любого пакета логирования или трассировки)
- Другое (свободный ответ)

> **justification**
>
> It is good to know how many users use a debugging tool, and which tool they use.
> This information could influence priorities for the compiler and tools teams.
>
> Note that there is some overlap between the answers, e.g., VS Code uses either a
> GDB or LLDB plugin, but I think that is OK, we can take this into account when
> interpreting the answers and we will get an indication of user's perceptions of
> their tools.

### Пожалуйста, укажите, насколько важен каждый из следующих инструментов при программировании на Rust для вашего рабочего процесса: 

Type: matrix (optional)

Инструменты:

- clippy
- cargo
- rustdoc/cargo doc
- rustup
- play.rust-lang.org
- miri
- rustfmt/cargo fmt
- bindgen

Значимость:

- Основной
- Важен в некоторой степени
- Не важен
- Нет опыта работы с этим инструментом

> **justification**
>
> Understanding how important certain tools are to the community and *more importantly* to 
> certain subsections of the community is important. This can also help us understand how
> popular certain tools are as well as how important lesser used tools are to their users.

### Каким из перечисленных способов вы принимали участие в сообществе Rust за последние 6 месяцев:

Обратите внимание, что перечисленные ниже пункты не включают деятельность, связанную с кодом (например, написание, рецензирование или обсуждение кода). Вопросы по активности, связанной с кодом, будут далее.

Type: select all that apply (optional)

- Создавал информационный контент о Rust (например, блоги, прямые трансляции, видео на YouTube, презентации на конференциях/встречах, и так далее)
- Иногда использовал информационный контент о Rust (например, блоги, прямые трансляции, видео на YouTube, презентации на конференциях/встречах, и так далее)
- Иногда *читал* комментарии о Rust на "новостных" сайтах (e.g., Hacker News, reddit.com/r/rust, lobste.rs/t/rust, и так далее)
- Иногда *комментировал* о Rust на "новостных" сайтах (e.g., Hacker News, reddit.com/r/rust, lobste.rs/t/rust, и так далее)
- Иногда читал официальные каналы Rust (e.g., This Week in Rust, официальный блог Rust, аккуант Rust в Twitter, и так далее)
- Иногда участвовал в обсуждениях на тему Rust в социальных сетях (Twitter, Facebook, LinkedIn, и так далее)
- Участвовал на форумах сообщества Rust или чатах (например, users.rust-lang.org, Rust Discord, локальный чат Rust сообщества, и так далее)
- Посещал встресу или конференцию, посвящённую Rust (виртуально или лично)

> **justification**
>
> We'd like to get a picture of _how_ people participate in the Rust community. In
> particular we can use this information to do cohort analysis on highly "active"
> community members in comparison to less active community members.

### Примерно как часто вы участвуете в проекте Rust?

Активности:

- Комментирование, участие в обсуждениях или внесение правок в открыте RFC
- Создание новых тем или комментирование на internals.rust-lang.org
- Обсуждение проекта Rust в официальном чате (на Zulip или Discord)
- Открытие вопросов в любом из репозиториев организации rust-lang на GitHub
- Внесение изменений в код (включая тесты) компилятора Rust (rust-lang/rust)
- Внесение изменений в код (включая тесты) любого из проектов внутри организации rust-lang на GitHub
- Внесение не связанных с кодом изменений (документирование, коментирование, прочее) в любой проект внутри организации rust-lang на GitHub

Type: select one (optional)

- Чаще одного раза в неделю
- Еженедельно
- Ежемесячно
- Реже раза в месяц
- Никогда не участвовал, но пытался
- Никогда не участвовал и не пытался

> **justification**
>
> We want to understand the nature of contribution to the Rust project both
> to better understand the shape of community involvement and for cohort analysis.

### Как часто вы чувствовали приветливое отношение к себе в сообществе Rust?

Type: matrix

Вид деятельности:

- *Официальные* форумы и чаты сообщества Rust (users.rust-lang.org, internals.rust-lang.org, официальный сервер Rust Discord или Rust Zulip)
- *Неофициальные* форумы и чаты сообщества Rust (e.g., reddit.com/r/rust, Hacker News, Rust *Community* Discord, прочее)
- Участие в конференции, посвящённой Rust
- Участие на встрече или локальном событии, посвящённом Rust
- Обсуждение (проблема, пул реквест, прочее) в репозитории *внутри* rust-lang организации на GitHub
- Обсуждение (проблема, пул реквест, прочее) в репозитории *вне* rust-lang организации на GitHub

Варианты:

- *Часто* испытывал приветливое отношение
- *Иногда* испытывал приветливое отношение
- *Никогда* не испытывал приветливого отношения
- Никогда не участвовал в данной деятельности

> **justification**
>
> We'd like to know where people are feeling welcome and the degree to which they are feeling welcome.

### Как часто вы чувствовали *не*приветливое отношение к себе в сообществе Rust?

Type: matrix (optional)

Вид деятельности:

- *Официальные* форумы и чаты сообщества Rust (users.rust-lang.org, internals.rust-lang.org, официальный сервер Rust Discord или Rust Zulip)
- *Неофициальные* форумы и чаты сообщества Rust (e.g., reddit.com/r/rust, Hacker News, Rust *Community* Discord, прочее)
- Участие в конференции, посвящённой Rust
- Участие на встрече или локальном событии, посвящённом Rust
- Обсуждение (проблема, пул реквест, прочее) в репозитории *внутри* rust-lang организации на GitHub
- Обсуждение (проблема, пул реквест, прочее) в репозитории *вне* rust-lang организации на GitHub

Варианты:

- *Часто* испытывал неприветливое отношение
- *Иногда* испытывал неприветливое отношение
- *Никогда* не испытывал неприветливого отношения
- Никогда не участвовал в данной деятельности

> **justification**
>
> We'd like to know where people are feeling unwelcome and the degree to which they are feeling unwelcome. This can 
> help us better understand the free from responses that will come in the next question.

### Если вы указали, что не чувствуете приветливого отношения в сообществе Rust, можете ли вы поделиться подробностями?

Type: free form (optional)

> **justification**
> 
> More detail on the type of situations where people have felt unwelcome can let us better 
> address these issues in the future.

### Какие из перечисленных ниже видов деятельсности вы считаете наиболее эффективными при изучении или улучшении навыков владения Rust?

Type: matrix (optional)

Виды деятельности:

- Чтение книг или других письменных материалов, направленных на изучение Rust
- Просмотр видео, трансляций или прочего, направленных на изучение Rust
- Участие на тренинге или курсе (лично или виртульно)
- Выполнение упражнений по программированию на Rust или задач, созданных для изучения Rust
- Создание нетривиальных проектов на Rust или участие в проекте с открытым исходным кодом

Варианты:

- Очень эффективный
- В некоторой степени эфеективный
- Неэффективный
- Не занимался данным видом деятельности

> **justification**
>
> We'd like to confirm what learning materials are popular with the community. This
> combined with some cohort analysis can tell us about how particular subsections
> of the community prefer to learn.

## Rust на работе

### В какой степени Rust используется в вашей компании?

Type: select one

- My company uses Rust for a large portion of production projects.
- My company uses Rust for a small portion of production projects.
- My company uses Rust only for non-production projects (e.g., tooling).
- My company has actively experimented with Rust
- My company has seriously considered, but not experimented with, using Rust.
- My company has not seriously considered Rust for any use.
- I am unsure whether my company has considered using or currently uses Rust.
- I don't work for a company or my company does not develop software of any kind. [`NEXT`](#rust-in-education)

> **justification**
>
> We want to establish how reliant companies are on Rust.

### Cколько примерно разработчиков в вашей компании?

Примечание: не беспокойтесь о том, чтобы быть точным здесь! Следуйте интуиции.

Type: select one (optional)

- Менее 10
- 11-49
- 50-99
- 100-500
- 500-1,000
- 1,000-10,000
- Более 10,000

> This question is not that interesting on its own, but it can be used as a sort of co-hort for understanding how answers 
> change depending on the size of the development effort at a company.
>
> Previously this question used "employees" instead of "developers". It is more appropriate for us to ask about the amount
> of developers at a company vs. the amount of people employed in total.

### Планирует ли ваша компания нанимать Rust разработчиков в следующем году?

Type: select one (optional)

- Да
- Нет
- Я не знаю

> This question assess hiring sentiment. Although there is intrinsic uncertainty, it is easy to answer and forward looking.
> It will also be interesting to see what the demand for Rust skills from companies is over time.

### В каких технологий областях Rust используется в вашей компании?

Если вы ранее ответили, что ваша компания не испольует активно Rust, вы можете не отвечать на данный вопрос.

Type: select all that apply (optional)

- Аудио программирование
- Блокчейн
- Приложения для облачных вычислений
- Инфраструктура облачных вычисление или утилиты
- Компьютерная графика
- Наука о данных
- Интерфейс приложений для настольных компьютеров
- Сервисы и библиотеки для мобильных или настольных приложений
- Распределённые системы
- Встроенные устройства (с операционной системой)
- Встроенные устройства (без операционной системы)
- HPC (Высокопроизводительные вычисления)
- IoT (Интернет вещей)
- Машинное обучение
- Интерфейс мобильных приложений
- Компьютеная сеть
- Языки программирования и относящиеся к ним инструменты (включая компляторы, IDE, стандартные библиотеки, прочее)
- Робототехника
- Компьютерная безопасность
- Научные и/или числовые вычисления
- Серверные или "бэкенд" приложения
- Симуляция
- Фронтенд веб-приложения
- WebAssembly
- Другое (свободный ответ)

> **justification**
>
> We want to known roughly what technology stacks are being most often used.
>
> This can be ambiguous and hard to answer. For example, if you're building an operating
> system for a mobile phone, is that embedded, mobile, or something else?
> We want to understand the "shape" of Rust usage, and this question tries to get at that
> by allowing the respondent to select multiple answers.

### Используете ли вы Rust на работе?

Type: select one

- Да, в большинстве случаев
- Да, это один из языков программирования, который я регулярно использую
- Да, но использую изредка
- Нет [`NEXT`](#rust-in-education)

> **justification**
>
> We want to establish what percentage of those who could possibly use Rust in a professional setting
> are using Rust in a professional setting. This is most interesting over time.
> Answers to this question should be combined with whether the respondent has ever used Rust.

### Оцените, в какой мере следующие утверждения являются причинами, по которым ваша команда использует Rust на работе.

Type: matrix (optional)

Утверждения:

- Из-за его производительности (например, скорость, используемая память, прочее).
- Нам нужен *полный контроль* над тем, как работает наше программное обеспечение.
- Нам важна его безопасность.
- Он позволяет нам создавать относительно правильное и свободное от ошибок программное обеспечение.
- Нам нравится программировать на Rust.
- Мы уже знаем Rust, так что это наш выбор по умолчанию.
- Мы находим его простым для протипирования.
- Мы должны взаимодействовать с уже существующим кодом на Rust.
- Другое (свободный ответ)

Оценка:

- Полностью согласен
- Согласен
- Ни согласен и ни не согласен
- Не согласен
- Категорическ не согласен

> **justification**
>
> The Rust community and potential adopters of Rust have a lot of assumptions of why one would choose Rust for a project.
> This question can help confirm or challenge our assumptions and see how they change over time.

### Please rate your agreement with the following statements regarding your team's experience using Rust at work.

Type: matrix (optional)

Утверждения:

- Использование Rust помогло нам достичь наших целей
- Переход на Rust был сложным
- В целом переход на Rust замедлил нашу команду
- Переход на Rust был оправдан
- Мы скорее всего продолжим использовать Rust в будущем

Оценка:

- Согласен
- Ни согласен и ни не согласен
- Не согласен

> **justification**
>
> Future potential adopters may want to know how often other's have encountered success.

### Что является сложным при использовании Rust?

Type: free form (optional)

> **justification**
>
> This an opportunity to learn from adopters at companies what they struggle with when adopting Rust.

## Rust в образовании

### Проходили ли вы в прошлом году или проходите сейчас курс или тренинг, в котором используется или преподается Rust?

Type: select one

- Да
- Нет [`NEXT`](#your-opinions-about-rust)

> **justification**
>
> This question is primarily used to funnel respondents into the more specific questions about the kinds of educational activities they've been a part of.

### Где проходил/проходит курс или учебное мероприятие?

Type: select one (optional)

- Университет или другое высшее учебное заведение
- Средние или старшие классы школы
- Курс от *онлайн* провайдера "непрерываного образования" (напимер, Udemy, Coursera, edX, LinkedIn Learning, прочее)
- Учебный лагерь или другое профессионально-техническое учебное заведение
- Краткий учебный курс, организованный вашим работодателем лично или по найму

> **justification**
>
> We want to know where Rust is being taught.

### Что лучше всего описывает ваш курс или учебную деятельность?

Type: select one (optional)

- Курс обучает только программированию на Rust
- Курс обучает программированию на Rust и других языках
- Курс информатики (например, операционные системы, алгоритмы, прочее), который включает использование Rust (и возможно других языков программирования)
- Другие виды обучения, где используется Rust

> **justification**
>
> We want to know how Rust is being taught.

### Являлся ли Rust обязательным в рамках вашего обучения или вы его выбрали самостояетльно?

Type: select one (optional)

- Rust является обязательным
- Я выбрал Rust

> **justification**
>
> Together with the above question, we want to know how Rust is being taught.

## Ваше мнение о Rust

### Что вас больше всего беспокоит в будущем Rust?

Type: select all that apply (optional)

- Недостаточно использование в индустрии
- Слишком большой интерес со стороны крупных компаний
- Недостаточное количество открытого исходного кода в экосистему
- Не имеет конкретной возможности, которая мне нужна
- Rust не развивается достаточно быстро
- Нестабильность языка
- Замена альтернативой
- Становится слишком сложным
- Инструменты и документация не являются достаточно доступными (например, из-за использованного языка или несовместимости с программами чтения вслух)
- Руководство проекта не масштабируется в соответствии с размером/требованиями сообщества
- Разработчики языка не имеют поддержки в достаточной степени
- Другое (свободный ответ)
- Я не обеспокоен

> **justification**
>
> Would be useful for leadership to understand the community's fears.

### Пожалуйста, оцените степень вашего согласия со слледующими утверждениями о Rust.

Type: matrix (optional)

Утверждения:

- Rust provides a real benefit over other programming languages
- Rust is significantly more complicated to program in than other programming languages
- Rust requires significantly more effort to learn than other programming languages
- Rust code tends to contain significantly *fewer* bugs than equivalent code written in another programming language would have.
- Rust is risky to use in production
- Rust makes me more productive
- Rust is fun to use

Оценка:

- Согласен
- Ни согласен и ни не согласен
- Не согласен

> **justification**
>
> There are several "truisms" about Rust that we'd like to get perspective on how true these are for users of Rust.
>
> Note that answers here can be subject to survivorship bias and so extra care should be taken with interpreting results.

### In your opinion, how do you find the following aspects of Rust?

Type: matrix (optional)

Аспекты:

- Время компиляции
- Размер приложения
- Использование (то есть, сколько оперативной памяти rustc использует во время компиляции)
- Использование дискового пространства (например, размер директории `target`)
- Ошибки копилятора (то есть, ICE или внутренние ошибки компилятора, неправильная компиляция, прочеее)
- Сообщение об ошибках компиляции
- Удобство использование IDE
- Удобство отладки
- Имеющиеся интсрументы
- Асинхронное программирование
- Разработка графического интерфейса
- Документация языка Rust и стандартной библиотеки

Варианты ответа:

- Хорошо
- Достаточно хорошо
- Может быть лучше
- Очень не хватает
- Не уверен

> **justification**
>
> This question gathers data on the communities perceptions of certain aspects of Rust at this point in time.

### По вашему мнению, стали ли следующие аспекты Rust лучше или хуже за прошедгий год?

Type: matrix (optional)

Аспекты:

REPEAT

Варианты ответа:

- Намного лучше
- Лучше  
- Без изменений  
- Хуже
- Намного хуже
- Не уверен

> **justification**
>
> This question gathers data on the communities perceptions of certain aspects of Rust over the last year.

### Согласны ли вы сос следующими утверждениями о стабильности Rust?

Type: matrix (optional)

Утверждения:

- Я могу обновить *стабильную* версию компилятора, не опасаясь, что мой код перестанет компилироваться
- Я могу обновить *ночную* версию компилятора, не опасаясь, что мой код перестанет компилироваться
- Я могу обновить *стабильную* версию компилятора, не опасаясь, что мой код будет дольше компилироваться
- I can upgrade the *ночную* версию компилятора, не опасаясь, что мой код будет дольше компилироваться
- Обновление на новую *стабильную* стабильную версию компилятора не трубует изменений или требует маленьких и простых изменений моего кода
- Upgrading to a new *ночную* стабильную версию компилятора не трубует изменений или требует маленьких и простых изменений моего кода

Оценка:

- Согласен
- Ни согласен и ни не согласен
- Не согласен

> **justification**
>
> When want to get an impression of how stable the compiler *feels*. Impressions are more important than hard numbers as
> not all users define stability in the same way the compiler does. For example, experiencing compiler performance regressions
> in a new version of the compiler isn't breaking official stability guarantees but it can feel just as painful as an
> actual breaking change.

### Согласны ли вы со следующими утверждениями о трудоустройстве с Rust?

Type: matrix (optional)

Утверждения:

- Квалифицированным кандидатам легко найти работу, которая использует Rust для большей части программирования
- Существующие Rust вакансии привлекательны
- Изучение Rust дает мне навыки, которые требуют работодатели
- Я чувствую себя достаточно квалифицированным для подачи заявкок хотя бы на несколько разрекламированных Rust вакансий

Оценка:

- Согласен
- Ни согласен и ни не согласен
- Не согласен

> **justification**
>
> The flip side of the question asking whether the respondent's company plans on hiring Rust developers, we
> want to know how respondents feel the level of demand for and quality of Rust jobs are.

## О вас

Смотри, [кто использует Rust](./design/who.md).

Эта часть опроса предназначена в первую очередь для когортного анализа, а во вторую - для понимания состояния сообщества.

В методологических целях основная часть демографических вопросов находится в конце опроса (если только они не используются для фильтрации вопросов, идущих ранее).
Вопросы являются достаточно лёгкими для ответа (и в конце концов, полезными) и отчасти личными (но на этом этапе люди уже вложились, и мы выстроили "доверие").
Может быть проблематично в начале, если мы зададим все простые личные вопросы и затем перейдём к более сложным - легко бросить.

### Считаете ли вы себя членом недостаточно представленной или маргинализованной группы в сфере технологий?

Пожалуйста, поделитесь только тем, чем вам хотелось бы. Это поможет нам лучше работать с мало представленными и маргинализированные группы, лучше понять, насколько хорошо мы продвинулись в данном направлении, и многое другое.

Type: select all that apply (optional)

- Нет [`NEXT`](#are-you-a-full--or-part-time-student)
- Да, но я предпочитаю не рзглашать
- Культурные взгляды
- Инвалид или лицо с ограниченными возможностями (в том числе физическими, умственными и другими)
- Образование
- Язык
- Лесбиянка, гей, бисексуал, квир или иным образом негетеросексуальный
- Небинарные пол
- Старше или младше знакомых мне разработчиков
- Политические взгляды
- Расовое или этническое меньшинство
- Религиозные взгляды
- Транс
- Женщина или осозднаю себя как женщина
- Другое (свободный ответ)

### Считаете ли вы, что принадлежность к слабо представленной или маргинализованной группе в сфере технологий мешает вам участвовать в сообществе Rust?

Type: select one (optional)

- Часто
- Иногда
- Никогда

### Вы студент дневной или заочной формы обучения?

Type: select one

- Нет
- Да, в средних или старших классах школы
- Да, в бакалавриате
- Да, в магистратуре
- Да, получаю докторскую степень
- Да, участвую в профессиональной программе
- Да, другое

> **justification**
>
> This will be important for cohort analysis. In particular, we want to
> understand how students at different points in their education view
> topics related to Rust.

### Работаете ли вы на условиях полной или неполной занятости (включая оплачиваемые стажировки)?

Type: select one

- Да
- Нет [`NEXT`](#excluding-rust-what-is-your-experience-with-other-kinds-of-programming-languages)

### Заниматесь ли вы разработкой программного обеспечения на работе?

Type: select one

- Да, в основном я занимаюсь разработкой (то есть, не занимаюсь управлением).
- В основном я управляю теми, кто это делает.
- Нет [`NEXT`](#excluding-rust-what-is-your-experience-with-other-kinds-of-programming-languages)

### Как долго вы занимаетесь разработкой приложений профессионально?

Type: select one (optional)

- <= 1 года
- 1 - 3 лет
- 3 - 5 лет
- 5 - 10 лет
- 10 - 20 лет
- > 20 лет

> **justification**
>
> For cohort analysis it is important to understand length of time in the software
> industry as this can have an impact on perceptions.
>
> The ranges of years chosen are a best attempt at capturing different "stages" in a person's professional career.

### Какая категория лучше всего описывает индустрию, в которой вы работаете?

Type: select all that apply (optional)

- Реклама
- Аэрокосмическая промышленность
- Автомобильная промышленность
- Программное обеспечение для бизнеса
- Программное обеспечение для пользователей
- Консалтинг
- Компьютерное оборудование
- Оборона
- Образование
- Энергетика
- Развлечения или СМИ
- Финансы
- Игры
- Правительство
- Медицина
- Производство
- Музыка
- Железные дороги
- Исследовательская деятельность
- Тороговля
- Телекоммуникации
- Транспорт
- Другое (свободный ответ)
- Я не работаю

> **justification**
>
> We want to see what industries have what representation in the Rust community.
> While it's impossible to be precise here, we want to get a general idea.
> This list is largely adopted from this [Wikipedia article](https://en.wikipedia.org/wiki/Outline_of_industry).

### Какие категории лучше всего описывают техническую область, для которой вы на текущий момент разрабатываете программное обеспечение?

Type: select all that apply (optional)

- Аудио программирование
- Блокчейн
- Приложения для облачных вычислений
- Инфраструктура облачных вычисление или утилиты
- Компьютерная графика
- Наука о данных
- Интерфейс приложений для настольных компьютеров
- Сервисы и библиотеки для мобильных или настольных приложений
- Распределённые системы
- Встроенные устройства (с операционной системой)
- Встроенные устройства (без операционной системы)
- HPC (Высокопроизводительные вычисления)
- IoT (Интернет вещей)
- Машинное обучение
- Интерфейс мобильных приложений
- Компьютеная сеть
- Языки программирования и относящиеся к ним инструменты (включая компляторы, IDE, стандартные библиотеки, прочее)
- Робототехника
- Компьютерная безопасность
- Научные и/или числовые вычисления
- Серверные или "бэкенд" приложения
- Симуляция
- Фронтенд веб-приложения
- WebAssembly
- Другое (свободный ответ)

> **justification**
>
> We want to see generally what tech areas respondents work in. In addition to general categories,
> we include some technology categories that are known to be popular in the Rust community.
> This can help us get more insight into what respondents are working on. For instance, if a respondent
> answers their employer works in automotive but they are working on mobile phone applications and not 
> embedded devices, we might conclude different things than if they are working on embedded devices.

### Исключая Rust, каков ваш опыт использования других языков программирования?

Type: matrix (optional)

Языки:

- Языки ассемблера (любой)
- Языки с неавтоматическим управлением памятью (напимер, C, C++, Objective-C без ARC)
- Статически типизированные объектно ориентированные языки со сборщиком мусора (наприме, Java, C#, Go)
- Статически типизированные функциональные языки программирования (например, Haskell, ML)
- Динамически типизированные функциональные языки программирования (например, Lisp, Clojure, Elixir)
- Стаически типизированные языки программирования с новейшей выразительной системой типов (например, Swift, Kotlin, Scala)
- Динамические типизированные языки (например, Javascript, Ruby, Python, PHP, Perl)

Опыт:

- Я ни разу не использовал и не знаком ни с одним языком данной категории
- Я имею базовые знания как минимум об одном из языков данной категории
- Я уверенно использую как минимум один из языков данной категории
- Я эксперт как минимум в одном языков данной категории

> **justification**
>
> For cohort analysis it is interesting to know what other language "families"
> respondents are familiar with. It is more illustrative which types of languages
> respondents are familiar with than the specific language.

### Как давно вы занимаетесь программированием (на любом языке и по любой причине)?

Type: select one (optional)

- < 1 года
- < 3 лет
- < 5 лет
- < 10 лет
- > 10 лет

### Где вы живёте?

Type: select one (optional)

- *государство-член ООН*
- *государтсво-обозреватель (Ватикан или Палестина)*
- Другое (свободный ответ)

> **justification**
>
> We'd like to get a geographic understanding of where the community is. The form of the question allows us to be fairly precise about this
> though there will still be some challenges (e.g., someone who lives in East Russia has similar timezones to East Asia not West Russia).

### Каким способом вам удобнее общаться на технические темы на английском языке?

Type: select all that apply (optional)

- Я уверенно могу общаться на технические темы на английском *устно*
- Я уверенно могу общаться на технические темы на английском *пиьсменно*
- Я уверенно могу читать техническую документацию на английсокм
- Я уверенно могу слушать разговор на техническую тему (например, на конференции или встрече) на английском
- Я уверенно могу читать технические обучающие материалы (например, технические книги, блоги, прочее) на английском
- Я уверенно могу слушать разговор на техническую тему (например, на конференции или встрече) на английском
- Я уверенно могу читать учебные материалы на техническую тематику (например, технические книги, блоги, прочее) на английском

> **justification**
>
> We want to understand self reported feeling of comfort and capability of communication
> of English since a large portion of the Rust community is and likely will always be in English.

### Какие языки вы предпочитаете для технического общения? 

**ВАЖНО**: Ваш ответ должен отражать ваши **предпочтения**, а **не** языки, которыми вы владеете. Например, если вам комфортно и способны вести диалог на технические темы на английскои и корейском, но всегда предпочитаете корейский, вы должны указать *только* корейский, так как он является предпочтительным.

Type: select all that apply (optional)

- Китайский
- Испанский
- Английский
- Хниди
- Бенгальский
- Португальский
- Русский
- Японский
- Турецкий
- Корейский
- Французский
- Немецкий
- Вьетнамский
- Урду
- Другое (свободный ответ)

> **justification**
>
> We want to understand *preference* of technical communication and how that differs
> from their abilities to consume technical communication in English.
> The languages selected are based on all national languages that are members of
> the top 20 most spoken languages in the world.

## Что-либо ещё?

### Желаете ли вы сказать нам что-либо ещё?

Свободная форма (опциоанльно)

> **justification**
>
> While it's unlikely we'll receive any one piece of feedback from this question that will prove to be super useful, 
> having it in the survey can still be useful. It can help us decide on new questions or perspectives that we want to
> try to capture in future surveys. It also gives respondents a place to give thanks or share a particular opinion they
> hold which can be useful in and of itself.
