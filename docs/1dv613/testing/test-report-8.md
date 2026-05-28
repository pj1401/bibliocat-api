**Date:** 2026-05-22  
**Version:** v0.5.0-19-g07216ec  
**Test environment:** Testing Env, CI/CD, Apidog CLI, pytest

## Results

| Test | Result | Comment |
|---|---|---|
| TC1.1 | ✅ Pass / ❌ Fail | |
| TC1.2 | ✅ Pass / ❌ Fail | |

## Automated test coverage

**Output:**

*Screenshot or output from your test runner.*

```
❏ collection
↳ health (API is running)
  GET http://localhost:5001/api/v1/health [200 OK, 184B, 84.00ms]
  ✓  Correct HTTP Code
↳ Swagger UI (Swagger UI is accessible)
  GET http://localhost:5001/api/v1/docs [200 OK, 1.62KB, 45.00ms]
  ✓  Correct HTTP Code
┌─────────────────────────┬─────────────────────────┬───────────────────────┐
│                         │                Executed │                Failed │
├─────────────────────────┼─────────────────────────┼───────────────────────┤
│              Iterations │                       1 │                     0 │
├─────────────────────────┼─────────────────────────┼───────────────────────┤
│           Http Requests │                       2 │                     0 │
├─────────────────────────┼─────────────────────────┼───────────────────────┤
│              Assertions │                       2 │                     0 │
├─────────────────────────┴─────────────────────────┴───────────────────────┤
│ Duration: 560.00ms                                                        │
├───────────────────────────────────────────────────────────────────────────┤
│ Total Response Size: 1.51KB (approx)                                      │
├───────────────────────────────────────────────────────────────────────────┤
│ Average Request Time: 43.50ms [min: 45.00ms, max: 84.00ms, s.d.: 29.74ms] │
└───────────────────────────────────────────────────────────────────────────┘

❏ auth
↳ register (register success)
  POST http://localhost:5001/api/v1/users/register [201 CREATED, 251B, 783.00ms]
  ┌
  │ Processor 'The value of the Environment variable usern
  │ ame has been set to Kolby10'
  └
↳ register (register failure duplicate)
  POST http://localhost:5001/api/v1/users/register [400 BAD REQUEST, 323B, 419.00ms]
↳ login (login failure wrong password)
  POST http://localhost:5001/api/v1/users/login [401 UNAUTHORIZED, 228B, 422.00ms]
↳ login (login success)
  POST http://localhost:5001/api/v1/users/login [200 OK, 702B, 533.00ms]
  ✓  Access token exists
┌─────────────────────────┬───────────────────────────┬─────────────────────────┐
│                         │                  Executed │                  Failed │
├─────────────────────────┼───────────────────────────┼─────────────────────────┤
│              Iterations │                         1 │                       0 │
├─────────────────────────┼───────────────────────────┼─────────────────────────┤
│           Http Requests │                         4 │                       0 │
├─────────────────────────┼───────────────────────────┼─────────────────────────┤
│              Assertions │                         1 │                       0 │
├─────────────────────────┴───────────────────────────┴─────────────────────────┤
│ Duration: 4.06s                                                               │
├───────────────────────────────────────────────────────────────────────────────┤
│ Total Response Size: 897B (approx)                                            │
├───────────────────────────────────────────────────────────────────────────────┤
│ Average Request Time: 353.88ms [min: 419.00ms, max: 783.00ms, s.d.: 261.79ms] │
└───────────────────────────────────────────────────────────────────────────────┘

❏ books
↳ Find book by ID (Not found)
  GET http://localhost:5001/api/v1/books/0 [404 NOT FOUND, 226B, 94.00ms]
↳ Find book by ID (Success)
  GET http://localhost:5001/api/v1/books/159 [200 OK, 1.4KB, 56.00ms]
↳ Find books (Find books by author_id)
  GET http://localhost:5001/api/v1/books?author_id=132 [200 OK, 4.6KB, 68.00ms]
  ✓  Correct HTTP code
  ✓  Target object has correct author ID
↳ Find books (Empty list, offset exceeds number of records)
  GET http://localhost:5001/api/v1/books?limit=20&offset=1000000000 [200 OK, 179B, 21.00ms]
  ✓  Data list is empty
↳ Find books (Failure (value not following constraint))
  GET http://localhost:5001/api/v1/books?limit=999 [400 BAD REQUEST, 323B, 16.00ms]
  ✓  Correct status code
↳ Find books (Success (Find 5 books))
  GET http://localhost:5001/api/v1/books?limit=5&offset=4&category=fiction [200 OK, 14.78KB, 78.00ms]
  ✓  Correct status code
  ✓  The number of returned objects is the same as limit
┌─────────────────────────┬─────────────────────────┬───────────────────────┐
│                         │                Executed │                Failed │
├─────────────────────────┼─────────────────────────┼───────────────────────┤
│              Iterations │                       1 │                     0 │
├─────────────────────────┼─────────────────────────┼───────────────────────┤
│           Http Requests │                       6 │                     0 │
├─────────────────────────┼─────────────────────────┼───────────────────────┤
│              Assertions │                       6 │                     0 │
├─────────────────────────┴─────────────────────────┴───────────────────────┤
│ Duration: 2.41s                                                           │
├───────────────────────────────────────────────────────────────────────────┤
│ Total Response Size: 20.62KB (approx)                                     │
├───────────────────────────────────────────────────────────────────────────┤
│ Average Request Time: 35.01ms [min: 16.00ms, max: 94.00ms, s.d.: 34.13ms] │
└───────────────────────────────────────────────────────────────────────────┘

❏ authors
↳ Find author by ID (Success)
  GET http://localhost:5001/api/v1/authors/132 [200 OK, 443B, 102.00ms]
  ✓  Correct HTTP code
↳ Find author by ID (Not Found)
  GET http://localhost:5001/api/v1/authors/0 [404 NOT FOUND, 226B, 42.00ms]
  ✓  Correct HTTP code
↳ Filter authors (Limit parameter exceeds max value (Failure))
  GET http://localhost:5001/api/v1/authors?limit=999 [400 BAD REQUEST, 323B, 16.00ms]
↳ Filter authors (Find 5 authors (Success))
  GET http://localhost:5001/api/v1/authors?limit=5&offset=5 [200 OK, 1.58KB, 88.00ms]
  ✓  The number of returned objects
↳ Filter authors (Filter by name)
  GET http://localhost:5001/api/v1/authors?limit=5&name=mar [200 OK, 1.6KB, 39.00ms]
  ✓  Name contains the value from the query parameter
┌─────────────────────────┬──────────────────────────┬───────────────────────┐
│                         │                 Executed │                Failed │
├─────────────────────────┼──────────────────────────┼───────────────────────┤
│              Iterations │                        1 │                     0 │
├─────────────────────────┼──────────────────────────┼───────────────────────┤
│           Http Requests │                        5 │                     0 │
├─────────────────────────┼──────────────────────────┼───────────────────────┤
│              Assertions │                        4 │                     0 │
├─────────────────────────┴──────────────────────────┴───────────────────────┤
│ Duration: 912.00ms                                                         │
├────────────────────────────────────────────────────────────────────────────┤
│ Total Response Size: 3.42KB (approx)                                       │
├────────────────────────────────────────────────────────────────────────────┤
│ Average Request Time: 36.58ms [min: 16.00ms, max: 102.00ms, s.d.: 35.64ms] │
└────────────────────────────────────────────────────────────────────────────┘

❏ reading-logs
↳ register (register success)
  POST http://localhost:5001/api/v1/users/register [201 CREATED, 263B, 493.00ms]
  ┌
  │ Processor 'The value of the Environment variable usern
  │ ame has been set to Josiane_Grant-Cummerata'
  └
↳ login (login success)
  POST http://localhost:5001/api/v1/users/login [200 OK, 724B, 466.00ms]
  ✓  Access token exists
  ┌
  │ Processor 'The value of the Environment variable acces
  │ s_token has been set to eyJhbGciOiJFUzUxMiIsInR5cCI6Ik
  │ pXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc3OTQ2NDY0MSwianR
  │ pIjoiODc5YmExYTktMzI3NS00MzVjLThjMzctYzk1NGE2ZDgyOTdjI
  │ iwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjMiLCJuYmYiOjE3Nzk0NjQ
  │ 2NDEsImNzcmYiOiIyYjY4ZjY4Yy1lZjA2LTRmZjAtOWU1NC00OTg1O
  │ TgwM2ExY2EiLCJleHAiOjE3Nzk0NjgyNDEsInVzZXJuYW1lIjoiSm9
  │ zaWFuZV9HcmFudC1DdW1tZXJhdGEiLCJwZXJtaXNzaW9uX2xldmVsI
  │ jowfQ.AUpsVNntm-xpMVgd2DfSqqgbKLq8Gy9HEJVlGe9naPryYAsP
  │ oospLgNg2_FBwo595n8Lmf_kaP0ueBKbuApElizoAQwkq5yKilywaW
  │ 0n_WzejA8OA-nYQ2MnCUrn91OD9ogsE-jAbwJ-o4TZxenCGUX7o3Kp
  │ vEeuQoql1i8k9TbZ31Ay'
  └
↳ Create Reading log (No auth (Failure))
  POST http://localhost:5001/api/v1/reading-logs [401 UNAUTHORIZED, 228B, 24.00ms]
  ✓  Unauthorized HTTP code
↳ Create Reading log (Validation Error (Failure))
  POST http://localhost:5001/api/v1/reading-logs [400 BAD REQUEST, 323B, 19.00ms]
  ✓  Bad Request HTTP Code
↳ Create Reading log (Create Reading Log (Success))
  POST http://localhost:5001/api/v1/reading-logs [201 CREATED, 599B, 70.00ms]
  ┌
  │ Processor 'The value of the Environment variable readi
  │ ng_log_id has been set to 1'
  └
↳ Find reading log by ID (No auth (Failure))
  GET http://localhost:5001/api/v1/reading-logs/1 [401 UNAUTHORIZED, 228B, 14.00ms]
  ✓  Correct HTTP Code
↳ Find reading log by ID (Find by ID (Success))
  GET http://localhost:5001/api/v1/reading-logs/1 [200 OK, 638B, 28.00ms]
  ✓  ID matches
┌─────────────────────────┬──────────────────────────┬────────────────────────┐
│                         │                 Executed │                 Failed │
├─────────────────────────┼──────────────────────────┼────────────────────────┤
│              Iterations │                        1 │                      0 │
├─────────────────────────┼──────────────────────────┼────────────────────────┤
│           Http Requests │                        7 │                      0 │
├─────────────────────────┼──────────────────────────┼────────────────────────┤
│              Assertions │                        5 │                      0 │
├─────────────────────────┴──────────────────────────┴────────────────────────┤
│ Duration: 3.50s                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ Total Response Size: 1.9KB (approx)                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│ Average Request Time: 75.35ms [min: 14.00ms, max: 493.00ms, s.d.: 152.22ms] │
└─────────────────────────────────────────────────────────────────────────────┘
```

**pytest:**

Job logs:

```
$ uv run pytest
============================= test session starts ==============================
platform linux -- Python 3.12.12, pytest-9.0.3, pluggy-1.6.0
rootdir: /builds/1dv613/student/pj222uc/workspace/bibliocat-api/api
configfile: pyproject.toml
testpaths: tests
plugins: typeguard-4.5.1
collected 5 items
tests/test_book_controller.py ..                                         [ 40%]
tests/test_reading_log_controller.py ...                                 [100%]
- generated xml file: /builds/1dv613/student/pj222uc/workspace/bibliocat-api/api/test-reports/junit.xml -
============================== 5 passed in 3.52s ===============================
```

JUnitXML:

```xml
<?xml version="1.0" encoding="utf-8"?>
<testsuites name="pytest tests"><testsuite name="pytest" errors="0" failures="0" skipped="0" tests="5" time="3.524" timestamp="2026-05-22T15:42:29.693889+00:00" hostname="runner-6mynever-project-59522-concurrent-0">
<testcase classname="tests.test_book_controller.TestGetParams" name="test_returns_book_query_params" time="0.013" />
<testcase classname="tests.test_book_controller.TestGetParams" name="test_raises_validation_error" time="0.016" />
<testcase classname="tests.test_reading_log_controller.TestGetValidatedArguments" name="test_returns_reading_log_params" time="0.017" />
<testcase classname="tests.test_reading_log_controller.TestGetValidatedArguments" name="test_raises_validation_error_on_missing_field" time="0.017" />
<testcase classname="tests.test_reading_log_controller.TestGetValidatedArguments" name="test_raises_validation_error_on_invalid_field" time="0.019" />
</testsuite></testsuites>
```

## Findings & improvements

Formatera output från automatiska tester?
