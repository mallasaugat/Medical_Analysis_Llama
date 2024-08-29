import csv
import os

with open("datasets/md-data.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)

    with open("datasets/md-data-statement.csv", 'w', newline='') as csvwrite:

        fieldnames = ['Statement','NoShow']
        writer = csv.DictWriter(csvwrite, fieldnames=fieldnames)
        
        writer.writeheader()

        next(reader)
        for row in reader:

            newList = list(row)
            newStatement = ""

            newStatement = (
                f"The patient is a {'male' if newList[2] == 'M' else 'female'}, aged {newList[5]}. "
                f"They have an appointment scheduled on {newList[3]} for the reason of {newList[4]}. "
                f"The patient has a history of hypertension: {'yes' if int(newList[8]) else 'no'}, "
                f"diabetes: {'yes' if int(newList[9]) else 'no'}, "
                f"alcoholism: {'yes' if int(newList[10]) else 'no'}, and a handicap: {'yes' if int(newList[11]) else 'no'}. "
                f"Additionally, they have received an SMS confirmation: {'yes' if int(newList[12]) else 'no'}."
            )

            
            writer.writerow({'Statement': newStatement, 'NoShow': newList[-1] })

