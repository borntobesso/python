class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = Account.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        print("First init: ", self.__dict__)
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute balue cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
        print("Second init: ", self.__dict__)
        
    def transfer(self, amount):
        self.value += amount

class Bank(object):
    '''The bank'''
    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        '''Add new_account in the Bank
            @new_account: Account() new account to append
            @return True if success, False if an error occured
        '''
        # test if new_account is an Account() intstance and if
        # it can be appended to the attribute accounts
        if not isinstance(new_account, Account):
            raise TypeError("new_account must be an Account() instance.")
        elif new_account.name in [account.name for account in self.accounts]:
            raise ValueError("new_account is already in the accounts list.")
        self.accounts.append(new_account)

    def transfer(self, origin, dest, amount):
        '''Perform the fund transfer
            @origin: str(name) of the first account
            @dest: str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        '''
        # test if origin and dest are str and amount is a float
        if not isinstance(origin, str) or not isinstance(dest, str) or not isinstance(amount, float):
            return False
        # test if origin and dest are in the accounts list
        elif origin not in [account.name for account in self.accounts] or \
           dest not in [account.name for account in self.accounts]:
            return False
        for account in self.accounts:
            if account.name == origin:
                origin = account
            elif account.name == dest:
                dest = account
        # test if amount is positive and if origin has enough money
        if amount < 0 or amount > origin.value:
            return False
        # if all tests are passed, transfer the money
        elif not self.is_corrupted(origin) and not self.is_corrupted(dest):
            if origin == dest:
                return True
            origin.value -= amount
            dest.transfer(amount)
            return True
        else:
            return False
        
    def fix_account(self, account):
        '''Fix account associated to name if corrupted
            @account: str(name) of the account
            @return True if success, False if an error occured
        '''
        dict_attr = {}
        if not isinstance(account, str) or account not in [account.name for account in self.accounts]:
            return False
        for acc in self.accounts:
            if acc.name == account:
                account = acc
                attr = [attr for attr in dir(account) if not attr.startswith('__')]
                break
        if not hasattr(account, 'zip'):
            dict_attr['zip'] = ""
        if not hasattr(account, 'addr'):
            dict_attr['addr'] = ""
        for attr in attr:
            if attr.startswith('b'):
                delattr(account, attr)
        if not hasattr(account, 'id'):
            dict_attr['id'] = Account.ID_COUNT
            Account.ID_COUNT += 1
        if not hasattr(account, 'value'):
            dict_attr['value'] = 0
        account.__dict__.update(dict_attr)
        attr = [attr for attr in dir(account) if not attr.startswith('__')]
        if len(attr) % 2 == 0:
            if not hasattr(account, 'placeholder'):
                dict_attr['placeholder'] = None
            else:
                delattr(account, "placeholder")
        account.__dict__.update(dict_attr)
        return True

    def is_corrupted(self, account):
        '''Check if the account is corrupted
            @account: str(name) of the account
            @return True if corrupted, False if not
        '''
        attr = []
        for acc in self.accounts:
            if acc.name == account.name:
                attr = [attr for attr in dir(account) if not attr.startswith('__')]
                break
        if len(attr) % 2 == 0:
            return True
        elif "name" not in attr or "id" not in attr or "value" not in attr:
            return True
        elif "zip" not in attr or "addr" not in attr:
            return True
        for attr in attr:
            if attr.startswith('b'):
                return True
        if not isinstance(account.name, str) or not isinstance(account.id, int) or not isinstance(account.value, (float, int)):
            return True
        else:
            return False
