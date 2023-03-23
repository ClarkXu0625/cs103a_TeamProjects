import sqlite3
##############this should have no problem############
class Transaction:
    def __init__(self, filename):
        self.conn = sqlite3.connect(filename)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY,
                        date TEXT,
                        description TEXT,
                        category TEXT,
                        amount REAL
                        )""")
        self.conn.commit()

    def add_transaction(self, amount, category, date, description):
        c = self.conn.cursor()
        c.execute("INSERT INTO transactions (amount, category, date, description) VALUES (?, ?, ?, ?)", (amount, category, date, description))
        self.conn.commit()

    def delete_transaction(self, transaction_id):
        c = self.conn.cursor()
        c.execute("DELETE FROM transactions WHERE id=?", (transaction_id,))
        self.conn.commit()

    def update_transaction(self, transaction_id, amount=None, category=None, date=None, description=None):
        c = self.conn.cursor()
        updates = {}
        if amount:
            updates['amount'] = amount
        if category:
            updates['category'] = category
        if date:
            updates['date'] = date
        if description:
            updates['description'] = description
        query = "UPDATE transactions SET " + ", ".join(f"{key}=?" for key in updates.keys()) + " WHERE id=?"
        params = tuple(updates.values()) + (transaction_id,)
        c.execute(query, params)
        self.conn.commit()

    def get_transactions(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM transactions")
        return c.fetchall()

    def get_categories(self):
        c = self.conn.cursor()
        c.execute("SELECT DISTINCT category FROM transactions")
        return [row[0] for row in c.fetchall()]

    def summarize_by_date(self):
        c = self.conn.cursor()
        c.execute("SELECT date, SUM(amount) FROM transactions GROUP BY date")
        return c.fetchall()

    def summarize_by_month(self):
        c = self.conn.cursor()
        c.execute("SELECT strftime('%Y-%m', date) AS month, SUM(amount) FROM transactions GROUP BY month")
        return c.fetchall()

    def summarize_by_year(self):
        c = self.conn.cursor()
        c.execute("SELECT strftime('%Y', date) AS year, SUM(amount) FROM transactions GROUP BY year")
        return c.fetchall()

    def summarize_by_category(self):
        c = self.conn.cursor()
        c.execute("SELECT category, SUM(amount) FROM transactions GROUP BY category")
        return c.fetchall()

    def add_category(self, category):
        c = self.conn.cursor()
        c.execute("INSERT INTO transactions (category) VALUES (?)", (category,))
        self.conn.commit()

    def modify_category(self, old_category, new_category):
        c = self.conn.cursor()
        c.execute("UPDATE transactions SET category=? WHERE category=?", (new_category, old_category))
        self.conn.commit()

        