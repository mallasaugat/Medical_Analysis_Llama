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

            newStatement += (
            f"Gender: {'Male' if newList[2] == 'M' else 'Female'}, "
            f"Age: {newList[5]}, "
            f"Appointment Date: {newList[3]}, "
            f"Reason: {newList[4]}, "
            f"Hypertension: {'YES' if int(newList[8]) else 'NO'}, "
            f"Diabetes: {'YES' if int(newList[9]) else 'NO'}, "
            f"Alcoholism: {'YES' if int(newList[10]) else 'NO'}, "
            f"Handicap: {'YES' if int(newList[11]) else 'NO'}, "
            f"SMS Received: {'YES' if int(newList[12]) else 'NO'}."
        )

            
            writer.writerow({'Statement': newStatement, 'NoShow': newList[-1] })

