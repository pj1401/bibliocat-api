# Test Report 7

**Date:** 2026-05-14  
**Version:** 0.4.0-60-ga852cfc  
**Test environment:** Testing Env, CI/CD, Apidog exported test scenarios

## Results

| Test | Result | Comment |
|---|---|---|
| TC1.1 | ❌ Fail | Query parameters not implemented |
| TC1.2 | ❌ Fail | Query parameters not implemented |
| TC1.3 | ✅ Pass |  |
| TC1.4 | ✅ Pass |  |
| TC4.1 | ✅ Pass |  |
| TC4.2 | ✅ Pass |  |
| TC4.3 | ✅ Pass |
| TC4.4 | ✅ Pass |  |

## Automated test coverage

**Output:**

```
❏ collection
↳ health (API is running)
  GET http://localhost:5001/api/v1/health [200 OK, 184B, 90.00ms]
↳ Swagger UI (Swagger UI is accessible)
  GET http://localhost:5001/api/v1/docs [200 OK, 1.6KB, 45.00ms]
┌─────────────────────────┬─────────────────────────┬───────────────────────┐
│                         │                Executed │                Failed │
├─────────────────────────┼─────────────────────────┼───────────────────────┤
│              Iterations │                       1 │                     0 │
├─────────────────────────┼─────────────────────────┼───────────────────────┤
│           Http Requests │                       2 │                     0 │
├─────────────────────────┼─────────────────────────┼───────────────────────┤
│              Assertions │                       0 │                     0 │
├─────────────────────────┴─────────────────────────┴───────────────────────┤
│ Duration: 350.00ms                                                        │
├───────────────────────────────────────────────────────────────────────────┤
│ Total Response Size: 1.48KB (approx)                                      │
├───────────────────────────────────────────────────────────────────────────┤
│ Average Request Time: 45.00ms [min: 45.00ms, max: 90.00ms, s.d.: 31.82ms] │
└───────────────────────────────────────────────────────────────────────────┘

❏ auth
↳ register (register success)
  POST http://localhost:5001/api/v1/users/register [201 CREATED, 240B, 772.00ms]
  ┌
  │ Processor 'The value of the Environment variable usern
  │ ame has been set to Dawn56'
  └
↳ register (register failure duplicate)
  POST http://localhost:5001/api/v1/users/register [400 BAD REQUEST, 323B, 419.00ms]
↳ login (login failure wrong password)
  POST http://localhost:5001/api/v1/users/login [401 UNAUTHORIZED, 228B, 439.00ms]
↳ login (login success)
  POST http://localhost:5001/api/v1/users/login [200 OK, 714B, 517.00ms]
┌─────────────────────────┬───────────────────────────┬─────────────────────────┐
│                         │                  Executed │                  Failed │
├─────────────────────────┼───────────────────────────┼─────────────────────────┤
│              Iterations │                         1 │                       0 │
├─────────────────────────┼───────────────────────────┼─────────────────────────┤
│           Http Requests │                         4 │                       0 │
├─────────────────────────┼───────────────────────────┼─────────────────────────┤
│              Assertions │                         0 │                       0 │
├─────────────────────────┴───────────────────────────┴─────────────────────────┤
│ Duration: 3.93s                                                               │
├───────────────────────────────────────────────────────────────────────────────┤
│ Total Response Size: 899B (approx)                                            │
├───────────────────────────────────────────────────────────────────────────────┤
│ Average Request Time: 351.91ms [min: 419.00ms, max: 772.00ms, s.d.: 258.20ms] │
└───────────────────────────────────────────────────────────────────────────────┘

❏ books
↳ Find book by ID (Not found)
  GET http://localhost:5001/api/v1/books/0 [404 NOT FOUND, 226B, 104.00ms]
↳ Find book by ID (Success)
  GET http://localhost:5001/api/v1/books/159 [200 OK, 1.35KB, 84.00ms]
┌─────────────────────────┬──────────────────────────┬───────────────────────┐
│                         │                 Executed │                Failed │
├─────────────────────────┼──────────────────────────┼───────────────────────┤
│              Iterations │                        1 │                     0 │
├─────────────────────────┼──────────────────────────┼───────────────────────┤
│           Http Requests │                        2 │                     0 │
├─────────────────────────┼──────────────────────────┼───────────────────────┤
│              Assertions │                        0 │                     0 │
├─────────────────────────┴──────────────────────────┴───────────────────────┤
│ Duration: 453.00ms                                                         │
├────────────────────────────────────────────────────────────────────────────┤
│ Total Response Size: 1.28KB (approx)                                       │
├────────────────────────────────────────────────────────────────────────────┤
│ Average Request Time: 68.00ms [min: 84.00ms, max: 104.00ms, s.d.: 40.10ms] │
└────────────────────────────────────────────────────────────────────────────┘
```

## Findings & improvements

*Bugs found, what needs fixing, overall feel of the system at this stage.*
