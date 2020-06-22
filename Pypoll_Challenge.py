
#Add our dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# CHALLENGE: Initialize total_votes, candidate options, counties and county votes
total_votes = 0
Candidate_options = []
Candidate_votes = {}
County_options = []
County_votes = {}


#CHALLENGE: Determining winning candidate, vote count, vote % and winning county.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0
#Open the file results and read the file
with open (file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the Header Row
    headers =next(file_reader)
    
    #Read the rows in the file_reader
    for row in file_reader:
        #Add the total votes to the count
        total_votes +=1

        #Find which row contains the candidate names: CHALLENGE: Find what row contains the County names
        Candidate_name = row[2]
        County_name =row[1]
        #Check to see if the candidate is in the list or not
        if Candidate_name not in Candidate_options:

            #If not, then add it.
            Candidate_options.append(Candidate_name)
            
            #Begin tracking that candidate's votes
            Candidate_votes [Candidate_name] = 0
        Candidate_votes [Candidate_name] += 1

            #CHALLENGE: look to see if the county is in the list of not
        if County_name not in County_options:

                #CHALLENGE: If not, then add the county name to the list of Counties
            County_options.append(County_name)
           
            #CHALLENGE: Begin keeping track of the number of votes in each County
            County_votes [County_name] = 0
        County_votes [County_name] +=1
#Save the file to a txt file
with open(file_to_save, "w") as txt_file:

     # Print the final vote count.
    election_results =(
        f"\nElection Results\n"
        f"--------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------\n"
        f"\nCounty Votes:\n")

    #Print the election results to the terminal
    print(election_results, end ="")
    
    #Wite the election results to the analysis txt.file
    txt_file.write(election_results)

      #CHALLENGE: First iterate through and get the results for each County
    for county in County_votes:

        #CHALLENGE: Retrieve the vote count for each County
        Votes_per_county = County_votes[county]
            #CHALLENGE: Calculate the percentage of votes for each county
        County_vote_percentage = float(Votes_per_county) / float(total_votes) * 100
        
            #CHALLENGE: Create a statement to hold the Results for each County
        County_results = (
            f"{county}: {County_vote_percentage:.1f}% ({Votes_per_county:,})\n")
        #CHALLENGE: Print the county results to the terminal
        print(County_results)

        #CHALLENGE: write the county results to the txt file
        txt_file.write(County_results)
        #CHALLENGE: Calculate the number of votes for the winning county
        if (Votes_per_county > winning_county_count) and (County_vote_percentage > winning_county_percentage):
            winning_county_count = Votes_per_county
            winning_county_percentage = County_vote_percentage
            winning_county = county
    
    #Challenge: Create a summary to print out the winning County
    Winning_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")

    #CHALLENGE: Print the winning counties to the terminal
    print(Winning_county_summary)

    #CHALLENGE: write the winning county summary to the txt.File
    txt_file.write(Winning_county_summary)

    #Iterate though the candidates list to find candidates

    for candidate in Candidate_votes:

        # 2. Retrieve the vote count for each candidate
        votes = Candidate_votes[candidate]

        # 3 Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
        Candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
     
        #Write the Candidate Results to the TXT file
        txt_file.write(Candidate_results)
       
        #Calculate the winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):

        #Make the winning count that # of votes, and the winning percentage that current vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
    #Create a space to hold the winning candidate summary
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    #Print the winning candidate summary to the terminal
    print(winning_candidate_summary)

    #write the winning candidate summary to the txt.file
    txt_file.write(winning_candidate_summary)

  
    
