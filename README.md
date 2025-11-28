# Books
GraphQL server and CLI client example.

## Usage
- `python books_client.py list`
It lists all books by running the following GraphQL query:
    ```graphql
    {
      books {
        title
        author
      }
    }
    ```

- `python books_client.py add --title <title> --author <author>`
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
    Parameter values with spaces must go between double quotes.

## Tools
Graphene / Python

## Author
- Kesha Williams, from her LinkedIn Learning course [*Programming Foundations: APIs and Web Services*](https://www.linkedin.com/learning/programming-foundations-apis-and-web-services-27993033) ([Original source](https://github.com/LinkedInLearning/programming-foundations-apis-and-web-services-3811153/tree/main/03_02))
- Command-line interaction and separation client-server implemented by ChatGPT 5.1, prompted by Arturo Mora-Rioja.