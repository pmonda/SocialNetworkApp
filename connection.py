class Connection:
  def __init__(self, fromUser, toUser):
    self.fromUser = fromUser
    self.toUser = toUser
    
  def friendReq(self, fromUser, toUser):
    print(f"{fromUser} has requested to be friends with {toUser}")
