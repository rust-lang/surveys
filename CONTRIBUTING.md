# How to contribute to the State of Rust survey

Great that you want to help with the State of Rust survey! The State of Rust survey is the annual platform for us to look at how was the past year of work and for the community to express their wishes.

The survey platform of choice is currently [Survey Hero](https://www.surveyhero.com). We have reached a general consensus that, while not perfect, it works rather well for us therefore we are not looking into alternatives for the time being.

The State of Rust survey is published usually in the first half of December. Contributions are tipically needed once a year as we approach to the deadline. The initial work to kickoff the survey is taken care of by the [Survey Team](https://github.com/rust-lang/team/blob/master/teams/community-survey.toml). Contributions are welcome to translate the survey into multiple languages. The more, the merrier.

Here's a rough timeline of the work:
- The State of Rust survey is discussed on Zulip (in [#t-community/survey](https://rust-lang.zulipchat.com/#narrow/channel/402479-t-community.2Frust-survey)). We gather feedback about the previous year's survey, we ask the main teams if they have specific wishes and we draft the English survey
- In the meantime we start recording interest from volunteers to translate the survey into different languages
- After the English survey is finalized and uploaded on Survey Hero, translators can start their work

Here's how the translation effort is coordinated:
- The Survey Team will first generate translation drafts by using a Survey Hero tool to machine-translate the English survey into other languages. The team will generate drafts only for languages we know will be reviewed by a human.
- Contributors will Keep an eye on the Zulip topic and will be contacted to receive an access token to access Survey hero and be able to work on a specific translation.
- Once the human review on Survey Hero is complete, the Survey Team will download the machine-translated drafts (Markdown files) and open pull requests on this repository
- Contributors will review again the pull request, proof-reading and fixing all inconsistencies
- Once the translation pull request is merged will be merged back into Survey Hero by the Survey Team

Thanks for helping us making the State of Rust survey more accessible!

## A few notes

- Translations are volunteer-based and best-effort
- We will not publish survey translations not reviewed by a human
- We will only publish translations that we are reasonably confident they reach a minimum standard of quality. Below this threshold we would make a disservice to the community.
- We recommend contributors avoiding non-UTF-8 whitespaces
- We refer to the ISO language code such as `en-US`, `zh-CN`, `fr-CA`, `fr-FR`, etc. (here's a [list](http://www.lingoes.net/en/translator/langcode.htm))
