from re import search

class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1
    
    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    def __str__(self):
        return str([a.name for a in self.account])

    def add(self, account):
        if isinstance(account, Account):
            self.account.append(account)

    def find_account(self, origin):
        if type(origin) is int:
            for elem in self.account:
                if elem.id == origin:
                    return elem
        elif type(origin) is str:
            for elem in self.account:
                if elem.name == origin:
                    return elem
        return None
    
    def check_attr(self, account):
        zipok = False
        addrok = False
        for attr in account.__dict__.keys(): 
            if not zipok and search(r'^zip.*', attr):
                zipok = True 
            if not addrok and search(r'^addr.*', attr):
                addrok = True
            if search(r'^b.*', attr):
                return False
            if zipok and addrok:
                return True
        return False

    def not_corrupted(self, account):
        if 'value' not in account.__dict__ or \
            'name' not in account.__dict__ or \
            'id' not in account.__dict__:
            return False  
        if not len(account.__dict__) % 2:
            return False
        return self.check_attr(account)
        
    def transfer(self, origin, dest, amount):
        """
            @origin:  int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return         True if success, False if an error occured
        """
        o = self.find_account(origin)
        d = self.find_account(dest)
        if not o or not d:
            return False
        if self.not_corrupted(o) and self.not_corrupted(d):
            if amount > 0 and amount <= o.value:
                o.value -= amount
                d.transfer(amount)
                return True
        return False

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
        """
        a = self.find_account(account)
        if a:
            self.account.remove(a)
        return True

if __name__ == '__main__':
    bank = Bank()
    acc1 = Account('test', zip_='a', addr='b', id=5, value=45, gg=4, cc=5)
    acc1.transfer(50)
    acc2 = Account('test2', zip_='a', addr='b', id=5, value=45, gg=4, cc=6)
    acc3 = Account('test0', zip_='a', addr='b', id=5, value=45, bolide=4, cc=6)
    bank.add(acc1)
    bank.add(acc2)
    bank.add(acc3)
    print(bank)
    print(acc1.value)
    print(acc2.value)
    print(bank.transfer('test', 'test2', 20))
    print(bank.transfer('test3', 'test2', 20))
    print(bank.transfer('test', 'test2', 100))
    print(bank.transfer('test', 'test0', 10))
    print(bank.transfer('test', 'test2', -3))
    print(acc1.value)
    print(acc2.value)
    print(bank.fix_account('test0'))
    print(bank)