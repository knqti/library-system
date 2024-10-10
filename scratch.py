def check_out_confirmation(library_file):
    while True:

        with open(library_file, 'r') as file:
            reader = csv.reader(file)

            user_check_out = input('\n>>> Select the Index number to check out (x to main menu): ').strip()

            for index, row in enumerate(reader):

                if user_check_out == 'x':
                    # Exit function
                    print('Exiting...')
                    return user_check_out
            
                elif index == int(user_check_out):
                    print(f'\nYou want to check out:')
                    print(f'{row[2]} by {row[0]}, {row[1]}')

                    user_confirm = input('>>> Is this correct? (y/n): ').strip().lower()

                    if user_confirm == 'y':
                        # Exit function
                        print('Confirmed!')
                        return user_check_out
                    
                    elif user_confirm == 'n':
                        # Restart confirmation
                        break

                    else:
                        print('error')
                        # NEED SOME WAY TO CATCH ERRORS
                        # err_msg = 'Invalid choice. Please try again.\nTo check out a book, type its Index number and press enter.\nTo go back to the main menu, type "x" and press enter.'
