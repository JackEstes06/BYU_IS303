# Jack Estes
# 4/11/24
# IS303 Section 3
# Extra Credit - recreate an excel spreadsheet like the GradeCalc.xlsx in the folder
import os

import openpyxl
from openpyxl import styles


# Set column widths for sheet
def sizeColumns(sheet):
    sheet.column_dimensions["A"].width = 21.83
    sheet.column_dimensions["A"].font = openpyxl.styles.Font(bold=True)
    sheet.column_dimensions["B"].width = 8
    sheet.column_dimensions["C"].width = 8
    sheet.column_dimensions["D"].width = 7.83


# Set the colors for a given range
def setColors(sheet, startRow, endRow, startCol, endCol):
    for row in range(startRow, endRow + 1):
        for col in range(startCol, endCol + 1):
            sheet.cell(row, col).fill = openpyxl.styles.fills.PatternFill(start_color="d9d9d9", fill_type="solid")


# Given a specific row, startCol, and endCol put a border around these cells
def setBorders(sheet, startRow, endRow, startCol, endCol):
    cellBorderStyle = openpyxl.styles.borders.Side(border_style="thin")

    for row in range(startRow, endRow + 1):
        topBorder = False
        bottomBorder = False
        if row == startRow:
            topBorder = True
        if row == endRow:
            bottomBorder = True
        for col in range(startCol, endCol + 1):
            leftBorder = False
            rightBorder = False
            if col == startCol:
                leftBorder = True
            if col == endCol:
                rightBorder = True
            sheet.cell(row, col).border = openpyxl.styles.borders.Border(
                left=cellBorderStyle if leftBorder else None,
                right=cellBorderStyle if rightBorder else None,
                top=cellBorderStyle if topBorder else None,
                bottom=cellBorderStyle if bottomBorder else None,
            )
    # sheet.merge_cells("A1:D1")
    # sheet.unmerge_cells("A1:D1")


gradeCalc = openpyxl.Workbook()
# There is only 1 sheet so we just get the first worksheet as the currSheet
currSheet = gradeCalc[gradeCalc.sheetnames[0]]

# Set the styling for the sheet
sizeColumns(currSheet)
setBorders(currSheet, 1, 1, 1, 4)
setBorders(currSheet, 3, 5, 1, 4)
setBorders(currSheet, 7, 8, 1, 4)
setBorders(currSheet, 10, 11, 1, 4)
setBorders(currSheet, 13, 13, 2, 4)
setBorders(currSheet, 15, 15, 1, 4)
setBorders(currSheet, 17, 17, 1, 4)
currSheet.merge_cells("B13:C13")
currSheet.merge_cells("A17:C17")
setColors(currSheet, 17, 17, 1, 1)
setColors(currSheet, 13, 13, 2, 2)
setColors(currSheet, 7, 7, 3, 4)

# Save the new workbook
outputFile = "GradeCalcMimic.xlsx"
gradeCalc.save(filename=outputFile)

# Close all excel files to avoid resource leaks
gradeCalc.close()
os.system(f"open -a '/Applications/Microsoft/Microsoft Excel.app' {outputFile}")
