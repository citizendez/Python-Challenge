import os
import csv

csvpath = os.path.join("..", "Resources", "web_starter.csv")

#new lists
title = []
price = []
subscriber_count = []
reviews = []
review_percent = []
length = []


with open(csvpath, newline ='', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    for row in csvreader:

        
        course_title = row[1]
        course_price = row[4]
        course_sub_count = row[5]
        course_reviews = row[6]
        
        title.append(course_title)
        
        price.append(course_price)
        
        subscriber_count.append(course_sub_count)
        
        reviews.append(course_reviews)
        
        percent = round(float(course_reviews)/float(course_sub_count), 2)
        review_percent.append(percent)
        
        new_length = row[9].split(" ")
        length.append(float(new_length[0]))
        
#zip file        
New_csv = zip(title, price, subscriber_count, reviews, review_percent, length )

# Set variable for output file
output_file = os.path.join("web_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

        # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])


    # Write in zipped rows
    writer.writerows(New_csv)



        