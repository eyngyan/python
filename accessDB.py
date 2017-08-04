import pypyodbc
import pyodbc

idnum=str(input('Please enter your id number: '))
#name=str(input('Please enter your name: '))
#colid=str(input('Please enter column id: '))
#def query(name):
#    cursor.execute('SELECT @name from Table1')
#    return cursor

#conn=pypyodbc.win_connect_mdb('Driver={Microsoft Access Driver (*.mdb)};DBQ=C:\\Users\\eyngyan\\Documents\\test.mdb')
conn=pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
    r"DBQ=C:\\Users\\eyngyan\\Documents\\test.mdb;")
#conn=pyodbc.connect('Driver={Microsoft Access Driver (*.mdb)};DBQ=' + DBfile + ';Uid=;Pwd=;')

cursor=conn.cursor()



#SQL=['SELECT ', colid, ' FROM Table1;']
SQL=['SELECT * FROM Table1 WHERE id =', idnum]
#SQL1='SELECT * FROM Table1 WHERE id = 1'
#for row in cursor.excute(SQL):
SQLcommand=(' ').join(SQL)
print(SQLcommand)
for row in cursor.execute(SQLcommand):
    print(row)
#print(query)
#result=cursor.execute(SQLcommand)
#for i in result:
#    print('result is: ', result)




cursor.close()
conn.close()

