def check_out_return_guard(dictionary, total_dictionary_items, input_message, status):
    while True:
        user_input = input(f'{input_message}').strip().lower()

        # Unhappy route
        try:
            # Convert the input to an integer
            user_input = int(user_input)            

            # Check for invalid Index numbers
            if not 0 <= user_input <= total_dictionary_items:
                print('\nInvalid choice. Please try again.\nType an Index number and press enter to proceed.\nOtherwise, type "x" and press enter to return to the main menu.')
                continue

            selected_book = dictionary[user_input]

            # Check for invalid book status
            if selected_book.book_status == f'{status}':
                print(f'\nSorry, that book is already {status}. Please try again.')
                continue
        
        except ValueError:
            # Check for invalid strings
            if type(user_input) == str and user_input != 'x':
                print('\nInvalid choice. Please try again.\nTo check out a book, type its Index number and press enter.\nTo go back to the main menu, type "x" and press enter.')
                continue
            
            # Exit
            elif user_input == 'x':
                selected_book = ''
                break
        
        # Checks passed
        break

    return user_input, selected_book