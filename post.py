import time

class Post:
    def __init__(self, user, content, format, timestamp):
        self.user = user
        self.content = content
        self.format = format
        self.timestamp = time.time()
    
    