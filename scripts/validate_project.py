#!/usr/bin/env python3
"""Validate the Build Week plugin without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def frontmatter(text: str, path: Path) -> tuple[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(f"missing YAML frontmatter: {path.relative_to(ROOT)}")
    block = match.group(1)
    name = re.search(r"^name:\s*([^\n]+)$", block, re.MULTILINE)
    description = re.search(r"^description:\s*(.+)$", block, re.MULTILINE)
    if not name or not description:
        fail(f"frontmatter must contain name and description: {path.relative_to(ROOT)}")
    return name.group(1).strip().strip('"'), description.group(1).strip()


def main() -> int:
    manifest_path = ROOT / ".codex-plugin" / "plugin.json"
    if not manifest_path.is_file():
        fail("missing .codex-plugin/plugin.json")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("name") != "portable-judgment-methods":
        fail("unexpected plugin name")
    if manifest.get("skills") != "./skills/":
        fail("manifest does not expose ./skills/")

    required = {
        "audit-decisions": ["## Run the audit", "## Output format", "## Retrospective scoring"],
        "update-ryuta-market-outlook": ["## Evidence priority", "## Regime decision", "## Required output"],
    }
    found: set[str] = set()
    for skill_file in sorted(SKILLS.glob("*/SKILL.md")):
        text = skill_file.read_text(encoding="utf-8")
        name, description = frontmatter(text, skill_file)
        if name in found:
            fail(f"duplicate skill name: {name}")
        found.add(name)
        if len(description) < 40:
            fail(f"description is too short: {name}")
        interface = skill_file.parent / "agents" / "openai.yaml"
        if not interface.is_file():
            fail(f"missing agents/openai.yaml: {name}")
        for heading in required.get(name, []):
            if heading not in text:
                fail(f"{name} is missing required section: {heading}")

    if found != set(required):
        fail(f"expected {sorted(required)}, found {sorted(found)}")

    print("PASS: plugin manifest")
    for name in sorted(found):
        print(f"PASS: {name}")
    print("PASS: Judgment Portability Layer is structurally ready")
    return 0


if __name__ == "__main__":
    sys.exit(main())
