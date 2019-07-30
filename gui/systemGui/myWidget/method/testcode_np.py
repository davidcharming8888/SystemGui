import pandas as pd

a = pd.read_csv(r'D:\chaos\jobless\keras\Forcast_Fault\data\4year\seldata1_nset_4year.csv',index_col=0)

print(a.iloc[80000:80010,:])