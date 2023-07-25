import sqlite3

class sqlcommands:
    

    def Open(self):
        if self.bOpen is False:
            self.conn = sqlite3.connect(self.db)
            self.curs = self.conn.cursor()
            self.bOpen = True
        return True

    def __init__(self):
        self.db = './~sqlcommands.sqlt3'
        self.conn = None
        self.curs = None
        self.bOpen = False
        self.fields = [('number', 'Integer',),('name','Text'),('email','Text')]
        self.table_name = 'emp'

    def NewTable(self):
        sqlCommand = """CREATE TABLE if not EXISTS emp (
        number INTEGER PRIMARY KEY,
        name VARCHAR(20),
        email VARCHAR(40));"""
        self.curs.execute(sqlCommand)

    def FillTable(self, fields):
        if self.bOpen:
            self.curs.execute("INSERT INTO emp (number, name, email) VALUES (?,?,?);", fields)
            return True
        return False

    def GetAll(self):
        self.curs.execute("SELECT * FROM emp")
        ans = self.curs.fetchall()
    ##    for i in ans:
    ##        print(i)
        return ans

    def GetSome(self, count):
        self.curs.execute("SELECT * FROM emp ORDER BY number LIMIT 5 OFFSET %s" % count)
        ans = self.curs.fetchall()
        return ans

    def GetPrimary(self):
        self.curs.execute("SELECT number FROM emp")
        ans = self.curs.fetchall()
        return ans

    def CountEntry(self):
        self.curs.execute("SELECT COUNT(number) FROM emp")
        ans = self.curs.fetchone()
        return ans

    def DelTable(self):
        if self.bOpen:
            self.curs.execute("DrOp TaBLe IF EXISTS emp;")
            return True
        return False

    def GetOne(self, number):
        if self.bOpen:
            self.curs.execute("Select * from emp where number = ?;",number)
            zlist = self.curs.fetchall()
            for ref in zlist:
                yield ref #Must itterate throught the yield
        return None
    def DelEm(self, numbers):
        if self.bOpen:
            if len(numbers) != 0:
                self.curs.execute("DELETE from emp where " + " or ".join(("number = " + str(n) for n in numbers)))
                self.conn.commit()
                return True
        return False

    def UpdateOne(self, dat):
        if self.bOpen:
            self.curs.execute("UPDATE emp SET name = ?, email = ? WHERE number = ?",dat)
            self.conn.commit()
            return True
        return False

    def DelOne(self, number):
        if self.bOpen:
            self.curs.execute("DELETE from emp where number = ?;",number)
            return True
        return False

    def End(self):
        if self.bOpen:
            self.conn.commit()
            self.bOpen = False
        return True

        @staticmethod
        def Import(dao, encoding=None, text_file='Employee.csv', hasHeader=True, sep='|'):
            try:
                # dao.open()
                with open(text_file, encoding=encoding) as fh:
                    line = fh.readline().strip()
                    if hasHeader is True:
                        line = fh.readline().strip()
                    while len(line) is not 0:
                        if dao.insert(line.split(sep)) is False:
                            return False
                        line = fh.readline().strip()
                # dao.close()
                return True
            except:
                pass
            return False


    
