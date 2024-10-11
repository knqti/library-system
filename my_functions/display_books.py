def display_books(dictionary):
    # Display header section
    print(f'\n{"Index":<5} | {"Author-Last":<17} | {"Author-First":<17} | {"Title":<20} | {"Edition":<7} | {"Status":<15} | {"Due Date":<10}')
    print('-' * 115)

    # Display books
    for book_index, book in dictionary.items():
        print(f'{book_index:<5} | {book.author_last[:17]:<17} | {book.author_first[:17]:<17} | {book.book_title[:20]:<20} | {book.book_edition:<8}| {book.book_status:<15} | {book.book_due_date:<10}')
