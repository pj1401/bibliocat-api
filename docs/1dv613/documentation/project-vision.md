# Project Vision

| | |
|---|---|
| Name | Patricia Johansson |
| Username | pj222uc |
| Project name | BiblioCat API |
| Product owner | *Patricia Johansson* |
| Tech stack | Python, Flask, PostgreSQL |

## Problem and target audience

*What problem does your app solve? Who is it for? Be specific - "young adults" is too vague, "university students who need to track shared expenses" is useful.*

Jag vill försöka bygga en bibliotekskatalog API åt ett (påhittat) bibliotek. Som extra funktionalitet kan användare betygsätta böcker. Kanske man också kan dela läsaktivitet med andra användare?  
I de flesta bibliotekskataloger jag har använt är det inte möjligt att betygsätta eller recensera böcker. De flesta använder någon annan tjänst för att hålla reda på böcker som de har läst.

## Market and similar solutions

[*What similar apps already exist? What do they do well, what do they lack? If nothing is exactly the same, how do users solve this problem today?*]: #

- Biblioteksmjukvara:
  - [koha](https://koha-community.org/)
  - [OverDrive](https://www.overdrive.com/)
- Litteraturplattformar:
  - [goodreads](https://www.goodreads.com/)
  - [LibraryThing](https://www.librarything.com)

Biblioteks mjukvara har sällan möjligheten att recensera böcker eller dokumentera läshistorik. Oftast använder man separata plattformar eller egna loggar för att hålla reda på böcker som man har läst.

## Base requirements

*What must the system do to solve the problem? Focus on value, not obvious things like "users can log in". Aim for 3-5 requirements. Full requirements with acceptance criteria go in [Requirements](Requirements).*

- Användarna ska ha möjligheten att söka böcker som finns i biblioteket.
- Användarna ska ha möjligheten att betygsätta lästa böcker.
- Användarna ska ha möjligheten att låna böcker.

## Tech stack

*What technologies are you planning to use and why? Motivation can be prior experience, wanting to learn something, or industry relevance. Detailed architectural decisions - component breakdown, deployment diagram, data model - go in [Architecture](Architecture).*

| Part | Technology | Why |
|---|---|---|
| Backend | Python, Flask | Har fungerat bra när jag har använt de tidigare. |
| Database | PostgreSQL | Jag har använt det tidigare, men vill fortsätta lära mig. |
| Deployment | | |

## How the documentation connects

Each artefact builds on the previous one:

```
Project Vision            - high-level goals and base requirements
  ├─ Project Plan & Risks - milestones, scope, risks
  ├─ Architecture         - how the system is structured
  └─ Design               - user personas, wireframes, user flows
       └─ Requirements         - one requirement per user flow (BR-X)
            └─ Test Specification   - test cases that verify each requirement (TC1.1)
                 └─ Test Report     - results from running those tests
```

Fill these in roughly in order - you don't need everything upfront, but Vision should exist before you write design, and requirements before test cases. Architecture should be an educated guess derived from design and requirements, but can change through iterations.

**These are living documents.** Return to them every iteration as your understanding of the problem and solution evolves. A requirement you wrote in iteration 1 may need updating in iteration 3 - that is expected, not a mistake.
