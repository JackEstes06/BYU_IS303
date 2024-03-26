from openpyxl import Workbook

myWorkbook = Workbook()
currSheet = myWorkbook.active
currSheet.title = "Practice"

j = 10
for i in range(1, 11):
    currSheet[f"A{i}"] = j
    j = j - 1

myWorkbook.save(filename="vba1.xlsx")

currSheet["A1"] = 15
currSheet["A2"] = "=A1 * 2"
myWorkbook.save(filename="vba2.xlsx")

myWorkbook.close()
