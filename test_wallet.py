"""Test the workings of the Wallet App."""


import pytest
from wallet import Wallet, InsufficientAmount

def test_check_default_initial_amount():
    """Is the default initial amount 100?"""
    wallet = Wallet()
    assert wallet.balance == 0
    
def test_check_loaded_initial_amount():
    """Is the initial amount equal to the passed amount?"""
    wallet = Wallet(500)
    assert wallet.balance == 500
    
def test_check_updated_balance_on_add_cash():
    """Is the wallet updated with funds on adding of cash?"""
    wallet = Wallet(100)
    wallet.add_cash(500)
    assert wallet.balance == 600    

def test_check_updated_balance_on_spend_cash():
    """Is the wallet updated with funds on spending of cash?"""
    wallet = Wallet(100)
    wallet.spend_cash(30)
    assert wallet.balance == 70    
    
def test_spend_cash_raises_insufficient_error():
    """Does the wallet throw errors on trying to spend amount greater than balance?"""
    wallet = Wallet(100)
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(1000)
        
def test_amount_passed_to_add_amount():
    """Does the wallet throw an error when a null amount is passed to the wallet methods?"""
    wallet = Wallet(100)
    with pytest.raises(TypeError):
        wallet.spend_cash()    
    with pytest.raises(TypeError):
        wallet.add_cash()    
        