# Iteration 3

**Milestone:** [Iteration 3](https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/milestones/2)  
**Period:** 2026-04-11 - 2026-04-17

## Reflection

Jag gjorde ett setup script som laddade böcker in i databasen. Just nu har jag bara böcker i databasen, men jag behöver vidareutveckla databasmodellen så att andra bibliografiska objekt kan läggas till. Det ska också sparas användarinformation i databasen.

Jag hade problem med att få igång produktions servern. Jag tänker använda en egen raspberry pi som server. Eftersom den ska sitta på mitt hemnätverk behöver jag ändra några inställningar. Men när jag försökte göra det blev det något konfigurationsfel, så jag fick återställa nätverket till en tidigare säkerhetskopia. Detta innebar att jag inte hade internetåtkomst i ca 2 timmar, så jag fick skjuta upp en del saker den dagen.

Vissa av kraven har inte så mycket information än, så jag får utveckla dem mer. Det behövs nog läggas till icke-funktionella krav, tex. krav på att APIet ska testas.  
För att testa APIet tänker jag använda Apidog.

**Går över till Iteration 4:** Att få igång APIet på produktionsservern.

## Goals this iteration

- Lägg till krav på nödvändig funktionalitet.
- Konfigurera databas och utvecklingsmiljön för huvudappen.
- Skapa testmiljö i Postman.
- Konfigurera produktionsservern.
- Huvudappen ska gå att starta.

## Time summary

### By category

| Label | Issues | Estimated (h) | Actual (h) |
|---|---|---|---|
| `development` | [#12], [#15] | 14 | 12h 30m |
| `documentation` | [#13], [#14] | 2 | 3h 40m |
| `learning` |  | - | 1 |
| `meeting` | [#23], [#24] | - | 4 |
| | **Total** | 16 | 20h 10m |
| | **Total project** | | 33 |

### Issues

| Issue | Title | Estimated (h) | Actual (h) |
|---|---|---|---|
| [#12] | Set up database |  | 8h 30m |
| [#13] | Set up test environment |  | 1 |
| [#14] | Specify requirements |  | 2h 40m |
| [#15] | Set up production server |  | 4 |
| [#23] | Grupparbete vecka 3 |  | 3 |
| [#14] | Examination |  | 1 |

[#12]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/12
[#13]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/13
[#14]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/14
[#15]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/15
[#23]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/23
[#24]: https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/issues/24
