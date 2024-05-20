control = str(input("Enter yes to loop or no to exit:  "))
x = 0
while control == "yes":
  lname = str(input("Enter your last name: "))
  jobcode = str(input("Enter your job code (L, A or J): "))
  hours = float(input("Enter hours worked: "))
  x = x + 1
  control = str(input("Enter yes to loop or no to exit:  "))
  #print("You have run this program ", x, " times")

if control == "no" and x >= 1:
  if jobcode == "L":
     payrate = 25
  elif jobcode == "A":
     payrate = 30
  elif jobcode == "J":
    payrate = 50
  grosspay = payrate * hours

  overtime = hours + (hours/2)
  
  if jobcode == "L" and hours > 25:
    total = overtime + grosspay
  else:
    total = grosspay

  if jobcode == "A" and hours > 30:
    total = overtime + grosspay
  else:
    total = grosspay

  if jobcode == "J" and hours > 50:
    total = overtime + grosspay
  else:
    total = grosspay
  
    


#grosspay = payrate * hours

#overtime = hours + (hours/2)

#if jobcode == "L" and hours > 25:
  #total = overtime + grosspay
#else:
  #total = grosspay
  
#if jobcode == "A" and hours > 30:
  #total = overtime + grosspay
#else:
  #total = grosspay
  
#if jobcode == "J" and hours > 50:
 # total = overtime + grosspay
#else:
 # total = grosspay





if control == "no" and x >= 1:
  print(lname, "has a job code of", jobcode, "with a payrate of $", payrate, "making a gross pay of", grosspay, "earning $", overtime, "of overtime", "and a total of $", total)
  print("You have run this program ", x, " times")
else:
  print("You have run this program ", x, " times")

#control = str(input("Enter yes to loop or no to exit:  "))
#print("You have run this program ", x, " times")