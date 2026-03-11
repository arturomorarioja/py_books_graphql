# Books
GraphQL server and CLI client example.

## Operations

- Query
It lists all books by running the following GraphQL query:
    ```graphql
    {
      books {
        title
        author
      }
    }
    ```

- Mutation
It adds a new book by running the following GraphQL mutation:
    ```graphql
    mutation {
      addBook(title: "{title}", author: "{author}") {
        success
        book {
          title
          author
        }
      }
    }
    ```

## Usage

**Docker**

- Build the container: `docker compose up -d --build`
- List books: `docker compose exec books python books_client.py list`
- Add a new book: `docker compose exec books python books_client.py add --title <title> --author <author>`. Parameter values with spaces must go between double quotes.
- Stop the container: `docker compose down`

**Python**

- List books: `python books_client.py list`
- Add a new book: `python books_client.py add --title <title> --author <author>`. Parameter values with spaces must go between double quotes.

## Tools
Graphene / Python

## Author
- Kesha Williams, from her LinkedIn Learning course [*Programming Foundations: APIs and Web Services*](https://www.linkedin.com/learning/programming-foundations-apis-and-web-services-27993033) ([Original source](https://github.com/LinkedInLearning/programming-foundations-apis-and-web-services-3811153/tree/main/03_02))
- Command-line interaction and separation client-server implemented by ChatGPT 5.1, prompted by Arturo Mora-Rioja.
- Dockerization implemented by ChatGPT 5.2, prompted by Arturo Mora-Rioja