import csv
import math

def read_file(name):
    csv_reader = csv.reader(open(name, encoding='utf-8'))
    return csv_reader

def calculate(row):
    row[1] = int(row[1])
    row[2] = int(row[2])
    row[3] = int(row[3])
    if (row[1]<1) or (row[2]<1) or (row[3]<1): 
        return 'error'
    elif (row[1]>70) or (row[2]>80) or (row[3]>90):
        return 'error'
    else:
        total = 25*row[1]+30*row[2]+45*row[3]
        payment=0
        if total <= 1000: 
            payment = total*0.1
        elif total > 1800: 
            payment = total*0.2
        else:
            payment = total*0.15
        return str(payment)

def computer(name):
    get_name = name
    data = read_file(get_name)
    result=[]
    correct=0
    wrong=0
    for row in data:
        temp = calculate(row)
        if (temp=='error') and (row[6]=='error'):
            correct+=1
        elif float(temp)-float(row[6]) == 0:
            correct+=1
        else:
            wrong+=1
        temp = temp + ','
        result.append(temp)
        
    rate= correct/(correct+wrong) * 1.0
    with open('result_1.csv', 'a', errors='ignore', newline='') as out:
        csv_writer = csv.writer(out, delimiter=' ')
        csv_writer.writerows(result)

    return rate

def classify(row):
    a = float(row[0])
    b = float(row[1])
    c = float(row[2])
    if (a<0) or (b<0) or (c<0): 
        return 'error'
    elif (a+b>c) and (a+c>b) and (b+c>a):
        if a==b or b==c or a==c:
            if a==b and b==c and a==c:
                return '等边三角形'
            else:
                return '等腰三角形'
        else:
            return '普通三角形'
    else:
        return '非三角形'


def triangle(name):
    get_name = name
    data = read_file(get_name)
    result=[]
    correct=0
    wrong=0
    for row in data:
        temp=classify(row)
        if temp==row[3]:
            correct+=1
        else:
            wrong+=1
            temp = temp + ' not match'
        temp = temp + ','
        result.append(temp)
    
    rate= correct/(correct+wrong) * 1.0
    with open('result_2.csv', 'a', errors='ignore', newline='') as out:
        csv_writer = csv.writer(out, delimiter=' ')
        csv_writer.writerows(result)
    return rate


