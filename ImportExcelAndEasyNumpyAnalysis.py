import pandas as pd
import openpyxl
import re

# load data file
df = pd.read_excel('/Users/garda.asyuhur/Documents/pokemon_data.xlsx', sheet_name='pokemon_data')
print(df.columns)
df_speed_more50 = df.loc[df['Speed'] >= 50]
df_name_HP = df.loc[df['HP'] > 150, ['Name', 'HP']]
df_describe = df.describe()
print(df_describe)
print(df_speed_more50)
wb = openpyxl.load_workbook('/Users/garda.asyuhur/Documents/pokemon_data.xlsx')
for sheet_name in wb.sheetnames:
    if re.match(r'^describe', sheet_name) or re.match(r'^Name_HP', sheet_name) or re.match(r'^speed >= 50', sheet_name):
        wb.remove(wb[sheet_name])
wb.save('/Users/garda.asyuhur/Documents/pokemon_data.xlsx')
with pd.ExcelWriter('/Users/garda.asyuhur/Documents/pokemon_data.xlsx', mode='a',
                                        engine='openpyxl') as writer:
    df_speed_more50.to_excel(writer, sheet_name='speed >= 50')
    df_name_HP.to_excel(writer, sheet_name='Name_HP')
    df_describe.to_excel(writer, sheet_name='describe')
