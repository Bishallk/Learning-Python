
# A megastore offers three types of discounts, which
# are represented as DiscountType enum.
# Implement the get _ discounted _ price function
# which should take the total weight of the shopping
# cart, the total price, and the discount type. It should
# return the final discounted price based on the
# discount schemes as shown in the promotional
# video below:
# Weight Discount :
## If weight>10 ->18% Dis
## If weight<=1010 ->6% Dis
#Standard Discount:

## If weight=any ->6% Dis
#SEasonal 
## If weight=any ->12% Dis

from enum import Enum, auto

class DiscountType(Enum):
    STANDARD = auto()
    SEASONAL = auto()
    WEIGHT = auto()

def get_discounted_price(cart_weight, total_price, discount_type):
    discount_perc=None
    if discount_type==DiscountType.WEIGHT:
        if cart_weight>10:
            discount_perc=18
        elif cart_weight<=10:
            discount_perc=6
    elif discount_type==DiscountType.SEASONAL:
        discount_perc=12
    elif discount_type==DiscountType.STANDARD:
        discount_perc=6

    price_after_dis=total_price - (discount_perc*100)/total_price
        
    return price_after_dis

        
print(get_discounted_price(12, 100, DiscountType.WEIGHT))
print(get_discounted_price(13, 10000, DiscountType.SEASONAL))
print(get_discounted_price(12, 10033, DiscountType.STANDARD))
print(get_discounted_price(6, 1000, DiscountType.WEIGHT))