# Annual community survey data sharing

This document describes how data from the annual survey should be shared.

## Objectives

In priority order:

* Protect the privacy of respondents.
* Provide high quality data (unbiased data which is unlikely to be misinterpreted, c.f., raw data).
* Provide useful and actionable data to the Rust Project (i.e., teams and working groups, contributors) and Foundation.
* Provide data in a timely manner.
* Provide data which is generally useful for the community (users and potential users of Rust, and providers of Rust tools and services). Note that this does not mean producing data to be useful for specific segments of the community.
* Provide marketing for Rust.
* Avoid overloading people working directly with the survey data (note that in 2021 there were over 9000 completed surveys and multiple opportunities for free form responses).

Non-goals:

* Making money by selling the data in any form.
* The project will aim to not privilege companies which employ people with access to survey data (raw or processed). However, we acknowledge that controlling widely shared data is impossible.
* Provide individuals or specific groups (including companies or commercial product teams) with data that is likely only beneficial to them and not to the wider project or community.
* Produce a rigorous or complete statistical study of survey results.

## Definitions

### Sensitive data

Sensitive data includes, but is not limited to, personally identifying information (PII, i.e., name, email address, identification numbers, etc).

Note that the survey should never request any PII. However, it is possible that respondents might have supplied such information in free-form responses.

Sensitive data may also include facts which should be kept confidential (e.g., company or national secrets, information which is not publicly known (either about the respondent of others)), offensive remarks or languages, harassment, etc.

Data (raw or derived) which could identify individuals or some groups is sensitive. Care should be taken around raw or derived data with small numbers of respondents, especially where free-form text is present (since styles of writing could be used to further narrow a group). Even data which shows the existence of a group without identifying members may be sensitive, for example data which shows the existence of LGBT respondents in a country where homosexuality is illegal.

Unresolved question: extend this section

### Raw data

Raw data is the data as collected from respondents, including free form answers. Raw data is always considered sensitive and may only be accessed by NDA-signed members of the survey team.

### Summary data

Summary data is data in aggregate form showing the number of respondents giving each answer to a question. Summary data is minimally processed. Summary data excludes free-form answers and groups answers with very small numbers of respondents (where 'small' depends on context, in particular the sensitivity of the question and total number of responses). Summary data may be complete or partial. Summary data should never be sensitive data.

A report containing a maximal amount of summary data will be shared publicly (see below for details). If it exists, summary data excluded from the public report will be shared with the Rust teams and Foundation.

### Processed data

Processed data is any data which has been processed beyond counting answers. That may include analysis of individual questions or analysis across multiple questions (such as cohort analysis or cross-referencing). Processed data may or may not include free-form answers, either individually or in aggregate. Processed data may or may not be sensitive depending on the data and how it is processed.

Processed data will be produced by the survey working group at the request of the Rust teams or Foundation. How it will be shared will be decided by the survey working group on an ad hoc basis, based on the objectives defined above (in particular respondents privacy), sensitivity of the data to the project, and openness.

## Blog post

The survey working group will author a blog post for publication on the main Rust blog as soon as possible after the survey is closed. The blog post should acknowledge respondents, and summarise highlights of the survey data. Highlights should be chosen based on being useful or interesting to a general audience (i.e., Rust users and non-users). The primary intent of the blog post is to communicate interest and usage of Rust, including drilling into interesting categories/use-cases. The blog post should not aim to be a complete summary of the data.


## Initial reporting of data

The survey working group will author an initial report on the survey data. This will contain a summary of responses to all questions with minimal processing, excluding free-form responses, and either excluding or combining groups so that individuals cannot reasonably be identified (i.e., the summary data defined above). The report will highlight data which the survey working group believe will be interesting or useful to members of the Rust Project or Foundation. Timeliness of the report will be prioritised over depth of analysis. The report must not contain any sensitive data. The report will not include raw data (i.e., any individual's responses to questions).

This initial report will be sent to all members of Rust teams, working groups, and the Rust Foundation. Recipients will be asked not to share the report outside the Rust Project and Foundation.

The survey working group will present the report to the Rust Project and Foundation, and answer questions, for example in the Cross-Team Collaboration Fun Times meeting (note that this meeting is public and thus care must be taken not to discuss any sensitive information).

With core team approval, this report will be shared publicly, but not strongly advertised (i.e., a post on the Inside Rust blog, but not the main blog).

Unresolved question: is the core team the right group to approve the public report?

## Ongoing reporting of data

The survey working group will continue to analyse the survey data and may produce further reports, either for teams or the whole Rust Project. The scope of distribution and any requirements for confidentiality agreements will be decided on a case-by-case basis. These reports should never include PII. This responsibility may be transferred to a different Rust team or working group in the future.

Teams and working groups may request further analysis of the survey data by the survey working group. The working group should aim to respond to all requests unless they would expose PII or allow for identification of respondents (e.g., by identifying a small cohort), or the workload on the group is too much. These requests will be prioritised by the survey working group. Responses to these requests may be shared with a wider group within the Rust Project, but should not be shared outside the Project or Foundation. The scope of distribution and any requirements for confidentiality agreements will be decided on a case-by-case basis.

Unresolved question: should there be a time limit?

## Raw data

The full data set of survey responses will never be widely shared. It should be accessible only to the subset of the survey working group responsible for the annual community survey, contractors engaged to help process and analyse the data, and translators (who should only have access to the data they are translating, not the whole data set). These groups may be expanded in the future, but should be kept to a minimum. Everyone with access should have completed a signed confidentiality agreement with the Rust Foundation.

### Archival

It will likely be useful to retain the survey response data long-term ('forever'). This data may be useful for comparison in future years.

Unresolved questions: is storing the data indefinitely allowed by the Rust Foundation's data retention policy? Do we need to scrub any PII before storing (to clarify, this means data which is definitely PII, c.f., data which might be PII)?
