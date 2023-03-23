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