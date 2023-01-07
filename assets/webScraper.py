import pandas as pd
import openpyxl 

url = '/Users/macbook/Desktop/Django/DjangoUnchained/judexRoot/assets/webscraper.html'
dfs = pd.read_html(url)
# Using pandas to read the html table from the url path
df = dfs[0]
print(df.Name[0][:1])
# df = pd.concat([df[0], df[1], df[2], df[3], df[4], df[5], df[6], df[7], df[8], df[9], df[10], df[11], df[12], df[13], df[14], df[15]])
# Concatenating all the individual dataframes into a single dataframe 
# print(df)
# df[['Last_Name', 'First_Name']] = df.Name.str.split(', ', expand=True)
# df[['First_Name', 'Middle_Name', 'Title']] = df.First_Name.apply(lambda x: pd.Series(str(x).split(' ')))
# Seperating the Name columns to First, Last and Middle names

# with pd.ExcelWriter('data_tables.xlsx') as writer:
    # df.to_excel(writer, sheet_name='Convictions', index=False)
#  Creating an excel sheet with the information from the dataframes

# with pd.ExcelWriter('data_tables.xlsx', mode='a', if_sheet_exists='overlay', engine='openpyxl') as writer:
#     df.to_excel(writer, sheet_name='Convictions', index=False, startrow=172)

# Split single column into two columns use apply()
# df[['First Name', 'Last Name']] = df["Student_details"].apply(lambda x: pd.Series(str(x).split(",")))
# print(df)

# df[0][['Last_Name', 'First_Name']] = df[0].Name.str.split(', ', expand=True)
# df[0][['First_Name', 'Middle_Name']] = df[0].First_Name.str.split(' ', expand=True)
