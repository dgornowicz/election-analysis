# Add dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Declare candidate options list
candidate_options = []

# Declare empty candidate votes dictionary
candidate_votes = {}

# Declare winning candidate and winning count tracker variables
winning_candidate = ''
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            
            # Add it to the list of candidates
            candidate_options.append(candidate_name)

            # Begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0


        # Add a vote to that candidates count
        candidate_votes[candidate_name] += 1

# Save the results to text file
with open(file_to_save,'w') as txt_file:

    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    
    print(election_results, end="")
    
    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine vote percentages
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        # Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # Assign candidate results to variable
        candidate_results = (f'{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n')

        # Print candidate results to terminal
        print(candidate_results)

        # Save candidate results to text file
        txt_file.write(candidate_results)

        # Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            
            # If true then set winning count = votes and winning percentage = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            
            # Set the winning candidate equal to the candidates name
            winning_candidate = candidate_name

    # Print winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    # Save the winning candidates name to the text file
    txt_file.write(winning_candidate_summary)