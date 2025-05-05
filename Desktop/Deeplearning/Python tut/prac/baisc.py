# print("Hwllo  i love eating food !What about you")
# print("nO I dont like much. I like to be as fit as i can ve c;")


def appl(f,val):
    return f(val)+4
# //lambda function
#M.1
cube=lambda x:x**3
print(appl(cube,3))


#M.2
print(appl(lambda x:x**3,3))

# *args(positional arguments), **kwargs(keyword arguements)
def pizzahut(sizw,*args,**kwargs):
    print(f"The pizza is of {sizw} size and is having these features")
    for i in args:
        print(f"-{i}")
    for key,value in kwargs.items():
        print(f"{key,value}")
            
        
pizzahut("large","suacy","cheesy",flavour="salty",cost="high") 


