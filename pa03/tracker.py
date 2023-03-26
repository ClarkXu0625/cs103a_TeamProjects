''' Create a file tracker.py which offers the user the following
 options and makes calls to the Transaction class to update the database.'''

import sys
from transaction import Transaction


def print_menu():
    """Menu of commands.
    Ephraim Zimmerman
    """
    print(
        '''
=======================================
           TRANSACTION MENU
  Type any of the following commands.

  1. show_categories
  2. add_category <category>
  3. modify_category <category> <modified category name>
  4. show_transactions
  5. [date is YYYY-MM-DD] add_transaction <category> <trans. amount> <date> <description>
  6. delete_transaction <transaction id>
  7. summarize_transactions_date
  8. summarize_transactions_month
  9. summarize_transactions_year
  10. summarize_transactions_category
  11. help
  12. reselect_file <file_path>
  13. quit

=======================================
'''
    )

def main():
    """Main function.
    Written by Ephraim Zimmerman, Clark Xu
    """
    print()
    print("Enter your database filename. If the file does not exist, a new one will be created.")
    filename = input("filename >>> ")
    transaction = Transaction(filename)
    if len(sys.argv) == 1:
        print_menu()
        args = []
        while True:
            command = input(">>> ")
            args = command.split(" ")
            given = len(args)-1     # number of arguements given

            # quit
            if command.strip()=="help":
                print_menu()

            # add category
            elif args[0] == "add_category":
                if len(args) == 2:
                    transaction.add_category(args[1])
                    print("Added category: ", args[1])
                else:
                    print_error(given, 2)
            # modify category
            elif args[0] == "modify_category":
                if len(args) == 3:
                    transaction.add_category(args[1])
                    print("Added category: ", args[1])
                    transaction.modify_category(args[1], args[2])
                    print("Modified category:", args[1], "->", args[2])
                else:
                    print_error(given, 1)

            # show transaction
            elif args[0] == "show_transactions":
                print(transaction.get_transactions())

            # add transaction
            elif args[0] == "add_transaction":
                transaction.add_transaction(args[2], args[1], args[3], ''.join(map(str, args[4:])))
                print("Added transaction.")

            # delete transaction
            elif args[0] == "delete_transaction":
                if len(args) == 2:
                    print(transaction.delete_transaction(args[1]))
                else:
                    print_error(given, 1)

            # summarize by date
            elif args[0] == "summarize_transactions_date":
                print(transaction.summarize_by_date())

            # summarize by month
            elif args[0] == "summarize_transactions_month":
                print(transaction.summarize_by_month())

            # summarize by month
            elif args[0] == "summarize_transactions_year":
                print(transaction.summarize_by_year())

            # print categories
            elif args[0] == "show_categories":
                print("categories:")
                print(transaction.get_categories())

            # summarize transaction by categories
            elif args[0] == "summarize_transactions_category":
                print(transaction.summarize_by_category())

            elif args[0] == "reselect_file":
                if len(args) == 2:
                    transaction = Transaction(args[1])
                else:
                    print_error(given, 1)

            elif command.strip() == 'quit':
                break

            # otherwise unknown command
            elif command.strip()!="":
                print("Unknown command")

def print_error(given, required):
    '''print error message when the number of arguments isn't compatable'''
    argument_error = "Type <help> to get list of arguments"
    print(f"Argument not compatiable, {given} argument(s) given but {required} required")
    print(argument_error)

main()
