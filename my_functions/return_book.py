from .check_out_return_guard import check_out_return_guard


def return_book(dictionary, total_dictionary_items):
    input_message = '\n>>> Select the book Index number to return (x to main menu): '
    status = 'available'

    user_input, selected_book = check_out_return_guard(dictionary, total_dictionary_items, input_message, status)
    
    # Exit
    if user_input == 'x':
        return user_input

    # Return process
    selected_book.book_status = 'Available'
    selected_book.book_due_date = ''

    print(f'\nReturned: {selected_book.book_title} by {selected_book.author_last}, {selected_book.author_first}')

    user_input = 'success'    
    return user_input