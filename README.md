# GenAI-projects

This repository is a collection of small generative AI demo projects and utilities. It contains multiple independent subprojects (for example `Autodialer`) and feature branches — the current branch is `Article-generator`.

This README gives a quick overview, how to run the Python projects in the workspace, and contribution notes. Add branch- or project-specific instructions below as needed.

## Repository layout (high level)

- `Autodialer/` — a small project with `main.py`, `req.txt`, and a `templates/` folder.
- `test.py` — top-level test/demo script (if present).
- Branches such as `Article-generator` contain branch-specific code (article-generation features).

If you open this repo locally, inspect each project folder for more detailed README or run instructions.

## Quick start (Linux)

Recommended: use a virtual environment per project.

1. Create and activate a venv (example):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies for a subproject. Example for `Autodialer`:

```bash
pip install -r "Autodialer/req.txt"
```

3. Run the project's main script (example):

```bash
python "Autodialer/main.py"
```

Replace the paths above with the appropriate project and script names for the branch you're working on.

## Git / branch workflow suggestions

- Use feature branches for changes (example: `feature/my-new-article-generator`).
- Keep `main` or `develop` protected and merge via Pull Requests (PRs) with CI checks.
- To combine multiple feature branches before opening a PR, create an integration branch:

```bash
git checkout main
git pull origin main
git checkout -b integrate-features
git merge feature1
git merge feature2
git push origin integrate-features
```

Then open a PR from `integrate-features` into `main`.

## SSH, authentication, and pushing

- If you prefer SSH for git operations, add an SSH key to your GitHub account and use `git@github.com:owner/repo.git` remotes.
- Alternatively use HTTPS + Personal Access Token (PAT) for automation.

## Contributing

- Fork or create a branch off `main`/`develop`.
- Open a Pull Request describing the change and link any related issues.
- Include tests or manual test steps and let CI run.

## Next steps / To do

- Add project-specific README files inside each subfolder (for example `Autodialer/README.md`) with exact install and run steps.
- Add CI (GitHub Actions) to run tests and linting on PRs.

## License

Add a `LICENSE` file to the repository root if you want to declare an open-source license. If you're unsure, I can add a recommended license file for you.

---

If you want, I can:

- Add more detailed run instructions for the `Article-generator` branch specifically.
- Create a `Autodialer/README.md` with exact steps from that subproject.
- Add a `LICENSE` file (MIT, Apache-2.0, etc.).

Tell me which of the above you'd like next and I'll implement it.
