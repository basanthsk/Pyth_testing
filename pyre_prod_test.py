import pyrebase

cp='C:/Users/Zaban/PycharmProjects/iucc-assaf.json'



config = {
  "apiKey": "AIzaSyDaFI7VkVvmyWUHw6XWcI_Ce0JHZY-9j9g",
  "authDomain": "iucc-assaf-anderson.firebaseapp.com",
  "databaseURL": "https://iucc-assaf-anderson.firebaseio.com/",
  "storageBucket": "gs://iucc-assaf-anderson.appspot.com",
  "serviceAccount": cp
}

fbase = pyrebase.initialize_app(config)

db = fbase.database()
# data = db.reference('Samples_List').order_by_child('title').equal_to('170131b').get()
data=db.child('Samples_List').order_by_child('title').equal_to('170131b').get()
print(data)

