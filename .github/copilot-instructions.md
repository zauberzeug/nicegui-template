# GitHub Copilot – Review Instructions for nicegui-template

**Purpose**: Maximize signal/noise, maintain template quality, and offload maintainers.
Copilot acts as a _single, concise reviewer_.
Prefer one structured top-level comment with suggested diffs over many line-by-line nits.

**Standards Reference**: Before starting a review, internalize all coding standards, style guidelines, and contribution workflows defined in [CONTRIBUTING.md](../CONTRIBUTING.md).
Also make sure to follow [AGENT.md](../AGENT.md).
This file defines review-specific automation rules only.

## Scope & Tone

- Audience: PR authors and maintainers of nicegui-template
- Voice: concise, technical, actionable. No style opinions when linters/formatters are green
- Output format: one summary + grouped findings (**BLOCKER**, **MAJOR**, **CLEANUP**) + **suggested diff** blocks where possible

## Severity Mapping

### BLOCKER (if violated ⇒ request changes)

1. **Template syntax errors**: Invalid Jinja2 syntax, undefined variables, broken conditionals
2. **Breaking changes**: Changes that break existing generated projects without migration path
3. **Missing tests**: New template options without corresponding tests; untested file combinations
4. **Documentation gaps**: New copier.yml questions not added to README.md table
5. **Tests & CI**: failing tests; ignoring linters/formatters
6. **PR description quality**: missing/vague problem statement or motivation
7. **Security**: exposed secrets/credentials in templates or tests

### MAJOR (should be fixed before merge)

1. **Template quality**: Complex/hard-to-understand Jinja2 logic; should be simplified
2. **Scope creep**: Project-specific details in templates (should stay generic/universal)
3. **File placement**: Unexpected template file location without rationale
4. **Test coverage**: Edge cases untested (various option combinations, conditional file generation)
5. **Unnecessary complexity**: Simpler template design meets requirements
6. **Duplicate content**: Repeated Jinja2 blocks that should use variables or includes

### CLEANUP (suggest quick diffs)

1. **Readability**: Complex template logic without comments; unclear variable names
2. **Whitespace handling**: Missing `{%- -%}` in Jinja2 where whitespace control needed
3. **Consistency**: Inconsistent template patterns across similar files

## Template-Specific Checks

- **Generated project works**: Can the generated project be installed and run?
- **Jinja2 syntax**: Valid templating with proper variable substitution?
- **File naming**: Conditional filenames work correctly?
- **Option combinations**: All combinations of copier.yml options tested?
- **README.md updated**: New questions added to the options table?
- **Generic content**: Templates stay universal and don't include project-specific details?

## What to Produce

Structure your comment like this:

**Summary**

Lead with the motivation of the change, then explain what changed and why.
Finish with general risk assessment and impact.

**BLOCKER**

Itemized violations of critical rules with short rationale

**MAJOR**

Concrete issues that should be fixed pre-merge

**CLEANUP**

Low-noise, quick-win improvements

**Suggested diffs**

Use GitHub's suggestion blocks (apply only if trivial and safe):

```diff
- {% if use_poetry %}
+ {%- if use_poetry %}
```

## Copilot Behavior Controls

- Prefer **one** top-comment; avoid scatter
- If evidence is weak/speculative, ask a short question instead of asserting
- If change is broad: propose a tiny follow-up PR rather than expanding this one

## Quick Checks

Mental checklist before posting review:

1. **Template syntax valid?** No Jinja2 errors? Variables defined in copier.yml?
2. **Tests added/updated?** All option combinations covered?
3. **README.md updated?** New questions documented in table?
4. **Code follows [CONTRIBUTING.md](../CONTRIBUTING.md)?** Style, organization, principles?
5. **Generated projects work?** Can install, run, and lint?
6. **Templates stay generic?** No project-specific details leaked in?

---

> Maintainers: update this file as conventions evolve.
> Copilot will treat this file as authoritative for review behavior.
