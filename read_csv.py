import os
import pandas as pd


fileArr = os.listdir('./csv')

print(fileArr)


for i in fileArr:

    filepath = f'./csv/{i}' #'./coup_list.csv'#"./lemonade.csv"
    data = pd.read_csv(filepath)

    filter_data = pd.notnull(data["상품명"])

    print(data[filter_data])
    print(len(data), len(data[filter_data]))
 
