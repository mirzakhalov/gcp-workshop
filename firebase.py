## some code snippets from here can be found at https://github.com/thisbejim/Pyrebase

import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com",
  "serviceAccount": "path/to/serviceAccountCredentials.json"
}

firebase = pyrebase.initialize_app(config)

# # build paths
# db = firebase.database()
# db.child("Users").child("jim")

# # set() and push() data
# data = {"name": "Jim", "age": 21, "job": "presenter"}
# db.child("Users/jim").set(data)
# db.child("Users/").push(data)

# # update() 
# data = {"name": "Jim", "age": 22, "job": "presenter"}
# db.child("User/jim").update(data)










