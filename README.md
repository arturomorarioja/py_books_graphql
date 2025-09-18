# Books
GraphQL example

## Usage
Query all books
```graphql
{
  books {
    title
    author
  }
}
```

Add a new book
```graphql
addBook(title: "Dune", author: "Frank Herbert") {
  success
    book {
      title
      author
  }
}
```

## Tools
Graphene / Python

## Author
Kesha Williams, from her LinkedIn Learning course [*Programming Foundations: APIs and Web Services*](https://www.linkedin.com/learning/programming-foundations-apis-and-web-services-27993033) ([Original source](https://github.com/LinkedInLearning/programming-foundations-apis-and-web-services-3811153/tree/main/03_02)).