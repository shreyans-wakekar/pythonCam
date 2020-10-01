import pandas as pd
import csv
with open('3233234.csv',"r") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)
    row_count = len(data)
N=11
df = pd.read_csv('3233234.csv', skiprows = row_count - N).values.tolist()
print(f'{df}')