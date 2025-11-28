"""
GraphQL Books CLI client.

Uses the schema defined in books_graphql.py and executes operations via the command line.
"""

import argparse
from books_server import schema


def run_query_all():
    """Executes a GraphQL query to retrieve all books."""
    query = """
    {
      books {
        title
        author
      }
    }
    """
    result = schema.execute(query)
    print('\nBooks:\n', result.data)


def run_add_book(title, author):
    """Executes a GraphQL mutation to add a new book."""
    mutation = f"""
    mutation {{
      addBook(title: "{title}", author: "{author}") {{
        success
        book {{
          title
          author
        }}
      }}
    }}
    """
    result = schema.execute(mutation)
    print('\nAdd Book Mutation:\n', result.data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='GraphQL Books CLI')

    subparsers = parser.add_subparsers(dest='command', required=True)

    # A) query
    parser_query = subparsers.add_parser('list', help='Query all books')

    # B) new
    parser_new = subparsers.add_parser('add', help='Add a new book')
    parser_new.add_argument('--title', '-title', required=True)
    parser_new.add_argument('--author', '-author', required=True)

    args = parser.parse_args()

    if args.command == 'list':
        run_query_all()

    elif args.command == 'add':
        run_add_book(args.title, args.author)