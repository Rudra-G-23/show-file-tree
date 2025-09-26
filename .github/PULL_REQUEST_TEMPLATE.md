## Summary (one line)
🔑 Provide a short description of what this PR does.

**Example:** Add `--top` flag for showing top N files by size

---

## Type of change
📦 Bug fix / New feature / Data change / Model/Experiment / Documentation / Infrastructure/CI / Deployment

---

## Motivation / Business Context
💡 Why are these changes needed? What problem or use case do they solve?

---

## Detailed description of changes
📝 List the main changes (files, modules, datasets, configs)
- Added cli flag `--top`
- Updated `tree_renderer.py` to support table output
- Modified `tests/test_cli_basic.py`

---

## Reproducibility Steps
🔄 How can reviewers run and verify your changes locally?
1. `pip install -e .`
2. Run `show-file-tree tests/fixtures/sample_tree --top 3`

---

## Tests
🧪 New/updated tests and CI status
- Added `test_cli_top.py`
- CI: passing ✅ / failing ❌

---

## Documentation updates
📚 Link or describe updated docs, README, or usage examples.

---

## Deployment / Rollout Plan
🚀 If applicable (monitoring, rollback, etc.)

---

## Checklist
- [ ] Code follows project style / lint rules
- [ ] Tests added/updated and passing locally
- [ ] Data validation (if applicable) completed
- [ ] Docs/README/usage updated
- [ ] No sensitive/PII data introduced
