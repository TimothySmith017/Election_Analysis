temperature = int(input("What is the temperature outside"))
if temperature > 80:
    print("Turn on the AC")
else:
    print("Open the windows")

#What is the Score?
score = int(input("What is your letter grade"))
#Determine the Letter Grade
if score >=90:
    print('Your grade is an A')
elif score >=80:
    print("your grade is a B")
elif score >=70:
    print("your grade is a C")
elif score >=60:
    print("your grade is a D")
else:
    print("Your grade is an F")

#Check if something is IN a list
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

#If both are in a list
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

#If EITHER are in a list
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")