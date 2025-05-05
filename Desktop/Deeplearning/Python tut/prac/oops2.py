#Accessing and modifying the data:
#1.The traditional way:make the data private and use getters and setters function 
class user:
    def __init__(self,name,email,password):
        self.name=name
        self._email=email#protected attribute
        self.passw=password
    
    def get_email(self):
        return self._email

user1=user("shashank","shasank@gmail.com","abc")

print(user1._email)#protected can still be accessed
user1._email="fo1@gmail.com"#value of protected member can still be changed outside the class
print(user1._email)



