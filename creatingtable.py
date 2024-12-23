###
create a data frame table using dept_name,hod_name,total_strength,and adding phone_no,and chnage that phone_no?
###
data = {
    'dept name':['cse','cse ds','ai&ds','ece','eee'],
    'hod name':['prabhu kumar','reddy prasad','lokesh kumar','ram murthy','surya prabha'],
    'total_strength':[94,64,57,40,30]
}
df = pd.DataFrame(data)
print(df)
df['phone_no'] = [75432345,98765421,65432,99876543,2345678]
print(df)
df.loc[1,'phone_no'] = 8645678765
print(df)
###
  dept name      hod name  total_strength
0       cse  prabhu kumar              94
1    cse ds  reddy prasad              64
2     ai&ds  lokesh kumar              57
3       ece    ram murthy              40
4       eee  surya prabha              30
  dept name      hod name  total_strength  phone_no
0       cse  prabhu kumar              94  75432345
1    cse ds  reddy prasad              64  98765421
2     ai&ds  lokesh kumar              57     65432
3       ece    ram murthy              40  99876543
4       eee  surya prabha              30   2345678
  dept name      hod name  total_strength    phone_no
0       cse  prabhu kumar              94    75432345
1    cse ds  reddy prasad              64  8645678765
2     ai&ds  lokesh kumar              57       65432
3       ece    ram murthy              40    99876543
4       eee  surya prabha              30     2345678

