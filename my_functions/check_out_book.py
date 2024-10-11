from datetime import datetime, timedelta
from .check_out_return_guard import check_out_return_guard


def check_out_book(dictionary, total_dictionary_items):
    input_message = '\n>>> Select the book Index number to check out (x to main menu): '
    status = 'checked out'
    
    user_input, selected_book = check_out_return_guard(dictionary, total_dictionary_items, input_message, status)
    
    # Exit
    if user_input == 'x':
        return user_input

    # Check out process
    selected_book.book_status = 'Checked out'
    due_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
    selected_book.book_due_date = due_date

    print(f'\nChecked out: {selected_book.book_title} by {selected_book.author_last}, {selected_book.author_first}')
    print(f'Due date: {due_date}')

    user_input = 'success'    
    return user_input