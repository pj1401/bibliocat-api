# Iteration 5

**Milestone:** [Iteration 5](https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/milestones/4)  
**Project Iteration:** [Iteration 5](https://gitlab.lnu.se/groups/1dv613/student/pj222uc/workspace/-/cadences/59/iterations/572)  
**Period:** 2026-04-25 - 2026-05-01

## Reflection

*What went well? What didn't? What carries over to next iteration?*

Jag håller fortfarande på att försöka driftsätta projektet. Eftersom jag använder en egen server har det inte varit helt enkelt att ta reda på hur jag ska göra. Först tänkte jag att jag skulle använda öppna portar och göra port forwarding till servern, men det finns en del säkerhetsrisker med det, så jag ändrade till att använda Cloudflare tunnel.

Jag hade kunnat dela upp driftsättningen i fler delar. Till exempel: Konfigurera server, ladda upp projektet, installera docker, konfigurera gunicorn, etc. Men jag har inte provat att driftsätta med den här tech stacken innan, så jag visste inte att det skulle bli så många steg.

Eftersom det gick mer tid till att konfigurera servern än vad jag planerat, har jag inte hunnit göra så mycket annat den här iterationen. Jag började göra API specifikation och tester till `books` endpoints, men själva implementationen för göras nästa iteration.

Jag fixade API anslutnings problemet när den körs i en container, så nu kan docker-compose användas för att köra APIet.

**Carries over to Iteration 6:** [#36] GET `books` endpoints, [#41] CI/CD

## Goals this iteration

- CI/CD
- Driftsättning
- GET `books` endpoints

## Time summary

### By category

| Label | Issues | Estimated (h) | Actual (h) |
|---|---|---|---|
| `development` | [#30], [#36], [#41], [#53] | 13 | 8 |
| `documentation` | [#42], [#43], [#47], [#48], [#50] | 5 | 5h 30m |
| `learning` | [#44], [#49] | - | 3h 30m |
| `meeting` | [#45], [#46] | - | 2 |
| | **Total** | 16 | 19 |
| | **Total project** | | 78 |

### Issues

| Issue | Title | Estimated (h) | Actual (h) |
|---|---|---|---|
| [#30] | Få igång APIet på produktionsservern | 4 | 6 |
| [#36] | User Story: Search for books (Flyttad till Iteration 6) | 4 | 0 |
| [#41] | CI/CD (Flyttad till Iteration 6) | 4 | 0 |
| [#42] | Reflektion Iteration 5 | 1 | 1 |
| [#43] | Planera Iteration 6 | 2 | 30m |
| [#44] | Teori Iteration 5 | 3 | 1h 30m |
| [#45] | Examination av vecka 4 | 1 | 1 |
| [#46] | Grupparbete vecka 5 | 2 | 1 |
| [#47] | Testrapport Iteration 5 | 1 | 1 |
| [#48] | Lägg till filstruktur | 0 | 1 |
| [#49] | Praktisk övning (vecka 5) | 2 | 2 |
| [#50] | Search books API specification | 1 | 2 |
| [#53] | Fixa API docker container port | 1 | 2 |

[#30]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/30
[#36]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/36
[#41]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/41
[#42]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/42
[#43]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/43
[#44]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/44
[#45]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/45
[#46]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/46
[#47]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/47
[#48]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/48
[#49]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/49
[#50]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/50
[#53]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/53
