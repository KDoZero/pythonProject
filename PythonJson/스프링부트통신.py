import requests
import json

data = {
    "id" : "ehdudloro김",
    "pwd" : "ehdud0127"
}
# JSON 데이터를 스프링부트 서버로 전송하기
url = "http://localhost:8111/auth/python"
headers = {"Content-Type" : "application/json"}
response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 200 :
    print(response.content)
else :
    print("데이터 전송에 실패했습니다. 응답 코드 : ", response.status_code)