import csv

from os import walk
import os

def getResult():

    filenames = next(walk("./predictions"), (None, None, []))[2]  # [] if no file
    print(filenames)
    file = ""

    for filename in filenames:
        if filename[:4] == "cast":
            file = filename
            break

    if file:

        with open("predictions/" + file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            result = []
            for i, row in enumerate(csv_reader):
                if i == 1:
                    result = row

            print(result)

            for filename in filenames:
                os.remove("predictions/" + filename)  
            return(result)

 
    
    return None
            

        # for row in csv_reader:
        #     if line_count == 0:
        #         print(f'Column names are {", ".join(row)}')
        #         line_count += 1
        #     else:
        #         print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
        #         line_count += 1
        # print(f'Processed {line_count} lines.')