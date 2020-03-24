# Ground Shipping Cost
def ground_shipping(weight):
  if weight <= 2:
    return weight*1.50 + 20.00
  if 2 < weight <= 6:
    return weight*3.00 + 20.00
  if 6 < weight <= 10:
    return weight*4.00 + 20.00
  else:
    return weight*4.75 + 20.00

# Premium Ground Shipping Cost
premium_shipping_cost = 125

# Drone Shipping Cost
def drone_shipping(weight):
  if weight <= 2:
    return weight*4.50
  if 2 < weight <= 6:
    return weight*9.00 
  if 6 < weight <= 10:
    return weight*12.00 
  else:
    return weight*14.75

# Cheapest Shipping Method
def cheapest_shipping(weight):
  if ground_shipping(weight) < premium_shipping_cost and ground_shipping(weight) < drone_shipping(weight):
    return "The cheapest shipping method is ground shipping and it will cost $" + str(ground_shipping(weight)) 
  if drone_shipping(weight) < premium_shipping_cost and drone_shipping(weight) < ground_shipping(weight):
    return "The cheapest shipping method is drone shipping and it will cost $" + str(drone_shipping(weight))
  else:
    return "The cheapest shipping method is premium ground shipping and it will cost $" + str(premium_shipping_cost)