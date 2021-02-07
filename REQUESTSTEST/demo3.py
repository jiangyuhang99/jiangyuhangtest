import pandas as pd
from pandas import DataFrame

#读
data = pd.read_excel('data.xlsx')

#查看所有的值
print(data.values)
