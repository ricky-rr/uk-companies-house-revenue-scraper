from bs4 import BeautifulSoup
import requests, openpyxl


read_file = "/Users/**filepath"
readWb = openpyxl.load_workbook(read_file)
readSheet = readWb.active

m_row = readSheet.max_row

writeExcel = openpyxl.Workbook()
writeSheet = writeExcel.active
writeSheet.title = "Generated Data"
writeSheet.append(['Company Number', 'Total Assets', 'Total Liabilites', 'NetAssets', 'CashInBank', 'Employees', 'Turnover', 'Debt Ratio', 'No of Directors'])

  
for i in range(1, x):
    cell_obj = readSheet.cell(row = i, column=1)
    try:
        companyNo = cell_obj.value
        source = requests.get(f"https://suite.endole.co.uk/insight/company/{companyNo}")
        source.raise_for_status()
        soup = BeautifulSoup(source.text, 'html.parser')
        financials = soup.find('div', id="tiles_Financials").contents[4]
        totalAssets = ((financials.contents[1]).find(class_="t1").get_text())
        totalLiabilites = ((financials.contents[2]).find(class_="t1").get_text())
        netAssets = ((financials.contents[3]).find(class_="t1").get_text())
        cashInBank = ((financials.contents[4]).find(class_="t1").get_text())
        employees = ((financials.contents[5]).find(class_="t1").get_text())
        turnover = ((financials.contents[6]).find(class_="t1").get_text())
        debtRatio = ((financials.contents[7]).find(class_="t1").get_text())
        noOfDirectors = soup.find('div', id="tiles_People").contents[2].find(class_="count").get_text()
        writeSheet.append([cell_obj.value, totalAssets, totalLiabilites, netAssets, cashInBank, employees, turnover, debtRatio, noOfDirectors])
    except Exception as e:
      print(e)
    
writeExcel.save('GeneratedData.xlsx')
