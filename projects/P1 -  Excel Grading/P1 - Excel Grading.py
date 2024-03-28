# Jack Estes, Katelyn Hamilton, Hannah Larkin, Sebastian Mcfarland, Allen Schultz, Hayden Whalen
# IS303 Section 3
#
# Project 1 - Take poorly formatted input data from excel sheets and create a more organized excel sheet w/
# different workbooks & statistics
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font


def startPage(name, myBook):
    # Headers
    currSheet = myBook[name]
    currSheet.cell(1, 1).value = "Last Name"
    currSheet.column_dimensions["A"].width = len(currSheet.cell(1, 1).value) + 5
    currSheet.cell(1, 1).font = Font(bold=True)
    currSheet.cell(1, 2).value = "First Name"
    currSheet.column_dimensions["B"].width = len(currSheet.cell(1, 2).value) + 5
    currSheet.cell(1, 2).font = Font(bold=True)
    currSheet.cell(1, 3).value = "Student ID"
    currSheet.column_dimensions["C"].width = len(currSheet.cell(1, 3).value) + 5
    currSheet.cell(1, 3).font = Font(bold=True)
    currSheet.cell(1, 4).value = "Grade"
    currSheet.column_dimensions["D"].width = len(currSheet.cell(1, 4).value) + 5
    currSheet.cell(1, 4).font = Font(bold=True)
    currSheet.cell(1, 6).value = "Summary Statistics"
    currSheet.column_dimensions["F"].width = len(currSheet.cell(1, 6).value) + 5
    currSheet.cell(1, 6).font = Font(bold=True)
    currSheet.cell(1, 7).value = "Value"
    currSheet.column_dimensions["G"].width = len(currSheet.cell(1, 7).value) + 5
    currSheet.cell(1, 7).font = Font(bold=True)
    # Non Headers
    currSheet.cell(2, 6).value = "Highest Grade"
    currSheet.cell(3, 6).value = "Lowest Grade"
    currSheet.cell(4, 6).value = "Mean Grade"
    currSheet.cell(5, 6).value = "Median Grade"
    currSheet.cell(6, 6).value = "Number of Students"


def createSheets(poorData, classesList, goodData):
    for row in poorData:
        if row[0].value == "Class Name":
            pass
        elif not classesList.__contains__(row[0].value):
            print(row[0].value)
            classesList.append(row[0].value)
            goodData.create_sheet(row[0].value)
            startPage(row[0].value, goodData)
            setGrades(goodData[row[0].value])
    # TODO figure out where to put this
    # Parse the data for each sheet
    parseData(poorData, classesList, goodData)
    # end TODO


def parseData(poorData, classesList, goodData):
    print("Parse data called")
    # TODO parse data


def setGrades(currSheet):
    currSheet["G2"] = '=MAX(OFFSET($D$2,0,0,COUNT($D:$D)-1,1))'
    currSheet["G3"] = '=MIN(OFFSET($D$2,0,0,COUNT($D:$D)-1,1))'
    currSheet["G4"] = '=IF(G6=0,0,AVERAGE(OFFSET($D$2,0,0,COUNT($D:$D)-1,1)))'
    currSheet["G5"] = '=IF(G6=0,0,MEDIAN(OFFSET($D$2,0,0,COUNT($D:$D)-1,1)))'
    currSheet["G6"] = '=COUNT(OFFSET($D$2,0,0,COUNT($D:$D)-1,1))'


# Create objects for poorly organized spreadsheets w/ our data
poorDataXlsx1 = openpyxl.load_workbook("Poorly_Organized_Data_1.xlsx")
poorDataXlsx2 = openpyxl.load_workbook("Poorly_Organized_Data_2.xlsx")

# Create objects for well organized spreadsheet data
goodDataXlsx1 = Workbook()
goodDataXlsx2 = Workbook()

# Create sheets for each class in poorDataXlsx1 & poorDataXlsx2
createSheets(poorDataXlsx1.active, [], goodDataXlsx1)
createSheets(poorDataXlsx2.active, [], goodDataXlsx2)

# Remove default sheets if they exist
goodDataXlsx1.__delitem__("Sheet")
goodDataXlsx2.__delitem__("Sheet")

# Save the well organized data
goodDataXlsx1.save(filename="Well_Organized_Data_1.xlsx")
goodDataXlsx2.save(filename="Well_Organized_Data_2.xlsx")

# Close all excel files used to avoid resource leak
goodDataXlsx1.close()
goodDataXlsx2.close()
poorDataXlsx1.close()
poorDataXlsx2.close()
