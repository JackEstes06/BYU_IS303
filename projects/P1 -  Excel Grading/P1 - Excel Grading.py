# Jack Estes, Katelyn Hamilton, Hannah Larkin, Sebastian Mcfarland, Allen Schultz, Hayden Whalen
# IS303 Section 3
#
# Project 1 - Take poorly formatted input data from excel sheets and create a more organized excel sheet w/
# different workbooks & statistics
import openpyxl
from openpyxl import Workbook

# Create objects for poorly organized spreadsheets w/ our data
poorDataXlsx1 = openpyxl.load_workbook("Poorly_Organized_Data_1.xlsx")
poorDataXlsx2 = openpyxl.load_workbook("Poorly_Organized_Data_2.xlsx")

# TODO remove content below
myWorkbook = Workbook()
currSheet = myWorkbook.active

myWorkbook.save(filename="Well_Organized_Data_1.xlsx")
myWorkbook.close()
# end TODO
