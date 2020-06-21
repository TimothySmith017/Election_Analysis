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

# 1.) Initialize total_votes to 0 & other shit.
total_votes = 0
Candidate_options = []
Candidate_votes = {}

#Determining winning Candidate and winning vote %
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#Open the file results and read the file
with open (file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the Header Row
    headers =next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        # 2. Add the total votes to the count
        total_votes +=1
        #Print candidate name in each row
        Candidate_name = row[2]

        #Check to see if the candidate is in the list or not
        if Candidate_name not in Candidate_options:

            #If not, then add it.
            Candidate_options.append(Candidate_name)

            #Begin tracking that candidate's votes
            Candidate_votes [Candidate_name] = 0
        Candidate_votes [Candidate_name] += 1
       

        #Getting the percentage of votes

    #1.) Iterate though the candidates list

for candidate in Candidate_votes:

    # 2. Retrieve the vote count for each candidate
    votes = Candidate_votes[candidate]

    # 3 Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100



    # To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
    print(f"{candidate}: {vote_percentage:.1f}% {votes:,}\n")

    #   FINIDNG THE WINNING CANDIDATE AND THE WINNING PERCENTAGE
    #If the votes are greater than the winning count, and the vote percentage is higher than the win %
    if (votes > winning_count) and (vote_percentage > winning_percentage):

    #Make the winning count that # of votes, and the winning percentage that current vote percentage
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


 #print candidate name and the percentage of the number of votes
   # print(f"{candidate} recieved {vote_percentage:.2f} % of the vote.")



#Print the Candidate Votes
#print(Candidate_votes)



#Print the Candidates list
#print(Candidate_options)


# 3. Print the total votes
#print(total_votes)


