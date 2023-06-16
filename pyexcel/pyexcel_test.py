import pyexcel as px

s = px.get_sheet(file_name='./測試用活頁簿.xlsx', 
             start_column = 0, column_limit = 3)

for i in s:
    print(i)
# print(s[0, 0], s.row)