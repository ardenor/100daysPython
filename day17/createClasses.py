class User: #__init__ runs/initializes every time object created from Class
    def __init__(self, user_id, username):
        print("New user created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User("001", "colin")


#print(user1.id, user1.username, user1.followers)

user2 = User("","")
user2.id = "002"
user2.username = "xyz"

#print(user2.id, user2.username)

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)