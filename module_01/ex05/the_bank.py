from random import randint
from uuid import uuid4


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
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount

    def __repr__(self):
        return f"Account {self.__dict__}"

    def __str__(self):
        return self.__repr__()


def account_is_corrupted(account):
    as_dict = account.__dict__
    return (
        not len(as_dict) % 2
        or [x.startswith('b') for x in as_dict].count(True)
        or [[x.startswith(y) for x in as_dict].count(True)
            for y in ('zip', 'addr')].count(0) == 2
        or not all(x in as_dict for x in ('name', 'id', 'value'))
        or not isinstance(as_dict["name"], str)
        or not isinstance(as_dict["id"], int)
        or not isinstance(as_dict["value"], (int, float))
    )


class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """
        Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        if not isinstance(new_account, Account):
            raise TypeError("new_account must be an Account instance")
        if next(
            (x for x in self.accounts if x.name == new_account.name), None
        ):
            raise ValueError(f"Account {new_account.name} already exists")
        self.accounts.append(new_account)

    def transfer(self, origin, dest, amount):
        """
        Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        if not isinstance(origin, str):
            raise TypeError("origin must be a str object")
        if not isinstance(dest, str):
            raise TypeError("dest must be a str object")
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be a number")
        if amount < 0:
            raise ValueError("amount cannot be negative")
        origin_account = next(
            (x for x in self.accounts if x.name == origin), None
        )
        dest_account = next(
            (x for x in self.accounts if x.name == dest), None
        )
        if (
            not origin_account
            or not dest_account
            or origin_account.value < amount
            or account_is_corrupted(origin_account)
            or account_is_corrupted(dest_account)
        ):
            return False
        origin_account.transfer(-amount)
        dest_account.transfer(amount)
        return True

    def fix_account(self, name):
        """
        fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            raise TypeError("name must be a str object")
        account = next(
            (x for x in self.accounts if x.name == name), None
        )
        if not account:
            return False
        as_dict = account.__dict__
        for x in [y for y in as_dict.keys() if y.startswith('b')]:
            del as_dict[x]

        if (
            [[x.startswith(y) for x in as_dict].count(True)
                for y in ('zip', 'addr')].count(0) == 2
        ):
            as_dict['zip'] = '000-000'
            as_dict['addr'] = 'Unknown'

        if 'name' not in as_dict or not isinstance(as_dict['name'], str):
            as_dict['name'] = 'Unknown'
            i = 1
            while next(
                (x for x in self.accounts if x.name == as_dict['name']), None
            ):
                as_dict['name'] = f"Unknown_{i}"
                i += 1
        if 'id' not in as_dict or not isinstance(as_dict['id'], int):
            as_dict['id'] = max(
                [x.__dict__.get('id', -1) for x in self.accounts]
            ) + 1
        if (
            'value' not in as_dict
            or not isinstance(as_dict['value'], (int, float))
        ):
            as_dict['value'] = 0
        if not len(as_dict) % 2:
            key = str(uuid4())
            while key in as_dict:
                key = str(uuid4())
            as_dict[key] = None
        return True
