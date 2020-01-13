import math
def tops(datas,impact,c):
    rows= len(datas)
    square = []
    positive =[]
    negative = []
    for i in range(0, len(c)):
        sum=0
        for j in range(0,rows):
            sum = sum + (datas[j,i]*datas[j,i])
        temp= math.sqrt(sum)    
        square.append(temp)
   
    for i in range(0, len(c)):
        for j in range(0,rows):
            datas[j,i]= datas[j,i]/square[i]
            datas[j,i]= datas[j,i]*c[i]
        
    for i in range(0, len(c)):
        min = 100000000
        max = -100000000
        for j in range(0,rows):
            if min > datas[j,i]:
                min= datas[j,i]
            if max < datas[j,i]:
                max = datas[j,i]
        if impact[i] == '+':
            positive.append(max)
            negative.append(min)
        if impact[i] == '-':
            positive.append(min)
            negative.append(max)

    spositive = []
    snegative = []
    performance = []

    for i in range(0,rows):    
        sum=0
        sum1 = 0
        for j in range(0, len(c)):
            sum = sum + (datas[i,j]-positive[j])*(datas[i,j]-positive[j])
            sum1 = sum1 + (datas[i,j]-negative[j])*(datas[i,j]-negative[j])
        sum = math.sqrt(sum)
        sum1 = math.sqrt(sum1)
        spositive.append(sum)
        snegative.append(sum1)
        
    for i in range(0,len(spositive)):
        performance.append(snegative[i]/(spositive[i]+snegative[i]))
        #print(performance)
    return performance