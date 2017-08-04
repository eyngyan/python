import pypyodbc
import pyodbc

#idnum=str(input('Please enter your id number: '))
times = 5
while times>0:
    times=times-1
    idnum=str(input('Please enter your id number: '))
    conn=pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        r"DBQ=C:\\Users\\eyngyan\\Documents\\test.mdb;")
    cursor=conn.cursor()
    SQL=['SELECT * FROM Table1 WHERE id =', idnum]
    SQLcommand=(' ').join(SQL)
    print(SQLcommand)
    for row in cursor.execute(SQLcommand):
        print(row)
    cursor.close()
    conn.close()
print('you do not have enough times')