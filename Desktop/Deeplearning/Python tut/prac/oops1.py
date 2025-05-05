class dog:
    def __init__(self ,name ,breed,owner):#contructor in python
        self.name=name
        self.breed=breed
        self.owner=owner
        
    def bark(self):#function
        print("Whoo Whoo")
        

class owner:
    
    def __init__(self,name,address,contact_number):
        self.name=name
        self.address=address
        self.mob_number=contact_number
        
        
owner1=owner("Aditya p.","IIT ISM ","23JE0051")#object of owner class 
dog1=dog("Bruce","Scottish Terrier",owner1)#object of dog class  made

print(dog1.name)
print(dog1.breed) 

dog1.bark()#function called 

dog1.owner.name
print(f"Owner of dog named {dog1.name} is:{dog1.owner.name}")