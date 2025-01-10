# -*- coding: UTF-8 -*-

import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join('Resources /election_data.csv')
file_to_output = os.path.join('analysis', 'election_analysis.txt')



# Initialize variables to track the election data
total_votes = 0
candidate_votes = {}

# Open the CSV file and process it
with open(file_to_load) as election_data:
    csv_reader = csv.reader(election_data)

    # Skip the header row
    header = next(csv_reader)

    # Loop through each row of the dataset and process it
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]  # Assuming "candidate" is the third column

        # Update candidate vote count
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Determine the winner
winner = max(candidate_votes, key=candidate_votes.get)

# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

