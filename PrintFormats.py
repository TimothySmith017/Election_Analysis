#Printing total votes in an election more efficiently by using f-strings
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#Printing a message to a candidate with multiple lined f-strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"you received {candidate_votes:,} number of votes. "
    f"The total number of votes in th election was {total_votes:,}. "
    f"you received {candidate_votes / total_votes * 100:.2f} percent of the vote. ")

print(message_to_candidate)

#f'{value:{width}.{precision}}' -> used to format a value to a certain precision.

