# Devpost submission draft

## Project name

Judgment Portability Layer

## Tagline

Transfer a human decision method between AI environments—without transferring the human.

## Category

Developer Tools

## Inspiration

After keeping seven years of timestamped market records, I used Codex and GPT-5.6 to extract not only what I had concluded, but how I repeatedly made and revised decisions. The resulting market Skill was useful but highly specialized. I then extracted the underlying decision-audit method into a second, general Skill and installed it in another person's personalized AI. It worked without transferring either person's identity, private memory, or personal data.

That suggested a new unit of knowledge transfer: not a prompt, persona, or dataset, but an inspectable human decision method.

## What it does

Judgment Portability Layer is an installable Codex plugin with two Skills:

1. Decision Audit reconstructs an objective, separates observations from interpretations, tests supporting and counterevidence, compares risk-adjusted alternatives, proposes a reversible test, and defines invalidation conditions.
2. Market Outlook encodes a seven-year, regime-based investment decision practice with evidence priority, historical precedents, exact allocation rules, and explicit update conditions.

The first proves that the method generalizes. The second proves that the architecture can carry deep specialist judgment.

## How we built it

Codex and GPT-5.6 were used to inspect long decision records, reconstruct causal chains, detect repeated operating rules, distinguish durable rules from regime-specific ones, compress the result into Skill procedures, and package the Skills as a testable plugin. A local validator checks the manifest, frontmatter, interfaces, unique Skill names, and required method sections.

The architecture separates identity, philosophy, reusable method, and specialist domain knowledge. Only the method and deliberately selected domain layer are shared.

## Challenges

The hardest problem was avoiding retrospective storytelling. A method extracted from old records can easily absorb later information or confuse good outcomes with good decisions. The Skills therefore enforce decision timestamps, separate later evidence, preserve counterevidence, and define update conditions. The second challenge was keeping the method useful without smuggling in the author's personality or another user's private context.

## Accomplishments

- Distilled seven years of recorded market decisions into a runnable Skill.
- Derived a general decision-audit Skill from the specialist practice.
- Successfully transferred the general method into another personalized AI without transferring identity or memory.
- Packaged both methods as one installable, inspectable developer tool.
- Made professional authority boundaries and invalidation conditions part of the runtime method.

## What we learned

The most valuable part of personalization may not be an AI knowing more facts about a person. It may be the AI learning which evidence the person prioritizes, how they handle contradiction, when they change regimes, and what makes them reverse a decision. Those structures can be separated from identity and shared deliberately.

## What's next

The next step is an evaluation format for method fidelity: give the original and recipient AI the same unseen cases, compare the structure of their decisions, and measure where the transferred method remains faithful or needs revision. That would make tacit-knowledge transfer testable rather than anecdotal.

## Built with

Codex, GPT-5.6, ChatGPT Skills, Codex plugins, Python.
