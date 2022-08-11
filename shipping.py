weight = 41.5
ground_premium = 125.00

# Ground shipping
if weight <= 2.0:
  print('Ground Shipping: $',round((weight*1.50+20),2))
elif weight > 2 and weight <= 6:
  print('Ground Shipping: $',round((weight*3.00+20),2))
elif weight > 6 and weight <= 10:
  print('Ground Shipping: $',round((weight*4.00+20),2))
elif weight > 10:
  print('Ground Shipping: $',round((weight*4.75+20),2))

# Premium
print('Ground Shipping Premium: $', ground_premium)

# Drone Shipping
if weight <= 2.0:
  print('Drone Shipping: $',round((weight*4.50),2))
elif weight > 2 and weight <= 6:
  print('Drone Shipping: $',round((weight*9.00),2))
elif weight > 6 and weight <= 10:
  print('Drone Shipping: $',round((weight*12.00),2))
elif weight > 10:
  print('Drone Shipping: $',round((weight*14.25),2))

