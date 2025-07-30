import pymysql
conn = pymysql.connect(host="localhost", user="root", password="Founders72!", database="record_boxes")
print("Connected!")
conn.close()