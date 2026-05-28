# Iteration 6

**Milestone:** [Iteration 6](https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/milestones/5)  
**Project Iteration:** [Iteration 6](https://gitlab.lnu.se/groups/1dv613/student/pj222uc/workspace/-/cadences/59/iterations/573)  
**Period:** 2026-05-02 - 2026-05-08

## Reflection

Att implementera `Find book by ID` tog längre tid än jag förväntade mig. Egentligen kunde jag ha lagt mindre tid på det, men jag ville att respons datan skulle följa API specifikationen för att testerna skulle passera. Det som tog lång tid var att hämta ID:n till relaterade resurser, authors, categories, etc.

Kanske jag ska lägga mindre vikt på att respons datan har rätt struktur? Det finns flera endpoints kvar att implementera, så det kan vara bra att ignorera tester som inte går igenom, så länge APIet inte kraschar. Att responsen har exakt rätt struktur kan vara något jag fokuserar på efter de flesta features har blivit implementerade.

Jag började med en CI/CD pipeline. Det enda den gör just nu är att kolla att docker containers fungerar. Men det uppstår error när jag försöker använda docker, så jag behöver fixa det.

Jag behöver exportera mina API tester från Apidog så att andra ska kunna testa APIet. Att ha Swagger UI skulle också underlätta.

Här är APIet driftsatt: [https://patriciaj.se/bibliocat-api/api/v1/](https://patriciaj.se/bibliocat-api/api/v1/)

**Carries over to Iteration 7:** GET books using query parameters.

## Goals this iteration

- Applikationen ska levereras?
- GET `books` endpoint
- CI/CD

## Time summary

| Label | Issues | Estimated (h) | Actual (h) |
|---|---|---|---|
| `development` | [#36], [#41], [#51], [#52], [#61], [#62], [#64] | 14 | 23h 50m |
| `documentation` | [#54], [#55], [#56], [#63] | 5 | 2h 50m |
| `learning` | [#57], [#58] | - | 5h 45m |
| `meeting` | [#59], [#60] | 4 | 4h 30m |
| | **Total** | 17 | 36h 55m |
| | **Total project** |  | 115 |

### Issues

| Issue | Title | Estimated (h) | Actual (h) |
|---|---|---|---|
| [#36] | User Story: Search for books | 4 | 1h 5m |
| [#41] | CI/CD | 4 | 4 |
| [#51] | Installera docker på produktionsservern | 1 | 1 |
| [#52] | Installera och konfigurera Gunicorn | 1 | 30m |
| [#54] | Reflektion Iteration 6 | 1 | 30m |
| [#55] | Planera Iteration 7 | 1 | 1 |
| [#56] | Testrapport Iteration 6 | 1 | 20m |
| [#57] | Teori Iteration 6 | 3 | 3h 45m |
| [#58] | Teori: CI/CD | 2 | 2 |
| [#59] | Examination av vecka 5 | 1 | 1 |
| [#60] | Grupparbete vecka 6 | 3h 30m | 3 |
| [#61] | Konfigurera Nginx och Cloudflare | 0 | 3 |
| [#62] | Fixa Nginx request path till APIet | 0 | 3h 30m |
| [#63] | Exportera API specifikation | 2 | 1 |
| [#64] | User Story: Find book by ID | 4 | 10h 45m |

[#36]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/36
[#41]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/41
[#51]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/51
[#52]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/52
[#54]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/54
[#55]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/55
[#56]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/56
[#57]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/57
[#58]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/58
[#59]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/59
[#60]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/60
[#61]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/61
[#62]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/62
[#63]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/63
[#64]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/64
