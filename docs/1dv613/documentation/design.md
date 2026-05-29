# Design

## User personas

*Who exactly are you building for? One persona is enough for a solo project.*

**Persona: Maja**
- **Age / background:** 40 / Developer
- **Goal:** Build a frontend for the library application.
- **Frustration:** The API needs to be documented so the frontend team can develop the client-side code.
- **Uses the API to:** Send requests from the client-side app.

<details>
<summary>Persona template</summary>
**Persona: [Name]**
- **Age / background:**
- **Goal:** What do they want to achieve?
- **Frustration:** What problem are they facing today?
- **Uses the app to:**
</details>

## User flows

**Flow 1 - book search:**
1. User enters the URL for the `books` endpoint, and a filter. Example: `books?category=philosophy`
2. User runs the request.
3. System responds with a status and a list of books that matches the search criteria.

**Flow 2 - find book by id:**
1. User enters the URL for the `books` endpoint, and the book ID. Example: `books/2`
2. User runs the request.
3. System responds with a status and the book data if it is found.

**Flow 3 - create account:**
1. User enters the URL for the `users/register` endpoint. In the request body, the user enters a username, email and password.
2. User runs the request.
3. System responds with a status describing how the action went, the user id, username and email.

**Flow 4 - log in:**
1. User enters the URL for the `users/login` endpoint. In the request body, the user enters their username and password.
2. User runs the request.
3. System responds with a status describing how the action went, and a JWT if the user was successfully logged in.

**Flow 5 - checkout book:**
1. User logs in and receives a JWT.
2. User enters the URL for the `checkouts` endpoint. In the request body, the user enters the book id.
3. User runs the request.
4. System responds with a status describing how the action went, and with a return date if the checkout was successful.

**Flow 6 - create reading log:**
1. User logs in and receives a JWT.
2. User enters the URL for the `reading-logs` endpoint. In the request body, the user enters the book id, the start date and end date.
3. User runs the request.
4. System responds with a status describing how the action went.

**Flow 7 - review book:**
1. User logs in and receives a JWT.
2. User enters the URL for the `reviews` endpoint. In the request body, the user enters the book id, the rating (integer) and a written review (optional, nullable).
3. User runs the request.
4. System responds with a status describing how the action went.

<details>
<summary>User flow template</summary>
**Flow - [feature]**
1. User enters the URL ...
2. User runs the request.
3. System responds with ...
</details>

Features:
- book search
- find book by id
- create account
- login
- checkout books
- reading logs
- review books

## Design decisions

*Any notable UX choices worth explaining? E.g. why a certain layout, navigation pattern, or interaction.*

-
