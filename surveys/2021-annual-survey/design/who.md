# Who is using Rust?

At a high-level, there are two groups of information that we want to collect from respondents about who they are:
* demographic information for cohort analysis (i.e., demographic info on *survey respondents*)
* demographic information to better understand the overall shape of the community (i.e., extrapolation on the demographic makeup of the Rust community as a whole)

## Cohort Analysis

We aim to collect demographic information such that we can group survey takers into various cohorts which we can perform cohort analysis which allows for comparing how different cohorts differ across different dimensions. 

Cohort analysis allows us to not only answer questions about the entire dataset of respondents but also subgroups that have potentially interesting defining characteristics.

For example, cohort based on experience with different types of programming languages could allow us to find out if the experience of using Rust is markedly different for systems programmers (i.e., those who exclusively use languages like C and C++) is different than for those who use dynamically-typed languages (i.e., those who exclusively use languages like JavaScript and Python).

### The cohorts 

The cohorts should include:

* Current user of Rust, former user of Rust, non-user of Rust
* Types of programming languages used (i.e., extensive and current use of a programming language that fits into a given category):
  * Systems programming (C, C++) 
  * Statically-typed "modern" language (Haskell, Scala, Swift, Kotlin, etc.)
  * OO Languages (Java, Objective-C, C#)
  * Dynamically-typed languages (Ruby, JavaScript, Python)
* Identifies with an underrepresented group in technology 
* Industry (e.g., general software, banking, transportation, etc.)
* Current stack (server networking, desktop application, mobile application, web application, embedded, etc.)


## Community shape

Other demographic information can be collected just to better understand the shape of Rust community. While cohort analysis could also be performed based on these factors, we have a strong feeling that these indicators won't lead to interesting cohort analysis. Further investigation may prove this assumption to be incorrect however. 

The other demographic information includes:
* Location
* Preferred human language for technical communication

Other possible information we might consider collecting:
* salary 
* operating system preference
* IDE preference
* education level and CS specialization or not
* gender 

Demographic information can be personal, and we don't want to make survey respondents uncomfortable with the level of information being asked. When possible we should offer the respondent the possibilty to not give a response. 

## Why is the information useful?

As indicated above, demographic information paired with cohort analysis allows us to do analysis on subsets of the survey respondent population on various potentially interesting dimensions.

In general, demographic information can also help lead to additional investigation if a particular subslice of the population is surprisingly over or under represented.