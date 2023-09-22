import csv 

def main(): 
    f = open('./data/clean_data.csv', 'r',encoding='utf-8')
    
    csv_reader = csv.DictReader(f, delimiter=',')

    decade_temp = []
    year = 1880 
    for line in csv_reader:
        
        if line["Year"] < "1890": 
            temp_year = (float(line["Jan"]) + float(line["Feb"]) + float(line["Mar"]) + float(line["Apr"]) + float(line["May"]) + float(line["Jun"]) + float(line["Jul"]) + float(line["Aug"]) + float(line["Sep"]) + float(line["Oct"]) + float(line["Nov"]) + float(line["Dec"])) / 12
            year += 10
            
    print(temp_year)
        

    #         decade_temp = decade_temp.append(temp_year)
   
    # print(decade_temp)
        
if __name__ == "__main__":
    main()      


"""

"""