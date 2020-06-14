import pygsheets
import fetchMD as fmd
gc = pygsheets.authorize(client_secret='../client_secret.json') # This will create a link to authorize 

#  Open spreadsheet  

# # 1. Open spreadsheet by name 
sh = gc.open('DrugData') # open spreadsheet

# # 2. Open spreadsheet by key
# sh = gc.open_by_key('spreadsheet_key')

# 3. Open spredhseet by link
# sh = gc.open_by_link('https://docs.google.com/spreadsheets/d/1w_67qHjxVyYtegiQLapKlk7NIlbUMvsL6Ucak-EL_Eg/edit#gid=721977854')

# Open worksheet

# wk1 = sh[0] #Open first worksheet of spreadsheet
# Or 
wk1 = sh.worksheet_by_title("main") # sheet1 is name of first worksheet
# print(sh.worksheets)
for row in range(50,51):
    if wk1.cell('G'+str(row)).value == '':
        data = fmd.fetchMD(wk1.cell('A'+str(row)).value)
        wk1.cell('G'+str(row)).set_value(data[0])
        wk1.cell('H'+str(row)).set_value(data[1])
        wk1.cell('I'+str(row)).set_value(data[2])
        wk1.cell('J'+str(row)).set_value(data[3])
        print(row)


# end for
# wk1.clear(start="A2", end="A1000")
# wk1.update_col(1, [2,3,4], row_offset=1)

""" First worksheet has index 0, second has index 1, so on. 
Instead of index, you can use worksheet name. 
"""