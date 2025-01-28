import time

class Profile:
  
  def __init_(self,username, hashed_pwd):
    self.username = username
    self.hashed_pwd = hashed_pwd
    self.account_age = time.time()

  def viewProfile(self):
    print(f"username : {username}")
    print(f"account age: {time.time() - self.account_age})
