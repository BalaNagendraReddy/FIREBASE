import pyrebase


# Your Webapp Firebase configuration
firebaseConfig = {
  'apiKey': "firebase_Api_Key",
  'authDomain': "crudfirebase-f69bf.firebaseapp.com",
  'projectId': "crudfirebase-f69bf",
  'databaseURL': "YOUR DATABASE URL",
  'storageBucket': "crudfirebase-f69bf.appspot.com",
  'messagingSenderId': "1004590374878",
  'appId': "1:1004590374888:web:c34fc55c7f365a73248e5d",
  'measurementId': "G-BP2X04NFYL"
}

firebase = pyrebase.initialize_app(firebaseConfig)

database = firebase.database()
data = {"Age":30, "Name":'Nagendra', "Likes Pizza": True}

# CREATE DATA
# database.push(data)    
# or
database.child("Users").child("FirstPerson").set(data)

# READ DATA
nagendra = database.child("Users").child("FirstPerson").get()
print(nagendra.val())

# UPDATE DATA
database.child("Users").child("FirstPerson").update({"Name":"Bala Nagendra"})

# Remove one field data
database.child("Users").child("FirstPerson").child("Age").remove()

# Delete whole Node
# database.child("Users").child("FirstPerson").remove()
