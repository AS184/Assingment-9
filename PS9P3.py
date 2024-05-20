def calculate_miles_per_gallon(miles, gallons):
    mpg = miles / gallons
    return mpg

trips = 0
gallons = 0
miles = 0
for trips in range(1,4,1):
    print("Enter a city ")
    city = input()
    print("Enter miles traveled ")
    miles = int(input())
    print("Enter gallons used  ")
    gallons = int(input())
    mpg = calculate_miles_per_gallon(miles, gallons)
    print("Destination " + city + " has a batting average of " + str(mpg))
print("Number of places traveled: ", trips)