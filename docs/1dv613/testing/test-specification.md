# Test Specification

## Traceability

Test cases are derived from requirements, which are derived from user flows:

```
UF-1 Books search        (Design)
  └─ BR-1 Search for books   (Requirements)
       ├─ TC1.1 Success, get an array of books
       └─ TC1.2 Failure, invalid search parameters
UF-2 Find book by ID
  └─ BR-1 Search for books
       ├─ TC1.3 Success, find book by ID
       └─ TC1.4 Failure, not found
UF-3 Register an account
  └─ BR-4 User authentication
       ├─ TC4.1 Successful registration
       └─ TC4.2 Duplicate username rejected
UF-4 Log in
  └─ BR-4 User authentication
       ├─ TC4.1 Successful registration
       ├─ TC4.4 Login failure, wrong password
       └─ TC4.3 Login success
```

A user flow describes *what the user does*. A requirement formalises *what the system must support*. A test case verifies *that it actually works* with specific input and expected output.

---

## Test plan

*Brief description of your testing strategy - what will be tested, how, and with what tools.*

| Aspect | Description |
|---|---|
| Testing tools | API: Apidog |
| Automated testing | Yes: Apidog, Gitlab CI/CD (planned) |
| Manual testing | No |
| Untested parts | Could add unit tests using `pytest` for more coverage. |

## Test suites

**Regression Test**
- register duplicate
  1. TC4.1
  2. TC4.2
- log in with wrong password
  1. TC4.1
  2. TC4.4
- register and log in
  1. TC4.1
  2. TC4.3
- TC1.1
- TC1.2
- TC1.3
- TC1.4

Coverage matrix - which requirements does each test cover?

| Test | BR-1 | BR-2 | BR-3 | BR-4 |
|---|---|---|---|---|
| TC1.1 | ✓ | | |  |
| TC1.2 | ✓ | | |  |
| TC1.3 | ✓ | | |  |
| TC1.4 | ✓ | | |  |
| TC4.1 |  | | | ✓ |
| TC4.2 |  | | | ✓ |
| TC4.3 |  | | | ✓ |
| TC4.4 |  | | | ✓ |
| **Coverage** | 4 | | | 4 cases |

## Test cases

