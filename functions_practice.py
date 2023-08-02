def hello():
    print('Hello user')

hello()

def pack(x,y,z):
    return [x,y,z]

pack(1,2,3)

def eat_lunch(list):
    if len(list)==0:
        print("My lunch box is empty")
    else:
        for i in range(len(list)):
            if i==0:
                print(f"First I eat {list[0]}")
            else: 
                print(f"Next I eat {list[i]}")

eat_lunch([])
eat_lunch(['sandwich','apple','cake'])