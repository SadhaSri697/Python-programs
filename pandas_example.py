#pandas is one of the most popular Python libraries used for working with data. 
# It helps you read, organize, analyze, clean, and manipulate data
#HOW TO USE:
#import pandas as pd
#import pandas → Imports the pandas library into your program.
#as pd → Gives it the shorter name pd, which is the standard convention.
#pandas.read_csv("data.csv") or pd.read_csv("data.csv")
#print(df.head())
#print(df.info())
#print(df.describe())
import pandas as pd
data = {
    "Name": ["Ram", "Sita", "Ravi"],
    "Age": [18, 19, 20],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)
print(df)