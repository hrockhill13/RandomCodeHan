# Han Rockhill
# python 3.12.1
# Use to determine what the fruit is going to contribute to OG when making mead
# allowing adjustment to Honey and other fermentable sugars.
from openpyxl import Workbook
wb = Workbook('.venv/lib/python3.12/site-packages/pandas/io/excel/fruitTable.xlsx')

# Read the Excel file into a DataFrame
df = pd.read_excel(wb)
# df = pd.read_excel(excel_file_path)
# Now, 'df' contains your Excel table as a DataFrame
print(df)


fruit = str.upper(input(" Fruit Name: "))
print(" the fruit is %s " % fruit)
if fruit == 'STRAWBERRY':
    fruit = 1.028
    acid = "citric"
    print("the starting gravity for that is %s" % fruit)
    print("Acid Type = %s " % acid)
else:
    print("no idea what the starting gravity is")
