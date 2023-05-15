# pylint result:
(ml) Clarks-MBP:pa03 apple$ pylint tracker.py
************* Module tracker
tracker.py:36:0: R0912: Too many branches (24/12) (too-many-branches)
tracker.py:36:0: R0915: Too many statements (57/50) (too-many-statements)

------------------------------------------------------------------
Your code has been rated at 9.68/10 (previous run: 9.68/10, +0.00)

# pytest result:
(ml) Clarks-MBP:pa03 apple$ pytest -v
============================= test session starts ==============================
platform darwin -- Python 3.11.2, pytest-7.2.1, pluggy-1.0.0 -- /opt/homebrew/opt/python@3.11/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/apple/Documents/GitHub/cs103a_TeamProjects/pa03
collected 10 items                                                             

test_transaction.py::test_create_table PASSED                            [ 10%]
test_transaction.py::test_add_transaction PASSED                         [ 20%]
test_transaction.py::test_delete_transaction PASSED                      [ 30%]
test_transaction.py::test_get_transactions PASSED                        [ 40%]
test_transaction.py::test_summarize_by_date PASSED                       [ 50%]
test_transaction.py::test_summarize_by_month PASSED                      [ 60%]
test_transaction.py::test_summarize_by_year PASSED                       [ 70%]
test_transaction.py::test_summarize_by_category PASSED                   [ 80%]
test_transaction.py::test_add_category PASSED                            [ 90%]
test_transaction.py::test_modify_category PASSED                         [100%]

============================== 10 passed in 0.02s ==============================
(ml) Clarks-MBP:pa03 apple$ 

# tracker.py
Enter your database name first, then run either one of the commands:
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


Hanyu Xie: 

/usr/local/bin/python3 "/Users/hanyuxie/Desktop/Homework/2023 Spring/Cosi 103/cs103a_TeamProjects/pa03/tracker.py"

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
(base) hanyus-MBP:cs103a_TeamProjects hanyuxie$ /usr/local/bin/python3 "/Users/hanyuxie/Desktop/Homework/2023 Spring/Cosi 103/cs103a_TeamProjects/pa03/tracker.py"

Enter your database filename. If the file does not exist, a new one will be created.
filename >>> test

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

>>> quit

(base) hanyus-MBP:cs103a_TeamProjects hanyuxie$ cd pa03
(base) hanyus-MBP:pa03 hanyuxie$ pylint transaction.py
************* Module transaction
transaction.py:61:4: R0913: Too many arguments (6/5) (too-many-arguments)
transaction.py:83:34: C0201: Consider iterating the dictionary directly instead of calling .keys() (consider-iterating-dictionary)

------------------------------------------------------------------
Your code has been rated at 9.69/10 (previous run: 9.69/10, +0.00)

(base) hanyus-MBP:pa03 hanyuxie$ pytest -v test_transaction.py
=========================================================== test session starts ===========================================================
platform darwin -- Python 3.9.13, pytest-7.1.2, pluggy-1.0.0 -- /Users/hanyuxie/opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/hanyuxie/Desktop/Homework/2023 Spring/Cosi 103/cs103a_TeamProjects/pa03
plugins: anyio-3.5.0
collected 10 items                                                                                                                        

test_transaction.py::test_create_table PASSED                                                                                       [ 10%]
test_transaction.py::test_add_transaction PASSED                                                                                    [ 20%]
test_transaction.py::test_delete_transaction PASSED                                                                                 [ 30%]
test_transaction.py::test_get_transactions PASSED                                                                                   [ 40%]
test_transaction.py::test_summarize_by_date PASSED                                                                                  [ 50%]
test_transaction.py::test_summarize_by_month PASSED                                                                                 [ 60%]
test_transaction.py::test_summarize_by_year PASSED                                                                                  [ 70%]
test_transaction.py::test_summarize_by_category PASSED                                                                              [ 80%]
test_transaction.py::test_add_category PASSED                                                                                       [ 90%]
test_transaction.py::test_modify_category PASSED                                                                                    [100%]

=========================================================== 10 passed in 0.06s ============================================================
(base) hanyus-MBP:pa03 hanyuxie$ 

I've implmennt the transaction.py, and most of the tests -Hanyu Xie