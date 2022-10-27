import sqlite3

class MSGBOX:
    def __init__(self):
        self.__create_error = '테이블 생성 실패.'
        self.__create_complete = '테이블 생성 성공.'
        self.__drop_error = '테이블 드롭 실패.'
        self.__drop_complete = '테이블 드롭 성공.'
        self.__insert_error = '데이터 삽입 실패.'
        self.__insert_complete = '데이터 삽입 성공.'
        self.__select_error = '데이터 조회 실패.'
        self.__select_complete = '데이터 조회 성공.'
    @property
    def create_error(self):
        print(self.__create_error)
        return

    @property
    def create_complete(self):
        print(self.__create_complete)
        return

    @property
    def drop_error(self):
        print(self.__drop_error)
        return 

    @property
    def drop_complete(self):
        print(self.__drop_complete)
        return

    @property
    def insert_error(self):
        print(self.__insert_error)
        return 

    @property
    def insert_complete(self):
        print(self.__insert_complete)
        return 

    @property
    def select_error(self):
        print(self.__select_error)
        return 

    @property
    def select_complete(self):
        print(self.__select_complete)
        return 



class EMART_DB:
    def __init__(self, db_name = 'SeoulAirIndex.db'):
        self.conn = sqlite3.connect('SeoulAirIndex.db')
        self.msg = MSGBOX()
        self.cur  = self.conn.cursor()

    def create(self, table_name = None):
        try:
            self.conn.execute('CREATE TABLE IF NOT EXISTS %s (DATE int, DIVISION TEXT, LOCATION TEXT, OXI REAL, NO REAL, CO REAL, SO REAL, PRIMARY KEY(DATE, DIVISION, LOCATION))'%table_name)
            self.conn.commit()
            self.msg.create_complete
        except:
            self.msg.create_error
        return

    def drop(self, table_name = None):
        try:
            self.conn.execute('DROP TABLE %s'%table_name)
            self.conn.commit()
            self.msg.drop_complete
        except:
            self.msg.drop_error
        return

    def insert(self, df, table_name = None):
        try:
            for row in df.itertuples():
                row = row[1:]
                print(row)
                sql = 'INSERT INTO %s VALUES(%d, \'%s\', \'%s\', %f, %f, %f, %f);'%(table_name, *row)
                self.cur.execute(sql)
                self.conn.commit()
                self.msg.insert_complete
        except:
            self.msg.insert_error
        return

    def select(self, query):
        try:
            self.cur.execute(query)
            rows = self.cur.fetchall()
            self.msg.select_complete
        except:
            self.msg.select_error
        return rows