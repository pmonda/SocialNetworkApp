#authentication module for social media app

accounts = {} # key: username, value: hashed password

def signup():
  input("What is your username")
  input("Create your password")

def login(username ,pwd):
  authenticate_user(pwd)
  
def authenticate_user(credential):
  if credential == accounts[username]:
      print("successful login")
      return
  print("unsuccessful login attempt, try again.")
