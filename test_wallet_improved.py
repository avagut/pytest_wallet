"""Test the workings of the Wallet App."""


import pytest
from wallet import Wallet, InsufficientAmount


@pytest.fixture
def empty_wallet():
    """Create an empty wallet"""
    return Wallet()


@pytest.fixture
def loaded_wallet():
    """Create a loaded wallet"""
    return Wallet(50)


@pytest.mark.parametrize("added,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transactions(empty_wallet, added, spent, expected):
    """Does the wallet show the correct final balance after series run?
        This test continues from above."""
    empty_wallet.add_cash(added)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance == expected


def test_check_default_initial_amount(empty_wallet):
    """Is the default initial amount 100?"""
    assert empty_wallet.balance == 0


def test_check_loaded_initial_amount(loaded_wallet):
    """Is the initial amount equal to the passed amount?"""
    assert loaded_wallet.balance == 50


def test_check_updated_balance_on_add_cash(loaded_wallet):
    """Is the wallet updated with funds on adding of cash?"""
    loaded_wallet.add_cash(500)
    assert loaded_wallet.balance == 550


def test_check_updated_balance_on_spend_cash(loaded_wallet):
    """Is the wallet updated with funds on spending of cash?"""
    loaded_wallet.spend_cash(30)
    assert loaded_wallet.balance == 20


def test_spend_cash_raises_insufficient_error(loaded_wallet):
    """Does the wallet throw errors on trying to spend
        amount greater than balance?"""
    with pytest.raises(InsufficientAmount):
        loaded_wallet.spend_cash(1000)


def test_amount_passed_to_add_amount(loaded_wallet):
    """Does the wallet throw an error when a null
        amount is passed to the wallet methods?"""
    with pytest.raises(TypeError):
        loaded_wallet.spend_cash()
    with pytest.raises(TypeError):
        loaded_wallet.add_cash()
