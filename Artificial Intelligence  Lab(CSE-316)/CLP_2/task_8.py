import pandas as pd

data=pd.read_csv('files/dataset.csv')

print('Orginal Dataset with missing values:\n',data)

average_of_column=data.mean()
filled_data=data.fillna(average_of_column)
print("\n\nfilled dataset with columnwise mean value:\n",filled_data)



