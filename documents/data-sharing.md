# Annual survey data sharing

This document describes how data from the annual survey should be shared.

## Objectives

In priority order:

* Protect the privacy of respondents.
* Provide high quality data (unbiased data which is unlikely to be misinterpreted, c.f., raw data).
* Provide useful and actionable data to the Rust project (Core team, Foundation, teams and working groups, contributors).
* Provide useful data for users and potential users of Rust and providers of Rust tools and services.
* Provide data in a timely manner.
* Provide marketing for Rust.
* Avoid overloading people working directly with the survey data (note that there were over 9000 completed surveys and multiple opportunities for free form responses).

Non-goals:

* We will not aim to make money by selling the data in any form.
* We will aim to not privilege companies which employ people with access to survey data (raw or processed). However, we acknowledge that controlling widely shared data is impossible.


## Blog post

The survey working group will author a blog post for publication on the main Rust blog as soon as possible after the survey is closed. The blog post should acknowledge respondents, and summarise highlights of the survey data. Highlights should be chosen based on being useful or interesting to a general audience (i.e., Rust users and non-users). The blog post should not aim to be a complete summary of the data.


## Initial reporting of data

The survey working group will author an initial report on the survey data. This will contain a summary of responses to all questions with minimal processing, excluding free-form responses, and either excluding or combining groups so that individuals cannot reasonably be identified. The report will highlight and cross-reference data which the survey working group believe will be interesting or useful to members of the Rust project. The report *may* include some more processed summary data, such as graphs or charts, categorisation of free-form answers, re-bucketing of responses to individual questions, or cohort analysis across multiple questions. Timeliness of the report will be prioritised over depth of analysis. The report must not contain any personally identifying information (PII, i.e., name, email address, identification numbers, etc). The report will not include raw data (i.e., any individual's responses to questions).

This initial report will be sent to all members of Rust teams, working groups, and the Rust Foundation. Recipients will be asked not to share the report outside the Rust project.

The survey working group will present the report to the Rust project and answer questions, for example in the Cross-Team Collaboration Fun Times meeting (note that this meeting is public and thus care must be taken not to discuss and sensitive information).

A reduced version of the report with any sensitive information removed will be produced after the initial report is distributed. With core team approval, this report will be shared publicly, but not strongly advertised (i.e., a post on the Inside Rust blog, but not the main blog).

Unresolved questions: is the core team the right group to approve the public report? Should we specify what we consider sensitive?

## Ongoing reporting of data

The survey working group will continue to analyse the survey data and may produce further reports, either for individuals, teams, or the whole Rust project. The scope of distribution and any requirements for confidentiality agreements will be decided on a case-by-case basis. These reports should never include PII. This responsibility may be transferred to a different Rust project team or working group in the future.

Teams and working groups may request further analysis of the survey data by the survey working group. The working group should aim to respond to all requests unless they would expose PII or allow for identification of respondents (e.g., by identifying a small cohort), or the workload on the group is too much. These requests will be prioritised by the survey working group. Responses to these requests may be shared with a wider group within the Rust project, but should not be shared outside the project. The scope of distribution and any requirements for confidentiality agreements will be decided on a case-by-case basis.

Unresolved question: should their be a time limit?

## Raw data

The full data set of survey responses will never be widely shared. It should be accessible only to the subset of the survey working group responsible for the annual survey, contractors engaged to help process and analyse the data, and translators (who should only have access to the data they are translating, not the whole data set). These groups may be expanded in the future, but should be kept to a minimum. Everyone with access should have completed a signed confidentiality agreement with the Rust Foundation.

### Archival

Note that the survey should not request any PII. However, it is possible that respondents might have supplied such information in free-form responses.

It will likely be useful to retain the survey response data long-term ('forever'). This data may be useful for comparison in future years.

Unresolved questions: is storing the data indefinitely allowed by the Rust Foundation's data retention policy? Do we need to scrub any PII before storing (to clarify, this means data which is definitely PII, c.f., data which might be PII)?
