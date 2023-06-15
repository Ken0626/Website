import pyexcel as px

s = px.get_sheet(file_name='測試用活頁簿.xlsx', 
             start_column = 1, column_limit = 3)

print(s[0, 0])