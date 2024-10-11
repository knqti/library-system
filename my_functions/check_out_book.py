from datetime import datetime, timedelta
from .check_out_return_guard import check_out_return_guard
from .export_dictionary_to_csv import export_dictionary_to_csv


def check_out_book(dictionary, total_dictionary_items, csv_file):
    print('Pending check out...')
    input_message = '\n>>> Select the book Index number to check out (x to main menu): '
    status = 'Checked out'
    
    user_input, selected_book = check_out_return_guard(dictionary, total_dictionary_items, input_message, status)
    
    # Exit
    if user_input == 'x':
        return

    # Check out process
    selected_book.book_status = status
    due_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
    selected_book.book_due_date = due_date

    print(f'\nChecked out: {selected_book.book_title} by {selected_book.author_last}, {selected_book.author_first}')
    print(f'Due date: {due_date}')

    export_dictionary_to_csv(csv_file, dictionary)

    print('\n...check out complete!')
    return