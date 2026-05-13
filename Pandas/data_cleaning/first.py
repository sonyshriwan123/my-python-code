# ==Data cleaning using pandas

# Data cleaning is the process is clearing the data 

# ==what can be the bed data?
# 1 missing data
# 2 duplicate data
# 3 empty cell
# 4 empty rows
# 5 empty columns
# 6 wrong data type
# 7 inconsistent data
import pandas as pd



# df = pd.read_csv(r"C:\Users\NIELIT\Downloads\data.csv")
# # print("orginal:",df.to_string())
# new_df = df.dropna()
# # print(new_df.to_string())

# ==removing the rows 
# df.dropna(inplace = True)
# print(df.to_string())

# ==adding the values in the empty cells
# df = pd.read_csv(r"C:\Users\NIELIT\Downloads\data.csv")
# df.fillna(258.5,inplace = True)
# print("After filling empty cells:", df.to_string())


# filling the messing values with differnt value
# df = pd.read_csv(r"C:\Users\NIELIT\Downloads\data.csv")
# df.fillna({"Calories":540.5},inplace = True)
# print("After filling empty cells with differnt values:", df.to_string())

# df.loc[3,"Calories"] = 123.5
# print("After filling empty cells with differnt values:", df.to_string())


df = pd.read_csv(r"C:\Users\NIELIT\Downloads\data.csv")
# x = df["Calories"].mean()
# x = df["Calories"].median()
x = df["Calories"].mode()[0]
# print("The mean value is:",x)
# print("The median value is:",x)
print("The mode value is:",x)

df.fillna({"Calories": x}, inplace = True)
print(df.to_string())