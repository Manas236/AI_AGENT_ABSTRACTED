# AI Agent (Abstracted)

> Created by **Manas Gawde** — https://github.com/Manas236

An autonomous AI agent system that independently ideates, architects, implements, validates, and ships Python projects to GitHub — running on a fully automated pipeline with zero human intervention per project.

---

## What It Does

The system operates as a closed-loop autonomous developer:

1. **Ideation** — Generates unique, scoped Python project ideas using an LLM, filtered by category rotation, complexity caps, and a history of past projects to avoid duplication.
2. **Architecture** — Expands each idea into a full project blueprint: modules, files, execution order, and interface contracts.
3. **Code Generation** — Produces each file individually via LLM, one at a time, guided by the blueprint.
4. **Validation Pipeline** — Every generated file passes through a static scanner, dependency installer, isolated sandbox runner, and safeguard gate before being committed.
5. **Self-Healing** — Failed files are automatically retried using an AI-powered fix engine. Projects with too many failures are safely abandoned.
6. **Autonomous Git Operations** — Each successful file is committed with a semantically appropriate message and pushed to a newly created GitHub repository.
7. **Post-Project** — Generates a README, writes a LICENSE, and performs a final push to close the project.
8. **Pacing & Behavior** — Randomized start delays, daily project caps, and configurable work windows simulate organic development behavior.

---

## System Architecture

```
main.py                     ← Pipeline entry point
├── behavior_simulation.py  ← Pacing, skip-day logic, work windows
├── project_selector.py     ← LLM-powered idea generation & ranking
├── project_expander.py     ← Idea → structured architecture blueprint
├── blueprint_manager.py    ← Blueprint locking, hashing, validation
├── repo_naming.py          ← Sanitized, kebab-case repo name generation
├── git_engine.py           ← Git CLI wrapper + GitHub API repo creation
├── workflow_controller.py  ← File-by-file orchestration loop
│   ├── file_generator.py   ← LLM code generation per file
│   ├── static_scanner.py   ← Pre-execution safety scan
│   ├── dependency_manager.py ← Import extraction + pip install
│   ├── sandbox_runner.py   ← Isolated subprocess execution
│   ├── validator.py        ← Output structure & field validation
│   ├── safeguard_engine.py ← Final gate: all checks must pass
│   ├── fix_engine.py       ← LLM-powered repair on failure
│   ├── commit_engine.py    ← Commit message generation
│   └── retry_controller.py ← Rate limit & API failure handling
├── decision_engine.py      ← Abandonment logic & project completion
├── execution_tracker.py    ← Per-file attempt & error tracking
├── state_manager.py        ← Persistent project state (JSON)
├── cost_monitor.py         ← Token usage tracking & budget enforcement
├── dynamic_monitor.py      ← Runtime anomaly detection
├── storage_manager.py      ← Local backup & cleanup
├── project_history.py      ← Cross-run deduplication history
├── config_loader.py        ← Env config, API key rotation, LLM client
├── logger.py               ← Structured logging (console + file)
├── readme_generator.py     ← Auto README generation
├── license_generator.py    ← LICENSE file writer
├── cleanup_projects.py     ← Disk cleanup when project count exceeds threshold
├── backfill_licenses.py    ← One-time: add LICENSE to existing projects
└── backfill_readmes.py     ← One-time: add README to existing projects
```

---

## Key Design Decisions

- **One file at a time** — The LLM generates one source file per call, bounded by the blueprint, keeping context tight and outputs verifiable.
- **Blueprint as contract** — A locked, hashed blueprint acts as the immutable spec. All generated code is validated against it.
- **Sandbox-first** — Every generated file runs in an isolated subprocess before any commit is made. Bad code never reaches the repo.
- **Graceful abandonment** — Projects with ≥3 failures at <50% completion are silently abandoned: remote repo deleted, local workspace cleaned, history updated.
- **API key rotation** — The system cycles through multiple Gemini API keys with per-model fallback chains, maximizing resilience.
- **Refinement sprints** — After the initial build, the system runs up to 2 additional sprints to expand the project with new modules.

---

## Configuration

All configuration is driven by environment variables in a `.env` file:

| Variable | Description |
|---|---|
| `GEMINI_API_KEY` | Primary Gemini API key |
| `GEMINI_API_KEY_2` ... | Additional keys for rotation |
| `GITHUB_TOKEN` | GitHub personal access token |
| `GITHUB_USERNAME` | GitHub username |
| `GITHUB_EMAIL` | Git committer email |
| `SKIP_DAY_CHANCE` | Probability of skipping a day (0.0–1.0) |
| `MIN_START_DELAY` / `MAX_START_DELAY` | Randomized startup delay range (seconds) |
| `DAILY_TOKEN_LIMIT` | Max tokens per day |
| `DAILY_CALL_LIMIT` | Max API calls per day |
| `ELITE_MODE` | Enables advanced project generation |

---

## License

This project is licensed under a **Proprietary Source License**.
See [LICENSE](LICENSE) for full terms.

**Commercial use is prohibited without a written agreement and compensation to the author.**
All forks, derivatives, and works claiming this as inspiration must credit:
> Manas Gawde — https://github.com/Manas236
