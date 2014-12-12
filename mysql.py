# -*- coding: utf-8 -*-
import MySQLdb

# mysq db 접근
db = MySQLdb.connect(host='127.0.0.1', user='root', passwd='20661503', db='test')
cursor = db.cursor(MySQLdb.cursors.DictCursor)
# select 문
cursor.execute('''insert into sample values(2)')
recs = cursor.fetchall()
for rec in recs: 
    print rec 
cursor.close()

cursor.execute('''INSERT into FACTRESTTBL (id, city)
                  values (%s, %s)''',
                  (id, city))