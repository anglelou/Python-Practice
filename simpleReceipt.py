#Catalog details
lovely_loveseat_desc = "Lovely Loveseat. Tufted polyester blenc on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or White."
lovely_loveseat_price = 254.00

stlyish_settee_desc = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

luxurious_lamp_desc = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

sales_tax = 0.88

#First Customer
customer_one_total = 0
customer_one_itemization = ""

customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_desc
customer_one_total += luxurious_lamp_price
customer_one_itemization += ("\n\n" + luxurious_lamp_desc)

customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

#Printing receipt
print("Customer One Items: ")
print(customer_one_itemization)
print("\nCustomer One Total:")
print(round(customer_one_total,2))

