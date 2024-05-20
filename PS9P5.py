control = str(input("Enter yes to loop or no to exit:  "))
x = 0
while control == "yes":
  lname = str(input("Enter your last name: "))
  credithour = float(input("Enter the number of credit hours earned: "))
  districtcode = str(input("Enter your district code (I or O): "))
  x = x + 1
  control = str(input("Enter yes to loop or no to exit:  "))


if control == "no" and x >= 1:
  if districtcode == "I":
     credithourworth = 250
  elif districtcode == "O":
    credithourworth = 550
  else:
    credithour = 0
  tuition = credithour * credithourworth





if control == "no" and x >= 1:
  print(lname,"has a district code of", districtcode, "each credit hour worth $", credithour ,"with a tuition of $", tuition)
else:
  print("You have run this program ", x, " times")
  