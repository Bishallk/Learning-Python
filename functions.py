def hello():
    print("hello")

hello()

def hello2(a,b,c,d=2):
    print(a,b,c,d)


hello2(2,3,4,5) #default parameter

hello2(d=30,b=2,a=5,c=20) #keyword parameter


#return keyword
def evenodd(a):
    if a%2==0:
        return("even")
    else:
        return("odd")
    

