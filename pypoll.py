import csv
import os

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

#Write some data to the file
    #txt_file.write("Hello World")


# Write three counties to the file.
    #txt_file.write("Arapahoe")
    #txt_file.write("Denver")
    #txt_file.write("Jefferson")

#Separatong with comma
    #txt_file.write ("Arapahoe, ")
    #txt_file.write ("Denver, ")
    #txt_file.write ("Jefferson, ")

    #All on one line

    #txt_file.write ("Arapahoe, Denver, Jefferson")

#getting new lines: Use the NEW LINE framework: \n
    #txt_file.write("Arapahoe\nDenver\nJefferson")

    #SKILL DRILL.
    #txt_file.write("Counties in the Election\n")
    #txt_file.write("-----------------\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")


    #TIME TO READ THE RESULTS CSV

    #Add our dependencies
    import csv
    import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the file results and read the file
#with open (file_to_load) as election_data:

    #To do: read and analyze the data here.

    #Read the file_object with the reader function.
    #file_reader = csv.reader(election_data)

    #Print each row of the CSV file
    #for row in file_reader:
       # print(row)

    #Get just the first element of each row.
    #for row in file_reader:
         #print(row[0])
    
    #Print the header row.
    #headers = next(file_reader)
    #print(headers)

#EVERYTHING: JUST CLEANER NOW

#Add our dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the file results and read the file
with open (file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read and print headers row
    headers =next(file_reader)
    print(headers)
    