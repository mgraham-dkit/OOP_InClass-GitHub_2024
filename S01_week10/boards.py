from roles import User


user1 = User("michelle", "password")
user2 = User("mgraham", "password")
user3 = User("grahamm", "password")
user4 = User("Heidi", "password")
user5 = User("KHeidi", "password")

users = [user1, user2, user3, user4, user5]
print("Before sorting:")
print(users)

input("Enter any key to continue:")

# users.sort()
# print("After sorting: ")
# print(users)

print(f"The min User found is: {min(users)}")
