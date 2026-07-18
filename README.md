# Judgment Portability Layer

Most AI personalization tries to make a model know more about a person. This project asks a different question:

> Can an AI carry a person's decision method without carrying the person?

Judgment Portability Layer is an installable Codex plugin containing two working Skills:

- `audit-decisions`: a general decision-audit method that separates objectives, observations, interpretations, counterevidence, risk, reversibility, invalidation conditions, and authority.
- `update-ryuta-market-outlook`: a specialist implementation distilled from seven years of recorded market decisions. It treats market views as regime decisions and translates them into explicit portfolio actions and update conditions.

Together they demonstrate a portable knowledge architecture:

1. Extract a repeated human decision process from a long decision record.
2. Separate the method from biography, personality, and private memory.
3. Encode the method as an inspectable Skill with triggers, procedures, boundaries, and output contracts.
4. Install it in another AI environment.
5. Test whether the recipient can reproduce the decision structure on new cases.

This is not prompt sharing. A prompt asks for an answer once. A Skill carries an operating method across tasks.

## Why two Skills?

The pair is the proof.

| Skill | Role | What it proves |
| --- | --- | --- |
| Decision Audit | General engine | A decision method can work across personal and professional domains. |
| Market Outlook | Specialist implementation | A dense, longitudinal expert practice can be encoded with domain-specific evidence priority, regime logic, allocation rules, and invalidation conditions. |

The general Skill shows portability. The specialist Skill shows depth.

## Install

Clone this repository and install the plugin from its root using the Codex plugin interface. The plugin manifest is at `.codex-plugin/plugin.json`; both Skills are under `skills/`.

For direct inspection or manual testing, each Skill is self-contained:

```text
skills/
├── audit-decisions/
│   ├── SKILL.md
│   └── agents/openai.yaml
└── update-ryuta-market-outlook/
    ├── SKILL.md
    └── agents/openai.yaml
```

No API key, external service, personal memory, or private dataset is required to test the decision-audit Skill. Current market analysis requires live, authoritative market data, as stated by the market Skill itself.

## Try it

### General decision audit

```text
Use $audit-decisions to audit this decision:
We launched a new publication channel for reach, received 300 clicks and no sales,
and the platform created administrative friction. Should we continue, modify, or stop?
```

Expected behavior: the Skill identifies the true objective, separates observed results from interpretations, distinguishes sunk cost from future value, proposes the smallest informative next test if one exists, and defines explicit stop conditions.

### Specialist market regime decision

```text
Use $update-ryuta-market-outlook to assess whether a new S&P 500 high justifies
raising equity exposure when the US 10-year yield is simultaneously moving toward 5%.
Separate observed facts, causal inference, regime judgment, portfolio action,
and invalidation conditions.
```

Expected behavior: the Skill refuses to treat price alone as confirmation, checks whether long yields validate or reject the breakout, keeps long- and short-horizon judgments separate, and maps the conclusion to exact weights.

## Test and validate

Run the repository checks:

```bash
python3 scripts/validate_project.py
```

The validator checks plugin structure, Skill frontmatter, unique names, interface files, and required method sections. OpenAI's plugin and Skill validators should also be run when available in the local Codex installation.

## Architecture

The project deliberately separates four layers:

1. **Identity layer** — biography, preferences, relationships, private memory. Not transferred.
2. **Philosophy layer** — the person's highest-order values and interpretive principles. Optional and remains with the owner unless explicitly shared.
3. **Method layer** — repeatable decision procedure, evidence hierarchy, counterevidence handling, and update rules. This is what the Skills transfer.
4. **Domain layer** — specialist facts, variables, precedents, and output contracts. Added only where needed.

This separation reduces privacy exposure and makes the transferred knowledge inspectable, testable, revisable, and revocable.

## Built with Codex and GPT-5.6

Codex was used to:

- inspect and reconcile seven years of decision records;
- identify repeated judgment patterns and regime-change rules;
- separate observations, interpretations, operating rules, and invalidation conditions;
- convert the extracted methods into Skills with explicit trigger and output contracts;
- test portability by installing the Skills in another personalized AI environment;
- package both Skills as a reproducible plugin and create validation and demonstration materials.

GPT-5.6 was used for long-context synthesis, contradiction checking, procedure compression, and the final plugin implementation and validation workflow.

## Privacy and safety

- No third party is identified.
- No recipient's memory, personality profile, or personal data is included.
- The market Skill is a decision-support method, not delegated financial authority.
- The audit Skill explicitly preserves professional authority boundaries for medical, legal, fiduciary, employment, and regulatory decisions.

## License

The plugin code and validation script are released under the MIT License. The two Skill texts are provided for Build Week judging and testing; attribution to Ryuta Sugimoto is required for redistribution.
