
import pymysql

# a = "猪猪"

def query(sql):
    #固定的方法
    db = pymysql.connect(host='118.24.255.132',user='testgoup',password="1qaz!QAZ",db='ljtestdb')
    #获取查询窗口：游标
    cur = db.cursor()
    #执行sql语句
    cur.execute(sql)
    #获取所有结果
    res = cur.fetchall()
    db.close()
    return res


if __name__ == "__main__":
    sql = "select * from t_user where id = 260"
    a = query(sql)
    print(a)
