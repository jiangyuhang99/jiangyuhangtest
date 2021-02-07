# post 
import requests
from dbtools import query

url = 'http://118.24.255.132:2333/login'
#{"username":"zhang111","password":"a1234567", "phone":"13980898845","email":"98268626@qq.com"}
data = {'username':'zhang111','password':'a1234567'}
h = {"Content-Type":"application/json"}

res = requests.post(url=url,json=data,headers=h)
assert res.status_code == 200  #状态码的判断
assert res.json()['status'] == 200   #结果码的判断

sql = "select * from t_user where username='zhang111'"
assert len(query(sql)) != 0
print('接口测试成功')

token = res.json()['data']['token']

url1 = 'http://118.24.255.132:2333/inspirer/new'
header1 = {"Content-Type":"application/json","token":token}
data1 = {"content":"这是来自星星的数据","ximg":"dsfsdf.jpg"}
res1 = requests.post(url=url1,json=data1,headers=header1)
print(res1.text)
