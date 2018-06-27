import pyrebase

cp='C:/Users/Zaban/PycharmProjects/staging-c6770.json'



config = {
  "apiKey": "AIzaSyD8qqwGnP_tG0ZFW261bQ0h-ACkXJsAsyY",
  "authDomain": "staging-c6770.firebaseapp.com",
  "databaseURL": "https://staging-c6770.firebaseio.com/",
  "storageBucket": "gs://staging-c6770.appspot.com",
  "serviceAccount": cp
}

fbase = pyrebase.initialize_app(config)

db = fbase.database()
# data = db.reference('Samples_List').order_by_child('title').equal_to('170131b').get()
data=db.child('Samples_List').order_by_child('title').equal_to('141209b').get()

for d in data.each():
  print(d.key())