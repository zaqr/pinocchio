"""Model transactions"""

from random import choices, randint
from string import ascii_letters, digits

account_chars: str = digits + ascii_letters

def _generate_account() -> str:
    return ''.join(choices(account_chars, k=12))

def _random_amount() -> float:
    return randint(100, 100000) / 100

def generate_random_transaction() -> dict:
    return {
        'from': _generate_account(),
        'to': _generate_account(),
        'amount': _random_amount(),
        'currency': 'USD',
    }