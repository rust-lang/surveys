# Survey Markdown format reference
This document serves as a reference for creating new surveys. We use a Markdown format for describing surveys. The MD
files do not have a completely strict structure, but it is good to follow some form of a template to keep things uniform.

You can check out the various existing surveys for an example of the Markdown file, e.g. [2023 annual survey](../2023-annual-survey/questions.md) or [2022 annual survey](../2022-annual-survey/questions.md).

## Format
The general format of the file looks like this:
```markdown
# Survey questions

<general description of the survey>

## <section-1>

### <question-1>

<question clarification> (optional)

Type: <question-type>

<prepared-answers>

> **justification** (optional)
<explain why do you ask this question>

### <question-N>

## <section-N>
...
```

### Question types
We use the SurveyHero system for running surveys, which supports several question types:
- Select one answer (`select one`). The user can choose one answer from a prepared set of answers.
    ```markdown
    ### Which language do you like the most?

    Type: select one

    - Rust
    - Python
    - C++
    ```
    You can also mark one answer as an open response, e.g. `- Other (open response)`
- Select all that apply (`select all that apply`). The user can select `0` to `N` answer to this question.
    ```markdown
    ### Which operating systems do you use?

    Type: select all that apply

    - Windows
    - Linux
    - macOS
    ```
    You can also mark one answer as an open response, e.g. `- Other (open response)`
- Free text (`free text`). The user fills an open answer into a text area.
    ```markdown
    ### Is there anything else you'd like to tell us?

    Type: free text
    ```
- Matrix (`matrix`). The user assigns a selected column for each row of this question. For example, they
   might assign "Not at all"/"A little"/"A lot" category to each answer. You specify also the labels that represent what do the rows and columns mean. In the example below, each row is an "aspect" and each column is a "priority".
    ```markdown
    ### Which Rust features should we prioritize?
  
    Type: matrix
  
    Aspects:
  
    - Runtime performance
    - Compilation performance
    - Binary size
    - Compiler error messages

    Priority:

    - High Priority
    - Medium Priority
    - Low Priority
    ```
    This would create a question that looks like this:
    ```
                                High Priority      Medium Priority      Low Priority
  
    Runtime performance               o                  o                    o
    Compilation performance           o                  o                    o
    Binary size                       o                  o                    o
    Compiler error messages           o                  o                    o
    ```

### Optionality
If you want to make a given question optional, add `(optional)` after the question type.
```markdown
### Which IDE do you prefer?

Type: select one (optional)

- RustRover
- Rust Analyzer
```

### Navigation
By default, all questions will be filled in the survey in the order you put them in the Markdown file. If you want to make jumps, you can optionally add a `NEXT` anchor after any prepared answer:
```markdown
### Do you like Rust?

Type: select one

- Yes [`NEXT`](#tell-us-about-rust)
- No [`NEXT`](#which-language-do-you-like)

### Tell us about Rust

### Which language do you like
```

The address of the link should point to a Markdown `#<anchor>` of the following question that should be displayed if the user selects the given answer.
