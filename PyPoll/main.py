import os
import csv

# Join the file in present pathway
election_data_csv = os.path.join('election_data.csv')

#notes: columns: [0] Voter ID, [1] County, [2] Candidate

candidate = {}


# read the file
with open (election_data_csv, encoding ='utf') as election_data_csv_file:
    # use comma as the delimiter
    csvreader = csv.reader(election_data_csv_file, delimiter = ",")
    # jump to next as the first row is the column headers
    header = next(csvreader)
    
#----------- Find the total number of votes ----------

        
    for row in csvreader:
        
        if row[2] not in candidate.keys():
            
            candidate[row[2]] = 1
        else:
            candidate[row[2]] = candidate[row[2]] + 1
            
            
##---------- Find the candidates names ---------------  
 
    print(candidate.keys())
   


    vote_sum = list(candidate.values())
    #print(vote_sum)
   # percentage = list(((candidate.values())/369711)*100)
   
   
    s = sum(candidate.values())
    for k, v in candidate.items():
        percentage = "{:.3f}".format(v * 100.0 / s)
        print(percentage)
        print(k+' : '+str(percentage)+ "%" +"("+str(v)+")")
            
   
####--------------- Find the winner ---------------------

    total_votes = sum(vote_sum)
    winner = list(candidate.keys())[vote_sum.index(max(vote_sum))]

#print(total_votes)  
#print(candidate)
#print(winner)


#!Notes! below the instrctions:
#Commands to print all the details with dates in the Terminal:
print('Election Results')
print('-------------------------')
print(f" Total Votes: {total_votes}")
print('-------------------------')
for k,v in candidate.items():
    percentage = "{:.3f}".format(v * 100.0 / s)
    print(k+' : '+str(percentage)+"%" +"("+str(v)+")")
print('----------------------------')
print(f" Winner: {winner}")
print('----------------------------')

#Commands to also save it saved file.txt in a folder called 'analysis' , how to do it:
#find here: https://www.kite.com/python/answers/how-to-write-a-file-to-a-specific-directory-in-python
save_path = 'analysis'
file_name = "Election.txt"
completeName = os. path. join(save_path, file_name)
print(completeName)
file1 = open(completeName, "w")
# how to start with a new line find here: https://www.kite.com/python/answers/how-to-write-a-string-to-a-file-on-a-new-line-every-time-in-python
file1.write('Election Results\n')
file1.write('----------------------------\n')
file1.write(f" Total Votes: {total_votes}\n")
file1.write('----------------------------\n')
# you hvae to loop here again to be able to print the names and percentage as values!
for k,v in candidate.items():
    percentage = "{:.3f}".format(v * 100.0 / s)
    file1.write(k+' : '+str(percentage)+"%" +"("+str(v)+")\n")
file1.write('----------------------------\n')
file1.write(f" Winner: {winner}\n")
file1.write('----------------------------\n')

file1 = open(completeName)
file1.close()
