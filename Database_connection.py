# SQL database connection

""""
For reference, the steps in this guide (windows) are (assuming you already have python installed):

Install the Microsoft ODBC Driver for SQL Server on Windows,
from https://docs.microsoft.com/en-us/sql/connect/odbc/windows/system-requirements-installation
-and-driver-files?view=sql-server-2017#installing-microsoft-odbc-driver-for-sql-server
Open cmd.exe as an administrator
Navigate to your python scripts folder containing pip
Type: pip install pyodbc
"""

import pyodbc
# sql: # SELECT @@SERVERNAME
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-OMOKT5U\SQLEXPRESS;'
                      'Database=Test2;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM Test2.dbo.tbStudent')

for row in cursor:
    print(row)