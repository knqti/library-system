from datetime import datetime, timedelta


def check_out_book(dictionary, total_dictionary_items):
    while True:
        user_input = input('\n>>> Select the Index number to check out (x to main menu): ').strip().lower()

        # Unhappy route
        try:
            # Convert the input to an integer
            user_input = int(user_input)            

            # Check for invalid Index numbers
            if not 0 <= user_input <= total_dictionary_items:
                print('\nInvalid choice. Please try again.\nTo check out a book, type its Index number and press enter.\nTo go back to the main menu, type "x" and press enter.')
                continue

            selected_book = dictionary[user_input]

            # Check for invalid book status
            if selected_book.book_status == 'Checked out':
                print('\nSorry, that book is already checked out. Please try again.')
                continue
        
        except ValueError:
            # Check for invalid strings
            if type(user_input) == str and user_input != 'x':
                print('\nInvalid choice. Please try again.\nTo check out a book, type its Index number and press enter.\nTo go back to the main menu, type "x" and press enter.')
                continue
            
            # Exit
            elif user_input == 'x':
                print('exit to main menu')
                break

        # Check out process
        selected_book.book_status = 'Checked out'
        due_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
        selected_book.book_due_date = due_date

        print(f'\nChecked out: {selected_book.book_title} by {selected_book.author_last}, {selected_book.author_first}')
        print(f'\nDue date: {due_date}')

        user_input = 'success'
        break    
        
    return user_input