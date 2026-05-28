## System overview

*One paragraph: what does the system do and how do the main parts connect?*

Library App är en server side rendering app. Den har ett internt API som kommunicerar med databasen. JSON datan från API:et används för att rendera HTML sidor.

## Diagram

*Add a diagram showing your components (frontend, backend, database, external APIs).
Use [Excalidraw](https://excalidraw.com), [draw.io](https://draw.io), or any tool - paste a screenshot or link here.*

![architecture-v2026-04-22](uploads/77472cbe1dd2cb67ae59ca663b7a0448/architecture-v2026-04-22.jpg){width=420 height=199}
![library-er-diagram-v2026-04-22](uploads/62bbf068657769cef80727ea9d726af2/library-er-diagram-v2026-04-22.jpg){width=641 height=600}

**ER in Mermaid:**
```mermaid
classDiagram
    class Book {
        +id: int
        +title: str
        +isbn: str
        +published_date: date
    }
    class Category {
        +id: int
        +name: str
    }
    class Author {
        +id: int
        +name: str
    }
    class BookCopy {
        +id: int
        +status: str
    }
    class Checkout {
        +id: int
        +start_date: date
        +return_date: date
    }
    class User {
        +id: int
        +username: str
        +email: str
        +password: str
        +permission_level: int
    }
    class Review {
        +id: int
        +rating: int
        +description: str
    }
    class ReadingLog {
        +id: int
        +start_date: date
        +end_date: date
    }
    Book "1..*" -- "1..*" Category : Belongs to
    Book "1..*" -- "1..*" Author : Written by
    Book "1" -- "1..*" BookCopy
    BookCopy "1" -- "0..*" Checkout
    User "1" -- "0..*" Checkout
    User "1" -- "0..*" Review : Writes
    User "1" -- "0..*" ReadingLog : Adds
    User "0..*" -- "0..*" BookCopy : Borrows
    Book "1" -- "0..*" Review
    Book "1" -- "0..*" ReadingLog

```

## Components

| Component | Responsibility | Technology |
|---|---|---|
| Library API | | Python, Flask |
| Database | | PostgreSQL |
| Server | Deployment | Docker, Nginx, Cloudflare |

## Key decisions

*Why did you pick the tech you picked? One line per decision is enough.*

- **Why Flask:** Jag har använt det förut och jag tycker det är lätt att använda.
- **Why PostgreSQL:** Jag tyckte att en relationsbaserad databas skulle passa bra.
- **Why Docker:** Det är lätt att starta APIet på servern med docker compose.
- **Why Cloudflare:** Servern är på mitt hemnätverk. Trafiken går igenom Cloudflare tunneln innan det går till servern.
