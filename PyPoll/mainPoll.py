# create a Python script that analyzes the votes and calculates each of the following
import os
import csv

# File path
csv_file = os.path.join("Resources","PyPoll.csv")
#print(csvpath)

# Open/Read CSV file
with open(csv_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")     
    
    # Skip header row
    csv_header = next(csvfile)
     
    #Declare variables
    candidates = {}
    count = 0
    votes_cast = 0
    percent_of_votes = 0
    most_votes = 0
    popular_vote = ""
        
    for row in csvreader:
        
        # The total number of votes cast
        candidate = row[2]
        count += 1
        if candidate in candidates.keys():
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
            
    #A complete list of candidates who received votes
    # The winner of the election based on popular vote.
    print("Election Results")
    print("-------------------------------")
    print(f"Total Votes: {count}")
    print("-------------------------------")

    for candidate in candidates:
        votes_cast += candidates[candidate]
    
        # The percentage of votes each candidate won
        percent_of_votes = (candidates[candidate])/(count) * 100
        print(f"{candidate}: {int(percent_of_votes)}% {votes_cast}")
        
        if candidates[candidate] > most_votes:
            popular_vote = candidate
            most_votes = candidates[candidate]

    print("-------------------------------")
    
    print(f"Winner: {popular_vote}")
    
    print("-------------------------------")

    # export a text file with the results
output_file = "Analysis/elections_file.txt"

with open(output_file,"w") as file:

    file.write("Election Results\n")
    file.write("-------------------------------\n")
    file.write(f"Total Votes: {count}\n")
    file.write("-------------------------------\n")

    for candidate in candidates:
        votes_cast += candidates[candidate]
    
        # The percentage of votes each candidate won
        percent_of_votes = (candidates[candidate])/(count) * 100
        file.write(f"{candidate}: {int(percent_of_votes)}% {votes_cast}\n")
        
        if candidates[candidate] > most_votes:
            popular_vote = candidate
            most_votes = candidates[candidate]

    file.write("-------------------------------\n")
    
    file.write(f"Winner: {popular_vote}\n")
    
    file.write("-------------------------------")
