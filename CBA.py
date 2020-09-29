def ground_shipping_cost(weight):
  cost = 20.00
  if weight <= 2:
    return cost+weight*1.50
  if 2 < weight <= 6:
    return cost+weight*3.00
  if 6 < weight <= 10:
    return cost+weight*4.00
  if weight > 10:
    return cost+weight*4.75

print(ground_shipping_cost(3.1))

premium_shipping_cost = 125.00

def drone_shipping_cost(weight):
  if weight <= 2:
    return weight*4.50
  if 2 < weight <= 6:
    return weight*9.00
  if 6 < weight <= 10:
    return weight*12.00
  if weight > 10:
    return weight*14.25

print(drone_shipping_cost(3.1))

def cost_benefit_analysis(weight):
  if weight <=3.33333:
    return "Drone Shipping is cheaper at $" + str(drone_shipping_cost(weight))
  if 3.33333 < weight < 22.1:
    return "Ground shipping is cheaper at $" + str(ground_shipping_cost(weight))
  if weight > 22.1:
    return "Premium shipping is cheaper at $125"

print(str(cost_benefit_analysis(4.8)))
