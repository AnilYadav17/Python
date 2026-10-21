from database.connection import get_connection
from model.account import Account

class AccountDAO:
    def add_account(self, account):
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO account (account_no, holder_name, balance, account_type) VALUES (%s, %s, %s, %s)"
        values = (account.account_no, account.holder_name, account.balance, account.account_type)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        return cursor.rowcount

    def update_account(self, account_no, holder_name, balance):
        conn = get_connection()

        cursor = conn.cursor()
        query = "UPDATE account SET holder_name = %s, balance = %s WHERE account_no = %s"
        values = (holder_name, balance, account_no)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        return cursor.rowcount

               

    def delete_account(self, account_no):
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM account WHERE account_no = %s"
        values = (account_no,)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        return cursor.rowcount

    def search_account(self, account_no):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM account WHERE account_no = %s"
        values = (account_no,)
        cursor.execute(query, values)
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Account(row['account_no'], row['holder_name'], row['balance'], row['account_type'])
        return None


    def display_all_accounts(self):
        conn = get_connection()
        accounts = []
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM account"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        for row in rows:
            accounts.append(Account(row['account_no'], row['holder_name'], row['balance'], row['account_type']))
        return accounts

