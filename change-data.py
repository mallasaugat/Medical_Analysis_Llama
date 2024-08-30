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
                f"Patient Information:\n"
                f"- Gender: {'Male' if newList[2] == 'M' else 'Female'}\n"
                f"- Age: {newList[5]}\n"
                f"- Appointment Date: {newList[3]}\n"
                f"- Scheduled For: {newList[4]}\n"
                f"- Medical Conditions:\n"
                f"  * Hypertension: {'YES' if int(newList[8]) else 'NO'}\n"
                f"  * Diabetes: {'YES' if int(newList[9]) else 'NO'}\n"
                f"  * Alcoholism: {'YES' if int(newList[10]) else 'NO'}\n"
                f"- Handicap: {'YES' if int(newList[11]) else 'NO'}\n"
                f"- SMS Reminder Sent: {'YES' if int(newList[12]) else 'NO'}"
            )

            
            writer.writerow({'Statement': newStatement, 'NoShow': newList[-1] })

