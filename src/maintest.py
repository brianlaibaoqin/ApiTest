from ExecuteTestCase import ExecuteTestCase
import sys
sys.path.append("C:\\Users\\flyyujunmh\\PycharmProjects\\unitest\\commons\\")
#print(sys.path)
from SendEmail import SendEmail

casefile="C:/Users/flyyujunmh/PycharmProjects/unitest/testcase/laohuangli-testcase.xlsx"
reportfile="C:/Users/flyyujunmh/PycharmProjects/unitest/report/laohuangli-testcase_report.xlsx"
sheetname="TestCase"
ExecuteTestCase=ExecuteTestCase()
ExecuteTestCase.execute(casefile,sheetname,reportfile)
SendEmail=SendEmail()
SendEmail.send_mail(reportfile)
