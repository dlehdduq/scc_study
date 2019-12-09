import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json() # 텍스트로 반환된 것들을 json화 시킨다!
print("!!! r --> ",r)
print(rjson);
print (rjson['RealtimeCityAir']['row'][0]['NO2'])