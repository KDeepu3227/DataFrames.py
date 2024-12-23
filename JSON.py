###
write a python program to create,save,reading,adding,deleting data?
###
data = {
    'name':['bob','alice'],
    'age':[24,27]
}
df = pd.DataFrame(data)
print(df)
df.to_json('employees.json',orient='records')
df_json = pd.read_json('employees.json')
print(df_json)
new_data_json = pd.DataFrame([{'name':'david','age':25,'city':'san fansisco'}])
df_json = pd.read_json('employees.json')
df_json = pd.concat([df_json,new_data_json],ignore_index=True)
df_json.to_json('employees.json',orient='records')
df_json = pd.read_json('employees.json')
df_json = df_json[df_json['name']!='bob']
df_json.to_json('employees.json',orient='records')
###
[{"name":"alice","age":27,"city":null},{"name":"david","age":25,"city":"san fansisco"}]

