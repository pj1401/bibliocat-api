# Contributing

## Getting started

*How do I clone and run this project locally?*

```bash
git clone <repo-url>
# add steps here
```

## Environment variables

*Never commit secrets or API keys. Copy `.env.example` to `.env` and fill in your values.*

| Variable | Description |
|---|---|
| `DATABASE_URL` | |
| `SECRET_KEY` | |

## Folder structure

*Brief map of the repo - what lives where.*

```
/
├── src/        # application source
├── tests/      # test files
└── ...
```

## Coding style

*What conventions are you following? Link to a style guide if there is one.*

- Language/framework style guide:
- Linting tool:
- Formatting tool:

## Branching

- `main` - stable, deployable code only
- `feature/your-feature` - one branch per issue
- Never push directly to `main`

## Commit messages

Short and descriptive. Reference the issue number:

```
Add login form (#12)
Fix broken redirect on logout (#15)
```

## Merging to main

Before merging a feature branch:
- [ ] Code works locally
- [ ] Tests pass
- [ ] No `.env` or secrets committed
- [ ] Linked to an issue

## Running tests

```bash
# add your test command here
```

## Time tracking

Every issue should have an estimate and logged time. Use quick actions in issue comments:

```
/estimate 2h
```
```
Implemented the login form, took longer due to validation edge cases.
/spend 3h
```

**For non-development time** (reading, videos, lectures, meetings) - don't create a separate issue for each. Use one standing issue per iteration called **"Learning & overhead - Iteration N"** and log time there:

```
Watched CI/CD lecture video.
/spend 1h
```

```
Read course literature chapter 4.
/spend 1.5h
```

Log time as you go - **not at the end of the week.** All time counts: coding, reading, debugging, meetings.

## Versioning

This project uses [semantic versioning](https://semver.org) with Git tags: `vMAJOR.MINOR.PATCH`

- **MAJOR** - breaking changes
- **MINOR** - new features, backwards compatible
- **PATCH** - bug fixes

Each iteration ends with a tag. The tag is your deliverable - if it is not tagged, it is not done.

```bash
git describe --tags --dirty
# -> v1.0.0          (exactly on a tag)
# -> v1.0.0-4-gabcde (4 commits after v1.0.0)
# -> v1.0.0-4-gabcde-dirty (uncommitted changes)
```

To tag a release:

```bash
git tag v1.0.0
git push origin v1.0.0
```
