# Iteration 7

**Milestone:** [Iteration 7](https://gitlab.lnu.se/1dv613/student/pj222uc/project-hub/-/milestones/6)  
**Project Iteration:** [Iteration 7](https://gitlab.lnu.se/groups/1dv613/student/pj222uc/workspace/-/cadences/59/iterations/574)  
**Period:** 2026-05-09 - 2026-05-15

## Reflection

Det tog lång tid att fixa CI/CD pipeline, så det har inte lagts till så mycket i projektet den här iterationen.

Eftersom min host server är på mitt hemnätverk, och den har brandväggsinställningar som blockerar ssh anslutningar utanför nätverket, var det svårt att få GitLab runnern att ansluta till servern. Om jag hade försökt att använda de existerande runners som finns på skolans GitLab instans, skulle jag behöva få dem att ansluta till ett VPN till mitt nätverk.

Den enklaste lösningen var att ha en runner på samma nätverk som host servern. Därför installerade jag GitLab Runner på host servern. Jag skapade en runner i BiblioCat API projektet och registrerade den på host servern med en runner authentication token.

Det har fungerat bra än så länge. En fördel är att jag inte behöver vara ansluten till hemnätverket eller ansluta via VPN för att driftsätta projektet.

Swagger UI fungerar nu. Jag exporterade dokumentationen från Apidog och använde ett plugin för att Swagger UI skulle användas. Jag hade lite problem med att paketet skulle använda rätt sökväg till JSON dokumentationen och med nginx routing. Men det är löst nu.

**Carries over to Iteration 8:** Reading logs endpoint (#76, #78, #79)

## Goals this iteration

- GET books med query parametrar
- CI: kolla att docker containers fungerar
- Användare ska kunna skapa reading logs

## Time summary

| Label | Issues | Estimated (h) | Actual (h) |
|---|---|---|---|
| `development` | #66, #67, #75, #77, #78, #81, #82, #84, #85. #86, #87, #88, #89, #90 | 31 | 30h 25m |
| `documentation` | #69, #70, #71, #74, #76, #79, #93 | 6h 30m | 5h 15m |
| `learning` | #91 | - | 1 |
| `meeting` | #72, #73 | 4 | 4 |
| | **Total** | 39h 30m | 40h 40m |
| | **Total project** | | 156 |
