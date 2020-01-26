from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional

import pytest


@dataclass
class Customer:
    first_purchase_date: Optional[datetime]  # datetime or None
    birth_date: datetime
    is_veteran: bool
        
    # @dataclass decorator automagically generates the following constructor:
    # def __init__(self, first_purchase_date, birth_date, is_veteran):
    #     self.first_purchase_date = first_purchase_date
    #     self.birth_date = birth_date
    #     self.is_veteran = is_veteran

def calculate_discount_percentage(customer):
    discount = 0
    now = datetime.now()
    year = timedelta(days=365)
    if customer.birth_date <= now - 65*year:
        # senior discount
        discount = 5
    if customer.first_purchase_date is not None:
        if customer.first_purchase_date <= now - year:
            # after one year, loyal customers get 10%
            discount = 10
            if customer.first_purchase_date <= now - 5*year:
                # after five years, 12%
                discount = 12
                if customer.first_purchase_date <= now - 10*year:
                    # after ten years, 20%
                    discount = 20
    else:
        # first time purchase ==> 15% discount
        discount = 15
    if customer.is_veteran:
        discount = max(discount, 10)
    return discount