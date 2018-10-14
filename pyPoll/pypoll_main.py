import csv
import os

csvfile = "election_data.csv"

voter_id_list = []
county_list = []
voted_for_list = []

with open(csvfile,newline = '') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        voter_id_list.append(row[0])
        county_list.append(row[1])
        voted_for_list.append(row[2])

print("""Election Results
-------------------------------------""")
#Total votes
total_votes = len(voter_id_list)

print(f"Total Votes: " + str(total_votes))
print("-------------------------------------")

#List of candidates receiving votes
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
total_votes_range = range(total_votes)

for vote in total_votes_range:
    if voted_for_list[vote] == "Khan":
        khan_votes = khan_votes + 1
    else:
        if voted_for_list[vote] == "Correy":
            correy_votes = correy_votes + 1
        else:
            if voted_for_list[vote] == "Li":
                li_votes = li_votes + 1
            else:
                if voted_for_list[vote] == "O\'Tooley":
                    otooley_votes = otooley_votes + 1

khan_percent = '{0:.2f}'.format((khan_votes/total_votes))
correy_percent = '{0:.2f}'.format((correy_votes/total_votes))
li_percent = '{0:.2f}'.format((li_votes/total_votes))
otooley_percent = '{0:.2f}'.format((otooley_votes/total_votes))


print("Khan: " + str(khan_percent) + " (" + str(khan_votes) +")")
print("Correy: " + str(correy_percent) + " (" + str(correy_votes)+")")
print("Li: " + str(li_percent) + " (" + str(li_votes) + ")")
print("O'Tooley: " + str(otooley_percent) + " (" + str(otooley_votes)+ ")")

print("-------------------------------------")


