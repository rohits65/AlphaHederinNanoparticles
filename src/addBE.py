import pygsheets
from joblib import load
import numpy as np
from keras.models import Sequential, load_model
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
wk1 = sh.worksheet_by_title("temp") # sheet1 is name of first worksheet
# print(sh.worksheets)
model = load_model("savedStates/entrapmentEfficiency_model.savedstate")
sc = load("savedStates/entrapmentEfficiency_scaler.savedstate")

for row in range(38,40):
        try:

                print('red')
                tpsa = wk1.cell('I'+str(row)).value
                cx = wk1.cell('J' + str(row)).value
                mps = wk1.cell('F' + str(row)).value
                mw = wk1.cell('G' + str(row)).value
                lg = wk1.cell('L'+str(row)).value
                xlog = wk1.cell('H'+str(row)).value
                EE = wk1.cell('N'+str(row)).value
                hrs = wk1.cell('O'+str(row)).value
                pdr = wk1.cell('D'+str(row)).value


                data = model.predict(np.array(sc.transform([np.array([mw, cx, lg, tpsa, pdr, xlog])])).reshape(-1, 6))[0][0]
                print('blue')

                wk1.cell('Q'+str(row)).set_value(str(data))
                print('green')


                print(row)
        except:
                continue


# end for
# wk1.clear(start="A2", end="A1000")
# wk1.update_col(1, [2,3,4], row_offset=1)

""" First worksheet has index 0, second has index 1, so on. 
Instead of index, you can use worksheet name. 
"""