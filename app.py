import pymysql
from flask import Flask, render_template, request
import timer

sensor_db = pymysql.connect(
    host='182.162.143.216',
    port=3306,
    user='sschina',
    passwd='Andy4240!@',
    db='dbsschina',
    charset='utf8'
)

cursor = sensor_db.cursor()




# Flask 객체 인스턴스 생성
app = Flask(__name__)


# 접속 페이지
@app.route('/')
def index():
    sql = "SELECT t.BIZ_ID, t.CSTID, b.CSTNAME, IFNULL(b.RESIDENT_ID, ''), " \
          "t.HomeTaxPrint, t.SmartABookMake, t.SmartAToConvert, t.WehagoTBookMake, t.HomeTaxUpload " \
          "FROM TB100023 AS t " \
          "LEFT JOIN TB100020 AS b ON t.CSTID=b.CSTID " \
          "LEFT JOIN TB100022 AS a ON t.BIZ_ID=a.BIZ_ID " \
          "WHERE a.CST_TYPE_YEAR='2022' and b.CSTNAME <> '전화문의'" \
          "LIMIT 1000;"

    cursor.execute(sql)

    data_list = cursor.fetchall()
    return render_template('index.html', data_list=data_list)


if __name__ == '__main__':
    app.run()