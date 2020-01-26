from datetime import datetime, timedelta

import pytest

from ocp import Customer, calculate_discount_percentage

YEAR = timedelta(days=365)

@pytest.fixture
def now():
    return datetime.now()

def test_should_return_zero_for_casual_customer(now):
    customer = Customer(
        first_purchase_date=now,
        birth_date=now-20*YEAR,
        is_veteran=False,
    )
    got = calculate_discount_percentage(customer)
    expected = 0
    assert got == expected

def test_should_return_15_for_new_client(now):
    customer = Customer(
        first_purchase_date=None,
        birth_date=now-20*YEAR,
        is_veteran=False,
    )
    got = calculate_discount_percentage(customer)
    expected = 15
    assert got == expected

def test_should_return_10_for_veteran(now):
    customer = Customer(
        first_purchase_date=now,
        birth_date=now-20*YEAR,
        is_veteran=True,
    )
    got = calculate_discount_percentage(customer)
    expected = 10
    assert got == expected

def test_should_return_5_for_a_senior(now):
    customer = Customer(
        first_purchase_date=now,
        birth_date=now-65*YEAR,
        is_veteran=False,
    )
    got = calculate_discount_percentage(customer)
    expected = 5
    assert got == expected

def test_should_return_10_for_a_loyal_customer(now):
    customer = Customer(
        first_purchase_date=now-1*YEAR,
        birth_date=now-20*YEAR,
        is_veteran=False,
    )
    got = calculate_discount_percentage(customer)
    expected = 10
    assert got == expected

def test_should_return_12_for_a_more_loyal_customer(now):
    customer = Customer(
        first_purchase_date=now-5*YEAR,
        birth_date=now-20*YEAR,
        is_veteran=False,
    )
    got = calculate_discount_percentage(customer)
    expected = 12
    assert got == expected

def test_should_return_20_for_a_most_loyal_customer(now):
    customer = Customer(
        first_purchase_date=now-10*YEAR,
        birth_date=now-20*YEAR,
        is_veteran=False,
    )
    got = calculate_discount_percentage(customer)
    expected = 20
    assert got == expected

def test_should_return_maximum_discount(now):
    customer = Customer(
        first_purchase_date=None,
        birth_date=now-20*YEAR,
        is_veteran=True,
    )
    # eligible for 15% discount as a new client and 10% as a veteran
    got = calculate_discount_percentage(customer)
    expected = 15
    assert got == expected