###
using csv file creating ,adding,save,reading,adding and deleting and after deleting csv file?
###
data = {
    'name':['bob','alice'],
    'age':[24,27]
}
df = pd.DataFrame(data)
print(df)
df.to_csv('employees.csv')
df_csv = pd.read_csv('employees.csv')
print(df_csv)
new_data = pd.DataFrame([{'name':'david','age':25,'city':'san fransisco'}])
df_csv = pd.read_csv('employees.csv')
df_csv = pd.concat([df_csv,new_data],ignore_index= True)
df_csv.to_csv('employees.csv',index= False)
df_csv = pd.read_csv('employees.csv')
df_csv = df_csv[df_csv['name']!='bob']
df_csv.to_csv('employees.csv',index = False)
###
Unnamed: 0,name,age,city
1.0,alice,27,
,david,25,san fransisco
