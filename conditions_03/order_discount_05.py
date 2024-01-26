# order discount program
item_cost = 200
item_qty = 3
special_client = 0      # 1 : Special 20%       0 : Not Special 10%
# calculate total order cost
total_order_cost = item_cost * item_qty
if total_order_cost >= 1000:
    if special_client == 1: # special 20%
        discount_pct = 20
    else:                   # not special 10%
        discount_pct = 10
else:
    discount_pct = 0
discount_val = total_order_cost * discount_pct / 100
print('Total before discount ', total_order_cost)
total_order_cost = total_order_cost - discount_val
print('discount pct ', discount_pct)
print('discount value ', discount_val)
print('Total after discount ', total_order_cost)