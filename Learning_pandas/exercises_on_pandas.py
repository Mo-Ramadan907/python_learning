import pandas as pd 

#check the pandas version 
# print(pd.__version__)


#--------------one diamesion column (series )
# # data = ["mohamed","ahmed","romio"]
# data = [104,105,1000,2200]
# boolean_data = [True,False,True]
# # series = pd.Series(data,index=['apartment #1','apartment #2','apartment #3'])
# # print(series.loc["apartment #1"])
# series = pd.Series(data)

# # series.iloc[3] = -50
# print(series[series < 150])



# calories = {"day 1" : 1750,"day 2":2100,"day 3":1700}
# series = pd.Series(calories)
# series.loc["day 3"] +=500
# print(series.loc["day 3"])
# print(series[series >1700])


# my_players_list = ['messi',"bruno fernandas","harry kane","son heung min","rashford","sesko","mbeumo","counia"]
# series = pd.Series(my_players_list)


#------------data frame tabular representation --------------------------

# data = {
#     "Name":["mohamed","merna","gemmy","salma"],
#     "Age":[23,21,22,None]
# }

# df = pd.DataFrame(data,index=["student"+str(i+1) for i in range(len(data["Name"]))])
# print(df)

# print(df.loc["student1"])


# data = {
#     "ID":[201,202,203],
#     "Name":['ahmed',"salah","abdelfattah"],
#     "salary":[1000.5,2333,70000]
# }
# i = 3 
# df = pd.DataFrame(data,index=[f"employee {num+1}" for num in range(i)])
# row_frame = pd.DataFrame([{"ID":204,"Name":"ibrahim","salary":8000},
#                           {"ID":205,"Name":"merna","salary":3210}],index=["employee 4","employee 5"])

# df = pd.concat([df,row_frame])
# print(df)


#-----read csv files ----------------

# here i can define index_col to change the label of the data frame to one of the values of the specific column (column_index = "your column")
df = pd.read_csv("/home/mo/Projects/study_program/Learning_pandas/archive/10_Property_stolen_and_recovered.csv")
# print(df[["Area_Name","Year"]])
# print(df.iloc[0:10:2,0:4])
# print(df.iloc[0])
# result_cols = df["Area_Name"]
# print(result_cols.head())
# result_rows = df[(df['Year'] > 1990) & (df['Cases_Property_Stolen'] > 50)]
# print(result_rows.shape)


#-------the whole data frames aggregation function ----

# print("the average of each numeric column")
# print(df.mean(numeric_only=True))
# print("the sum of each numeric column")
# print(df.sum(numeric_only=True))
# print("the maximum value is : ")
# print(df.max(numeric_only=True))
# print("the minimum value is : ")
# print(df.min(numeric_only=True))
# print("the count of values exist  in each columns")
# print(df.count())

#-------individual column aggregation func

# print(df["Year"].sum())

#-----groupby in data frames ----

# group = df.groupby("Year")
# print(group["Cases_Property_Stolen"].median())
# print(group["Cases_Property_Stolen"].max())
# print(group["Cases_Property_Stolen"].min())
# print(group["Cases_Property_Stolen"].sum())
# print(group["Cases_Property_Stolen"].mean())
# print(group["Cases_Property_Stolen"].count())

# print(df.shape)
# print(df.isna())
# df.isna().sum()
# df.fillna(0)
# df.dropna()


# print(df["Year"].isna().sum())
# print(df.isna().sum())


# df = df.drop_duplicates()
# df = df.drop_duplicates([])
# df = df.dropna(subset=["Sub_Group_Name","Year","Cases_Property_Stolen"])\
# df = df.fillna({"Year":df["Year"].mean()})
# df = df.drop(columns=["Year","Cases_Property_Stolen"])
# df["Year"] = df["Year"].replace({2010:2050})
# print(df["Year"])



# print(df.columns)
# print(df.info())
# print(df.describe())
# print(df.shape)

# change the data type of specific column
# df["age"] = df["age"].astype(int)


#---adding column in the data frame 
# df["salary"] = df["age"] * 1000

#---------------------rename colums--------
# df.rename(columns={"age": "Age"}, inplace=True)


#apply specific function on column 
# df["age2"] = df["age"].apply(lambda x: x * 2)
df = pd.read_csv("/home/mo/Projects/study_program/dataset/raw_material1.csv")
print(df.shape)