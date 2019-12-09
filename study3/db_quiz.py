from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

som = db.movies.find_one({'title':'사운드 오브 뮤직'},{'_id':0})
som_star = som['star']
print('사운드 오브 뮤직 평점 : ',som_star)
print('===== 평점이 같은 영화 List =====')
all_movies = list(db.movies.find())
for i in all_movies:
    if i['star'] == som_star:
        print(i["title"])
#        db.movies.update_many({'star': som_star}, {'$set': {'star': '9.39'}})



print("=== 평점이 9.3점인 애들 List ===")
ls_movies = list(db.movies.find({'star': {'$eq': '9.33'}}))
for i in ls_movies:
    print(i['title'],i['star'])

#all_movies = list(db.movies.find())
#for i in all_movies:
#    target_star = (i['star'])