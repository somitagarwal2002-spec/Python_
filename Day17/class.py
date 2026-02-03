class User: #first letter must be capital known as "PascalCase"
    def __init__(self, user_id, username): #constructor
        print("This constructor will be called everytime we create a new object")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# Pascal Case - UserName
# Camel Case - userName
# Snake Case - user_name

# user_1 = User()
# user_1.id = "001"
# user_1.username = "somit"

# print(user_1.username)

user_1 = User("001", "somit")
user_2 = User("002", "mohit")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# agr humne constructor bana diya hai to usme jo parameters diye gye
# hai wo hume pass krne hi honge
# like hum ab jb user_1 ko pehle jaise banaya to error aa gya ki
# parameters required 

print(user_2.id)
print(user_2.username)
print(user_2.followers)

def function():
    pass
# pass is a keyword to make empty classes or functions

print("hello")

# Constructor: What should happen when a object is being constructed
            #    or an object is initialized 

