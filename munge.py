def main(): 
    f = open('./data/data.txt', 'r',encoding='utf-8')
    d = open('./data/clean_data.csv', 'w',encoding='utf-8')
    lines = f.readlines()
    header = lines[7] # header for comparison purposes
    top_header = header.split()
    top_header = ','.join(top_header[:-1])
    top_header = top_header[:-24]
    top_header += '\n'
    d.write(top_header)
    
    for line in lines[8:-8]: # take out the first 8 lines and the last 8 lines 
        if line.strip():
            if header != line : 
                columns = line.split()
                data = ','.join(columns[:-1])
                data = list(data.split(','))
                data = data[:-6]
                result = []
                for i in range(0, len(data)):
                    if int(data[i]) < 1700:
                        Celsius = (int(data[i])/100)
                        Faren = Celsius * 1.8 
                        result.append('{:.1f}'.format(Faren))
                    else: 
                        result.append(data[i])
                
                result = ','.join(result)
                result += '\n'
                d.write(result)
            
                
    

    
                

    d.close()

        
if __name__ == "__main__":
    main()      
    

"""
def main():
    f = open("./data/readme.txt","r")
    full_text = f.readlines()

    #exclude top and bottom notes
    columns = ['\n']
    full_data = full_text[7:165]
    header = full_data[0].split()[0:13]
    columns = header + columns
    print(columns)

    #remove repeating columns and line break in the middle of dataset
    cleaned_list = []
    for line in full_data:
        if line.startswith("Y") == False and line != "\n":
            cleaned_list.append(line.strip("\n"))

    #convert Celsius to Fahrenheit
    temp_years = []
    for line in cleaned_list:
        temp_years.append(line.split())
        
    for year in temp_years:
        for i in range(1,13):
            if "*" not in year[i]:
                year[i] = '{0:.2f}'.format((float(year[i])/100)*1.8)
            else:
                year[i] = '{0:.2f}'.format(0)
        
        year[13:] = " "
        year[-1] = "\n"

    temp_years = [columns] + temp_years
    print(temp_years)



    #clean_data file
    f_new = open("./data/clean_data.csv","w")
    
    for year in temp_years:
        
        for month in year:
            f_new.write(f"{str(month).rjust(10)}")
            #    count += 1
        
    f_new.close()

if __name__ == "__main__":
    main()






"""