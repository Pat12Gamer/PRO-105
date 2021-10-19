import math
import csv
import pandas as pd
import plotly_express as px

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    p = len(data)
    total = 0
    for x in data:
        total += int(x)
    
    mean=total/p
    return mean

squared_list = []
for number in data:
    q = int(number) - mean(data)
    q = q**2
    squared_list.append(q)

sum=0
for x in squared_list:
    sum += x

r = sum/(len(data)-1)

a = math.sqrt(r)
print(a)

df = pd.read_csv("data.csv")
figure = 