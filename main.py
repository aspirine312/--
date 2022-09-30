if __name__ == "__main__":
    #extract number in athe text file
    f=open("day1.txt","r")
    data = f.read().splitlines()

    #change the data type to int
    #for i in range(10)  #<10,0~9
    data_length = len(data)
    for i in range(data_length):
        data[i] = int(data[i])
    
    #Main process
    #count every increase case
    counter=0
    for i in range(data_length-1):
        if data[i+1]-data[i] >0:
            counter += 1
    
    print(counter)