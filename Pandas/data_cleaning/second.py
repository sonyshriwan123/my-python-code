import pandas as pd
df = pd.read_csv(r"C:\Users\NIELIT\Downloads\Data.csv")
# print("original read", df.to_string())
#dd/mm/yyyy
df['Date'] = pd.to_datetime(df['Date'], format = 'mixed')
# mm/dd/yyyy
df['Date'] = df['Date'].dt.strftime('%m/%d/%y')
print(df.to_string())
# df.loc[7,'Duration'] = 45

# df.loc[[7,5,3,10,4],'Duration'] = 45
# df.loc[18,'Calories'] = 356.2
print(df.to_string())