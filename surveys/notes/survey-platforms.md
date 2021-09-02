# Survey Platform

The survey platform we use is ???.

## Functionality 

An ideal survey platform has the following functionality:
* One survey can consist of multiple translations
* The data is aggregated across translations
* Works in China 
* Low cost and pay-as-you-go

## Survey Platform Assessments

### SurveyHero (surveyhero.com)

* One survey, multiple languages
* Single output format – reduced data wrangling
* Automatic translate powered by Google
* Ability to review translations and make edits
* Manual editing capabilities (Original text visible during translation)
* Native management of RTL text
* Requires Business ($55/mo. Individual; $39/user/mo. Team [2 minimum])/Enterprise ($89/mo. Individual; $69/user/mo. Team) level subscription
  * Both for the translations and for the logic required for the Rust survey
* As of 2021-09 works in China reliably (seemingly due to not being blocked and using Irish IP addresses which won't be mistaken for VPN IP addresses).

### SurveyMonkey (surveymonkey.com)

* One survey, multiple languages
* Single output format – reduced data wrangling
* All translation done outside of survey platform
  * Create survey in base language (if need RTL language, it must be the default for the survey)
  * Uses set of csv files that are exported (after initial survey creation) and then imported with translation – And is a beta feature.
* No automatic translate
* Requires Team Premier ($75/user/mo. w/ 3 user minimum & billed annually)
  * Both for translations & logic. 
  * 15,000 response max 
* As of 2021-09 works in China somewhat reliably (might be less reliable than SurveyHero due to using Japanese and Hong Kong IP addresses which have been used by VPNs in the past).

### Qualtrics

* One survey, multiple languages
* Single output format – reduced data wrangling
* Automatic translate powered by Google
* Ability to review translations and make edits
* Manual editing capabilities (Original text visible during translation)
* Can also support translation uploads
* Paid translation also available (quote basis)
* Automatic language detection based on browser setting
  * Can switch language at any point in the survey (additional interface option that may be distracting?)
* Allows filter based on language
* $$$$$ (Exact amount unclear – potentially starts at $1500/year?. Would require quote…)

### Google Forms

* Separate survey for each language
* Multiple survey output – requires more data wrangling
* Ease of shared editing
* Unlimited responses
* Free