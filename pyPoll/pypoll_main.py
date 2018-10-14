import csv
import os

csvfile = "election_data.csv"

voter_id_list = []
county_list = []
candidate_list = []

with open(csvfile,newline = '') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        voter_id_list.append(row[0])
        county_list.append(row[1])
        candidate_list.append(row[2])

#Total votes
total_votes = len(voter_id_list)

print(f"Total Votes: " + str(total_votes))

#List of candidates receiving votes
