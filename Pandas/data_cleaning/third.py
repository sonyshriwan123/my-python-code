import pandas as pd
# Import the file and read the deta
# it consists of some duplicate values
df = pd.read_csv(r"C:\Users\NIELIT\Downloads\data (2).csv")
# print("original read", df.to_string())
# print("Showing the duplicate values:", df.duplicated())
#original file work to
# removing values==
df.drop_duplicates(inplace = True)
print("After removing the duplicate values:",df.to_string())








