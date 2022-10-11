class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError('Attribute value cannot be negative.')
        if not isinstance(self.name, str):
            raise AttributeError('Attribute name must be a str object.')
    def transfer(self, amount):
        self.value += amount

class Bank:
    def __init__(self):
        self.accounts=[]
    def add(self,account):
        try:
            assert isinstance(account,Account),'account must be an `Account` object.'
            assert all(x.name!=account.name for x in self.accounts),'2 accounts cant have the same name.'
        except Exception as e:
            print(e)
        else:
            self.accounts.append(account)
    @staticmethod
    def is_corrupted(account):
        if not isinstance(account,Account):
            return True
        if len(dir(account))%2==0:
            return True
        if 'name' not in dir(account) or 'id' not in dir(account) or 'value' not in dir(account):
            return True
        if not isinstance(account.name,str) or not isinstance(account.id,int) or not isinstance(account.value,(int,float)):
            return True
        corr=1
        for attr in dir(account):
            if attr.startswith('b'):
                return True
            elif attr.startswith('zip') or attr.startswith('addr'):
                corr=0
        if corr==1:
            return True
        return False
    def get_account_by_name(self,name):
        if isinstance(name,str):
            for account in self.accounts:
                if account.name==name:
                    return account
        else:
            print('name needs to be an string.')
    def transfer(self,origin,dest,amount):
        if not isinstance(origin,str) or not isinstance(dest,str):
            print('names need to be strings.')
            return False
        sender=self.get_account_by_name(origin)
        receiver=self.get_account_by_name(dest)
        if not sender or not receiver:
            print('one of the accounts provided for transfer wasnt found.')
            return False
        if sender.name==receiver.name:
            return True
        if self.is_corrupted(sender):
            print('sender->'+origin+': account corrupted.')
            return False
        if self.is_corrupted(receiver) :
            print(dest+': account corrupted.')
            return False
        if sender.value<amount:
            print('receiver->'+origin+': funds insufficient.')
            return False
        sender.value-=amount
        receiver.value+=amount
        return True
    def fix_account(self,name):
        if not isinstance(name,str):
            return False
        account=self.get_account_by_name(name)
        if not account:
            print('account->'+name+': account not found.')
            return False
        if not self.is_corrupted(account):
            print('account->'+name+': isnt corrupted.')
            return False
        if not hasattr(account,'name'):
            account.name=''
        if not hasattr(account,'value'):
            account.value=1.0
        if not hasattr(account,'id'):
            account.id=Account.ID_COUNT
            Account.ID_COUNT+=1
        zip_or_addr=0
        for attr in dir(account):
            if attr.startswith('zip') or attr.startswith('addr'):
                zip_or_addr=1
        if zip_or_addr==0:
            account.zip=0
        for attr in dir(account):
            if attr.startswith('b'):
                delattr(account,attr)
        if len(dir(account))%2==0:
            account.make_odd=1
        return True


tobi=Account('tobi',value=100,zip=22,addr='rue')
jean=Account('jean',value=100,zip=23,addr='avenue')
bank=Bank()
bank.add(tobi)
bank.add(jean)
print(tobi.value)
bank.transfer('tobi','jean',10)
print(tobi.value)
corrupted=Account('corr',value=100)
bank.add(corrupted)
print(bank.is_corrupted(corrupted))
bank.fix_account('corr')
print(bank.is_corrupted(corrupted))