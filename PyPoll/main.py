import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath) as csvfile:
    electiondatafile = csv.reader(csvfile, delimiter=',')

    totalvotes= 0
    khantotalvotes = 0
    correytotalvotes = 0
    litotalvotes = 0
    otooleytotalvotes = 0

    # skip the header

    next(electiondatafile)


    # Read each line of the csv file

    for row in electiondatafile:
        totalvotes=totalvotes + 1

#calculating the total number of votes for each person

        if row[2] == "Khan":
            khantotalvotes = khantotalvotes + 1

        if row[2] == "Correy":
            correytotalvotes = correytotalvotes + 1

        if row[2] == "Li":
            litotalvotes = litotalvotes + 1
    
        if row[2] == "O'Tooley":
            otooleytotalvotes = otooleytotalvotes + 1

#calculating  voting percentage for each candidate


        khanpercentage = khantotalvotes / totalvotes * 100
        correypercentage = correytotalvotes / totalvotes * 100
        lipercentage = litotalvotes / totalvotes * 100
        otooleypercentage = otooleytotalvotes / totalvotes * 100

#compare each candidate's total votes value to see who won
        if khantotalvotes > correytotalvotes and khantotalvotes > litotalvotes and khantotalvotes > otooleytotalvotes:
            winner = "Khan"

        if correytotalvotes > khantotalvotes and correytotalvotes > litotalvotes and correytotalvotes > otooleytotalvotes:
            winner = "Correy"

        if litotalvotes > khantotalvotes and litotalvotes > correytotalvotes and litotalvotes > otooleytotalvotes:
            winner = "Li"

        if otooleytotalvotes > khantotalvotes and otooleytotalvotes > correytotalvotes and otooleytotalvotes > litotalvotes:
            winner = "O'Tooley"
    
    # print the final results to the screen
    print("Election Results")
    print(" -------------------------")
    print(f"Total Votes: {totalvotes}")
    print(" -------------------------")
    print(f"Khan: {khanpercentage:.3f} % ({khantotalvotes})")
    print(f"Correy: {correypercentage:.3f} % ({correytotalvotes})")
    print(f"Li: {lipercentage:.3f} % ({litotalvotes})")
    print(f"O'Tooley: {otooleypercentage:.3f} % ({otooleytotalvotes})")
    print(" -------------------------")
    print(f" Winner: {winner}")
    print(" -------------------------")

    # Write results to a file
resultsfile = os.path.join("analysis", "pollingresults.txt")
with open(resultsfile, "w",) as textfile:
    textfile.write(f"Election Results\n")
    textfile.write(f"-------------------------\n")
    textfile.write(f"Total Votes: {totalvotes}\n")
    textfile.write(f"-------------------------\n")
    textfile.write(f"Khan: {khanpercentage:.3f} % ({khantotalvotes})\n")
    textfile.write(f"Correy: {correypercentage:.3f} % ({correytotalvotes})\n")
    textfile.write(f"Li: {lipercentage:.3f} % ({litotalvotes})\n")
    textfile.write(f"O'Tooley: {otooleypercentage:.3f} % ({otooleytotalvotes})\n")
    textfile.write(f"-------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write(f"-------------------------\n")