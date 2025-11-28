"""
GraphQL Books schema and data store.

From the LinkedIn Learning course "Programming Foundations: APIs and Web Services" (Kesha Williams, 2025)
https://www.linkedin.com/learning/programming-foundations-apis-and-web-services-27993033
"""

from graphene import ObjectType, String, List, Field, Schema, Mutation, Boolean
import json

DATA_FILE = 'books_data.json'


def load_books():
    """Loads books_data from the JSON file."""
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_books():
    """Saves the current books_data list to the JSON file."""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(books_data, f, ensure_ascii=False, indent=2)


# In-memory data store for books, initialized from JSON file
books_data = load_books()


#
# 1) GraphQL Book type
#
class Book(ObjectType):
    title = String()
    author = String()


#
# 2) Query class
#
class Query(ObjectType):
    """
    Defines two fields:
      - book(title): returns a single Book
      - books: returns a list of all books
    """

    book = Field(Book, title=String(required=True))
    books = List(Book)

    def resolve_book(root, info, title):
        for b in books_data:
            if b['title'] == title:
                return Book(title=b['title'], author=b['author'])
        return None

    def resolve_books(root, info):
        return [
            Book(title=b['title'], author=b['author']) for b in books_data
        ]


#
# 3) Mutation to add a new book
#
class AddBook(Mutation):
    class Arguments:
        title = String(required=True)
        author = String(required=True)

    success = Boolean()
    book = Field(Book)

    def mutate(root, info, title, author):
        new_entry = {'title': title, 'author': author}
        books_data.append(new_entry)
        save_books()

        return AddBook(
            success=True,
            book=Book(title=title, author=author)
        )


#
# 4) Mutation class (can contain multiple mutations)
#
class Mutation(ObjectType):
    add_book = AddBook.Field()


#
# 5) Build the GraphQL schema
#
schema = Schema(query=Query, mutation=Mutation)