a = 'spartacodingclub@gmail.com'
b = 'spartacodingclubgmail.com'

list = ['사과','감','감','배','포도','포도','딸기','포도','감','수박','딸기']
dic = {"사과":0,"감":0,"배":0,"포토":0,"딸기":0}

#채워야하는 함수
def check_mail(s):
	## 여기에 코딩을 해주세요
    mail_list = s.split('@');

    if len(mail_list) == 1:
        return "@가 없습니다 ==> FALSE"
    else: return True;

print(check_mail(a));

def count_list(a_list):
  result = {}
  for element in a_list:
    if element in result:
      result[element] += 1
    else:
      result[element] = 1
  return result

#결과값
print(count_list(list))


import random

def get_lotto():
  lotto_range = range(1,47)
  lotto_nums = random.sample(lotto_range,6)
  return lotto_nums

print(get_lotto())


