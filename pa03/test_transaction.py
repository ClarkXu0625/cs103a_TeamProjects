import pytest
import sqlite3
import tempfile

from transaction import Transaction


@pytest.fixture
def transaction():
    # Create a temporary file for testing
    with tempfile.NamedTemporaryFile() as temp_file:
        # Create a Transaction object
        txn = Transaction(temp_file.name)
        yield txn


def test_create_table(transaction):
    # Assert that the table exists
    assert 'transactions' in [table[0] for table in
                              transaction.conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()]


def test_add_transaction(transaction):
    # Add a transaction
    transaction.add_transaction(100, 'food', '2022-03-18', 'Groceries')

    # Assert that the transaction was added successfully
    result = transaction.conn.execute("SELECT * FROM transactions").fetchall()
    assert len(result) == 1
    assert result[0][3] == 'food'
    assert result[0][4] == 100


def test_delete_transaction(transaction):
    # Add a transaction
    transaction.add_transaction(100, 'food', '2022-03-18', 'Groceries')

    # Delete the transaction
    transaction.delete_transaction(1)

    # Assert that the transaction was deleted successfully
    result = transaction.conn.execute("SELECT * FROM transactions").fetchall()
    assert len(result) == 0

######test have not be completed yet##########

def test_delete_transaction(transaction):
    # Add a transaction
    transaction.add_transaction(100, 'food', '2022-03-18', 'Groceries')

    # Delete the transaction
    transaction.delete_transaction(1)

    # Assert that the transaction was deleted successfully
    result = transaction.conn.execute("SELECT * FROM transactions").fetchall()
    assert len(result) == 0


def test_get_transactions(transaction):
    # Add a few transactions
    transaction.add_transaction(100, 'food', '2022-03-18', 'Groceries')
    transaction.add_transaction(50, 'gas', '2022-03-19', 'Car Expenses')
    transaction.add_transaction(200, 'clothes', '2022-03-20', 'Shopping')

    # Get all transactions
    result = transaction.get_transactions()

    # Assert that the transactions were retrieved successfully
    assert len(result) == 3
    assert result[0][3] == 'food'
    assert result[1][3] == 'gas'
    assert result[2][3] == 'clothes'

def test_summarize_by_date(transaction):
    # Add some transactions
    transaction.add_transaction(100, 'food', '2022-03-18', 'Groceries')
    transaction.add_transaction(50, 'food', '2022-03-18', 'Restaurants')
    transaction.add_transaction(25, 'entertainment', '2022-03-19', 'Movies')

    # Summarize by date
    result = transaction.summarize_by_date()

    # Assert that the summary is correct
    assert len(result) == 2
    assert result[0][0] == '2022-03-18'
    assert result[0][1] == 150
    assert result[1][0] == '2022-03-19'
    assert result[1][1] == 25

def test_summarize_by_month(transaction):
    # Add some transactions
    transaction.add_transaction(100, 'food', '2022-03-18', 'Groceries')
    transaction.add_transaction(50, 'food', '2022-03-18', 'Restaurants')
    transaction.add_transaction(25, 'entertainment', '2022-04-19', 'Movies')

    # Summarize by month
    result = transaction.summarize_by_month()

    # Assert that the summary is correct
    assert len(result) == 2
    assert result[0][0] == '2022-03'
    assert result[0][1] == 150
    assert result[1][0] == '2022-04'
    assert result[1][1] == 25

def test_summarize_by_year(transaction):
    # Add some transactions
    transaction.add_transaction(100, 'food', '2022-03-18', 'Groceries')
    transaction.add_transaction(50, 'food', '2022-03-18', 'Restaurants')
    transaction.add_transaction(25, 'entertainment', '2023-04-19', 'Movies')

    # Summarize by year
    result = transaction.summarize_by_year()

    # Assert that the summary is correct
    assert len(result) == 2
    assert result[0][0] == '2022'
    assert result[0][1] == 150
    assert result[1][0] == '2023'
    assert result[1][1] == 25

def test_summarize_by_category(transaction):
    # Add some transactions
    transaction.add_transaction(100, 'food', '2022-03-18', 'Groceries')
    transaction.add_transaction(50, 'food', '2022-03-18', 'Restaurants')
    transaction.add_transaction(25, 'entertainment', '2022-04-19', 'Movies')

    # Summarize by category
    result = transaction.summarize_by_category()

    # Assert that the summary is correct
    assert len(result) == 2
    assert result[0][0] == 'entertainment'
    assert result[0][1] == 25
    assert result[1][0]== 'food'
    assert result[1][1] == 150

def test_add_category(transaction):
    # Add a new category
    transaction.add_category('Utilities')

    # Assert that the category was added successfully
    result = transaction.conn.execute("SELECT category FROM transactions").fetchall()
    assert len(result) == 1
    assert result[0][0] == 'Utilities'

def test_modify_category(transaction):
    # Add a transaction with the old category
    transaction.add_transaction(100, 'food', '2022-03-18', 'Groceries')

    # Modify the category
    transaction.modify_category('food', 'cood')

    # Assert that the category was modified successfully
    result = transaction.conn.execute("SELECT category FROM transactions").fetchall()
    assert len(result) == 1
    assert result[0][0] == 'cood'