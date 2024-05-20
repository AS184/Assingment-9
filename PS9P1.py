def calculate_total_cost(quantity, price):
  total = quantity * price
  if total > 10000:
    total = total - (total * 0.10)
  return total

eprice = 0
loop = input("Do you want to run this program? (y/n)  ")
while loop == "y":
  quantity = int(input("Enter the quantity "))
  price = float(input("Enter the price "))
  totalcost= calculate_total_cost(quantity, price)
  print(totalcost)
  print("Quantity purchased ", quantity, "Price per unit $", "{:2F}".format(price), "Total is $", "{:2F}".format(totalcost))
  eprice = eprice + totalcost
  loop = input("Do you want to run this program again? (y/n)  ")
  