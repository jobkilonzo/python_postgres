from user import User
from database import Database

Database.initialise(user="postgres", password="scusi", database="learning", host="localhost")
my_user = User('john@gmail.com', 'John', 'Jones', None)

user = my_user.load_from_db_by_email('jobkilonzo@gmail.com')

print(user)
