import csv

file1 = open('get_news.txt','r+')
news1 = file1.read()

with open('news_to_be_tested.csv', mode='w+') as e_file:
    e_writer = csv.writer(e_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    e_writer.writerow([news1])
