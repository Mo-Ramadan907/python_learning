import pandas as pd

#----first exercise ----
data = {
    "Name":["mohamed","yousef","el zoz","merna","mariam","yassmin"],
    "Age":[30,27,11,22,23,21],
    "salary":[1000,2930,4000,5000,8900,1002]
}
df = pd.DataFrame(data)
print(df.iloc[:3,:])

print(df["Age"])
print(df[df["Age"] > 25])

#----second exercise -----

df = pd.read_csv("/home/mo/Projects/study_program/Learning_pandas/students.csv")
print(df.info())
print(df.describe())

#----column operations

df["grade2"] = df["grade"] * 2
print(df['grade2']) 

df = df.drop(columns=["grade2"],axis=["columns"])
print(df)
df.rename(columns={"grade":"secore"},inplace=True)
print(df)

#----- filtering 


data = {
    "age":[23,27,22,80,66,55,44]
    , "city":["cairo","mansoura","sharm el sheikh","cairo","london","paris","tokoyo"]
    , "salary":[1000,8900,2702,100,500,222,7000]
}

df = pd.DataFrame(data)
print(df)
print(df[df["city"] == "cairo"])

print(df[df["salary"] > 1000])

print(df[(df["city"] == "cairo") & (df["age"] > 20) & (df["age"]< 30 )])

# --- missing values ----


data = {
    "age":[23,27,22,None,80,66,55,44,50,None,70]
    , "city":["","cairo","washington","mansoura","sharm el sheikh","cairo","london","paris","","tokoyo","london"]
    , "salary":[1000,8900,2702,100,500,None,222,7000,None,None,None]
}

df = pd.DataFrame(data)
print(df.isna().sum())
df["salary"] = df["salary"].fillna(df['salary'].mean())
df = df.dropna(subset=["age"])
print(df)



#------
print(df.sort_values(by="age"))
print(df.sort_values(by="salary",ascending=False))
print(df.sort_values(by=["city","salary"]))


#----groupby 

data = {
    "department":["it","is","hr","cv","it","cv","hr","it"],
    "salary":[10000,5000,7000,8000,2330,1890,2220,5000],
    "age":[22,21,56,54,47,48,33,50]
}
df = pd.DataFrame(data)
group = df.groupby("department")
print(group["salary"].mean())
print(group["age"].max())
print(list(group))



