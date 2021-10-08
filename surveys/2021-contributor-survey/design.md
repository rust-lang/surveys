# Design

The following documents the design of the Rust 2021 Contributor Survey starting from high-level design goals down to specific questions we want survey data to help us answer.

## Design Goals and Audience

The Rust Contributor Survey's goal is to help the Rust Foundation and Rust
Project Leadership identify the biggest problems affecting rust contributors
and maintainers and where possible, their causes. The foundation and project
leadership will then use this information to design initiatives that fix or
alleviate these problems in order to provide effective support to maintainers
and contributors to the rust projects and to improve the health and
sustainability of the rust project over time.

Ultimately, the survey should help different audiences (discussed below) answer
the following questions:

* What are the biggest problems affecting maintainers of the Rust Project.
* What are the causes of issues we are already aware of?
    * New contributors doing one or two PRs then leaving: How do we retain
      contributors and grow them into reviewers and maintainers?
        * What issues are causing new contributors to disengage?
    * Long time contributors stepping away from the project: Retaining domain
      expertise and the shape of unsustainable development
        * What got them involved?
        * What got them to stay for so long?
        * What made them leave the project?
            * Burnout?
    * Maintainers who stay with the project for a long time: The shape of
      sustainable development
        * What got them involved?
        * What has got them to stay?
    * Insufficient review capacity
        * How much review capacity do teams have?
        * How much review load do teams have?
        * What is a sustainable review burden? (based on available time, volunteer vs full time maintainers)
* Which teams are healthy or unhealthy?
    * What makes them healhty or unhealthy?

Parts of these questions will be interesting and useful to different audiences
of the survey results. The following are audiences we explicitly want to keep
in mind:

* Rust leadership: those in some sort of leadership role in the Rust project
  (i.e., core team, team leads, foundation members, project team members/leads, etc.)

Ultimately each piece of information gained from the survey should be useful to
at least one of the audiences above. While it may be tempting to collect
interesting facts and trivia about Rust, the ultimate goal of the survey favors
information that is a *actionable*.
