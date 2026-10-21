from dao.account_dao import AccountDAO
from model.account import Account


class AccountService:


    def add_account(self, account):
        A = AccountDAO()
        if account.balance < 0:
            print("Balance cannot be negative.")
            return 0
        return A.add_account(account)

    def update_account(self, account_no, holder_name, balance):
        A = AccountDAO()
        if balance < 0:
            print("Balance cannot be negative.")
            return 0
        return A.update_account(account_no, holder_name, balance)

    def delete_account(self, account_no):
        A = AccountDAO()
        return A.delete_account(account_no)

    def search_account(self, account_no):
        A = AccountDAO()
        return A.search_account(account_no)

    def display_all_accounts(self):
        A = AccountDAO()
        return A.display_all_accounts()
