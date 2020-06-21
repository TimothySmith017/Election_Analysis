counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#Get the keys using a for loop
for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county, voters)

for county, voters in counties_dict.items():
    print(county, f"county has {voters} registered voters")


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#Iterating over a list of dictionaires by using the range() method
for i in range(len(voting_data)):
     print(voting_data[i])
    
    #WHAT IS THIS DOING? For each dictionary in our list, loop through each value in those dictionaires and print the values
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#Printing only the county names from the county dictionary
for county_dict in voting_data:
    print(county_dict['county'])