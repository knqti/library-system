import csv
from my_classes import Book


def initialize_dictionary(csv_file, dictionary):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)

        for index, row in enumerate(reader):
            # Assign the column values to Book's attributes
            book = Book(
                book_index=index,
                author_last=row[0],
                author_first=row[1],
                book_title=row[2],
                book_edition=row[3],
                book_status=row[4],
                book_due_date=row[5]
            )

            # Store each book into the dictionary using the index as key
            dictionary[book.book_index] = book

    # for book_index, item in book_dictionary.items():
    #     print(f'\nBook index: {book_index}')
    #     print(item.__dict__)
    
    return dictionary