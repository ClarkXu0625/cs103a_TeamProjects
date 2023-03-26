# Create a file tracker.py which offers the user the following options and makes calls to the Transaction class to update the database.

from transaction import Transaction
import sys


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
  11. print_commands 

=======================================
'''
    )

def main():
    """Main function.
    Ephraim Zimmerman
    """
    print()
    print("Enter your database filename. If the file does not exist, a new one will be  created.")
    filename = input("filename >> ")
    transaction = Transaction(filename)
    if len(sys.argv) == 1:
        print_menu()
        args = []
        while args!=[""]:
            args = input("command >> ").split(" ")
            if args[0] == "quit":
                    break
            elif args[0] == "add_category":
                    transaction.add_category(args[1])
                    print("Added category: ", args[1])
            elif args[0] == "modify_category":
                    transaction.modify_category(args[1], args[2])
                    print("Modified category:", args[1], "->", args[2])
            elif args[0] == "show_transactions":
                    print(transaction.get_transactions())
            elif args[0] == "add_transaction":
                    transaction.add_transaction(args[2], args[1], args[3], ''.join(map(str, args[4:])))
                    print("Added transaction.")
            elif args[0] == "delete_transaction":
                    print(transaction.delete_transaction(args[1]))
            elif args[0] == "summarize_transactions_date":
                    print(transaction.summarize_by_date())
            elif args[0] == "summarize_transactions_month":
                    print(transaction.summarize_by_month())
            elif args[0] == "summarize_transactions_year":
                    print(transaction.summarize_by_year())
            elif args[0] == "show_categories":
                    print("categories:")
                    print(transaction.get_categories())
            elif args[0] == "summarize_transactions_category":
                    print(transaction.summarize_by_category())
            elif args[0] == "print_commands":
                    print_menu()
            else:
                print("Unknown command")

main()