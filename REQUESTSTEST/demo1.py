#导入requests : 固定的导入方法
import requests
from dbtools import query
#python调接口

# 1.构造请求
u = 'http://118.24.255.132:2333/get_title_img'
r = requests.get(u)
print(r.text)

# 2.判断结果：断言实现判断http状态码，和结果码
# assert 判断条件
#结果码：本次请求的结果是否正确； 状态码：接口的状态码
assert r.status_code == 200  #判断接口是不是正常的
# r.json() 把结果转换成字典
assert r.json()['status'] == 200 #判断结果码是否正确

#3. 数据库校验，本次要查询所有的轮播图id是否存在
data = r.json()['data']
for i in data:
    # 每次循环之后，都去查一下数据库
    sql = 'select * from t_title_img where id = {}'.format(i['id'])
    res = query(sql)
    print(res)
    assert len(res) != 0



    

