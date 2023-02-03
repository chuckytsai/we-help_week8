import mysql.connector
from flask_sqlalchemy import SQLAlchemy




db = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    passwd="pm2021pm",
    db='wonderland',
    charset='utf8')

cursor = db.cursor()

sql = "INSERT INTO userpassword(name, username, password) VALUES (%s, %s, %s)"
val = ("Peter", "PeterParker", "responsibility")
# 創建
cursor.execute(sql, val)
db.commit()

# 查看 表單全部值
cursor.execute("SELECT * FROM userpassword")
myresult=cursor.fetchall()
for x in myresult:
  print(x)
