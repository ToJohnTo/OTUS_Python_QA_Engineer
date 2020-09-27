import csv

with open('eggs.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',',)

    writer.writerow(['data', 'result', 'code'])
    for i in range(10):
        writer.writerow([i, i * 100, str(bin(i))])
