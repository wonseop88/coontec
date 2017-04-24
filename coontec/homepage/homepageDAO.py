'''
Created on 2017. 3. 24.

@author: wonseop
'''
# getInfoList
import pymysql
from homepage.config import DATABASE



class homeList:

    def dbopen(self):
        try:
            self.conn = pymysql.connect(**DATABASE)
            self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        except:
            print('error | msg = "db cur open failed"')
    def dbclose(self):
        try:
            self.curs.close()
            self.conn.close()

        except:
            print('error | msg = "db cur close failed"')
            
    def getAllList(self):
        s_query = ' SELECT SEQ, CATEGORY, PAGE_URL, FILENAME, NAME, ENABLED '
        s_query += 'from HOMEPAGE.PAGEINFO'
        try:
            self.dbopen()
            self.curs.execute(s_query)
            dbdata = self.curs.fetchall()
        except:
            print("error select failed")
        finally:
            self.dbclose()
            
        return dbdata
    
    def getList(self,pageurl):

        s_query = 'SELECT SEQ, CATEGORY, PAGE_URL, FILENAME, NAME, ENABLED '
        s_query += 'from HOMEPAGE.PAGEINFO where page_url="'+pageurl+'"'
        try:
            self.dbopen()
            self.curs.execute(s_query)
            dbdata = self.curs.fetchall()
        except:
            print("error select failed")
            
        finally:
            self.dbclose()
        return dbdata
    
    def getGroupList(self,category):
        s_query = 'SELECT SEQ, CATEGORY, PAGE_URL, FILENAME, NAME, ENABLED '
        s_query += 'from HOMEPAGE.PAGEINFO where CATEGORY="'+category+'"'
      
        try:
            self.dbopen()
            self.curs.execute(s_query)
            dbdata = self.curs.fetchall()
        except:
            print("error select failed")
            
        finally:
            self.dbclose()
        
        return dbdata
     
