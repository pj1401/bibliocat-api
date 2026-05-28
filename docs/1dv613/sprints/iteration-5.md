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

**Carries over to Iteration 6:** GET `books` endpoints, CI/CD

## Goals this iteration

- CI/CD
- Driftsättning
- GET `books` endpoints

## Time summary

| Label | Issues | Estimated (h) | Actual (h) |
|---|---|---|---|
| `development` | #30, #36, #41 | 12 | 8 |
| `documentation` | #42, #43, #47 | 4 | 5h 30m |
| `learning` | #44 | - | 3h 30m |
| `meeting` | #45, #46 | - | 2 |
| | **Total** | 16 | 19 |
| | **Total project** | | 78 |
