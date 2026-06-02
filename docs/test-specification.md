# Test Specification

## Test plan

| Aspect | Description |
|---|---|
| Testing tools | API: Apidog, unit tests: pytest |
| Automated testing | Yes: pytest and Apidog CLI in GitHub Actions |
| Manual testing | Yes |
| Untested parts | Could add more unit tests using `pytest` for more coverage. |

## Test suites

### Manual tests

[GitHub Project Manual tests view](https://github.com/users/pj1401/projects/2/views/5)

The instructions for the manual tests are in the issue descriptions.

| ID | Title | Issue link | Requirement(s) |
| -- | ----- | ---------- | -------------- |
| TC-NFR3.1 | API health check | [#14] | [#10] |
| TC4.1 | Register via Swagger UI | [#15] | [#7], [#8] |
| TC4.2 | Login via Swagger UI | [#16] | [#7], [#8] |
| TC5.1 | Create a reading log via Swagger UI | [#17] | [#7], [#8], [#12] |
| TC-FR1.1 | Delete user via Swagger UI | [#22] | [#7], [#8], [#13] |

Coverage matrix - which requirements does each test cover?

| Test | BR-1 | BR-2 | BR-3 | BR-4 | BR-5 | NFR-1 | NFR-3 | FR-1 |
|---|---|---|---|---|---|---|---|---|
| TC-NFR3.1 |  |  |  |  |  |  | ✓ |  |
| TC4.1 |  |  |  | ✓ |  | ✓ |  |  |
| TC4.2 |  |  |  | ✓ |  | ✓ |  |  |
| TC5.1 |  |  |  | ✓ | ✓ | ✓ |  |  |
| TC-FR1.1 |  |  |  | ✓ |  | ✓ |  | ✓ |
| **Coverage** |  | | | 4 cases | 1 | 4 | 1 | 1 |

---

### Automatic tests

Instructions for running tests: [tests/README](../tests/README.md)

**Coverage matrix for API tests**

| Test scenario | BR-1 | BR-2 | BR-3 | BR-4 | BR-5 | FR-1 |
| ------------- | ---- | ---- | ---- | ---- | ---- | ---- |
| Auth |  |  |  | ✓ |  | ✓ |
| Books | ✓ |  |  |  |  |  |
| Authors | ✓ |  |  |  |  |  |
| Reading logs |  |  |  | ✓ | ✓ | ✓ |

---

Test step name format: `HTTP method` `Endpoint title` (`test case title`)

**Auth API tests:**

Requirements:
- BR-4 Users should have the ability to create and manage an account
- FR-1 Users should have the ability to delete their user information

<img src="./img/api-tests-auth.png" alt="Auth API test steps" width="500">

**Books API tests:**

Requirements:
- BR-1 Users should have the ability to search for books

<img src="./img/api-tests-books.png" alt="Books API test steps" width="500">

**Authors API tests:**

Requirements:
- BR-1 Users should have the ability to search for books

<img src="./img/api-tests-authors.png" alt="Authors API test steps" width="500">

**Reading logs API tests:**

Requirements:
- BR-4 Users should have the ability to create and manage an account
- BR-5 Users should have the ability to keep track of read books
- FR-1 Users should have the ability to delete their user information

<img src="./img/api-tests-reading-logs.png" alt="Reading logs API test steps" width="500">

[#7]: https://github.com/pj1401/bibliocat-api/issues/7
[#8]: https://github.com/pj1401/bibliocat-api/issues/8
[#10]: https://github.com/pj1401/bibliocat-api/issues/10
[#12]: https://github.com/pj1401/bibliocat-api/issues/12
[#13]: https://github.com/pj1401/bibliocat-api/issues/13
[#14]: https://github.com/pj1401/bibliocat-api/issues/14
[#15]: https://github.com/pj1401/bibliocat-api/issues/15
[#16]: https://github.com/pj1401/bibliocat-api/issues/16
[#17]: https://github.com/pj1401/bibliocat-api/issues/17
[#22]: https://github.com/pj1401/bibliocat-api/issues/22
