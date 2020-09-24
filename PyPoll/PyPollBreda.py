# Modules
import os
import csv

# Establish file path to election_data.csv
csvpath = os.path.join('Resources', 'election_data.csv')

# Open the election_data.csv file using CSV module
with open(csvpath) as csv_file:
    election_data = csv.reader(csv_file, delimiter=',')

# Sets the header row
    header_row = next(election_data)

# Sets lists from the csv file to perform summary calculations upon
    all_rows = list(election_data)
    lists = list(zip(*all_rows))
    voter_ids = lists[0]
    counties = lists[1]
    candidates = lists[2]

# Sets a variable for total votes
    total_votes = len(voter_ids)

# Creates a list of all unique candidates
    unique_candidates = list(set(candidates))

# Creates a tally_totals function for counting votes and displaying results for each unique candidate
    def tally_totals(total_votes):
        vote_tally = 0
        for unique_candidate in unique_candidates:
            for candidate in candidates:
                if candidate == unique_candidate:
                    vote_tally += 1
            vote_percentage = vote_tally / total_votes
            print(unique_candidate + ': {:.1%}'.format(vote_percentage) + ' - {:,}'.format(vote_tally))
            vote_tally = 0

# Creates a declare_winner function
    def declare_winner():
        highest_votes = 0
        winner = 0
        vote_tally = 0
        for unique_candidate in unique_candidates:
            for candidate in candidates:
                if candidate == unique_candidate:
                    vote_tally += 1
                    if vote_tally > highest_votes:
                        highest_votes = vote_tally
                        if highest_votes == vote_tally:
                            winner = unique_candidate
            vote_tally = 0
        print(f'Winner: {winner}')

# Prints out election summary

    dash_line = '_ _ _ _ _ _ _ _ _ _ _ _'

    print(f'{dash_line}')
    print(f'ELECTION RESULTS')
    print(f'{dash_line}')
    print('Total Votes: {:,}'.format(total_votes))
    print(f'{dash_line}')
    tally_totals(total_votes)
    print(f'{dash_line}')
    declare_winner()
    print(f'{dash_line}')

# Creates a text file with the election summary
    print(f'{dash_line}', file=open("election_summary.txt","w"))
    print(f'ELECTION RESULTS', file=open("election_summary.txt","a"))
    print(f'{dash_line}', file=open("election_summary.txt","a"))
    print('Total Votes: {:,}'.format(total_votes), file=open("election_summary.txt","a"))
    print(f'{dash_line}', file=open("election_summary.txt","a"))
    print(f'{dash_line}', file=open("election_summary.txt","a"))
    print(f'{dash_line}', file=open("election_summary.txt","a"))





            






    