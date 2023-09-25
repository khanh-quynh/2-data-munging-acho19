import csv

def main():
    f = open("./data/clean_data.csv","r")
    csv_reader = csv.DictReader(f)
    csv_list = list(csv_reader)

    for current_decade in range(1880,2023,10):
        year_count = 0
        sum_anomly_decade = 0
        for line in csv_list:
            if (int(line['Year'])//10)*10 == current_decade:
                year_count+=1
                avg_anomly_year = (float(line['Jan']) + float(line['Feb']) + float(line['Mar']) + float(line['Apr']) + float(line['May']) + float(line['Jun']) + float(line['Jul']) + float(line['Aug']) + float(line['Sep']) + float(line['Oct']) + float(line['Nov']) + float(line['Dec']))/12
                sum_anomly_decade += avg_anomly_year
        result = round(sum_anomly_decade/10, 2)
        
        print(f"Average temperature anomaly {current_decade} to {current_decade+year_count}: {result}F")

if __name__ == "__main__":
    main()

#qkn
