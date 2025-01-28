class Profile:
  def __init_(self,username, hashed_pwd):
    self.username = username
    self.hashed_pwd = hashed_pwd
    self.follower = []
    self.following = []
    
  def viewProfile(self):
    pass
    
  def addFollower(self, follower):
    self.follower.append(follower)
  
  def removeFollower(self, follower):
    self.follower.remove(follower)
  
  def addFollowing(self, following):
    input(f"{following.username} has requested to follow you. Accept? (y/n)")
    if input().lower() == "y":
      self.following.append(following)
      following.addFollower(self)
