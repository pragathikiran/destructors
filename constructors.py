class employee:
 def __init__(self):
    print("employee crated")

    def __del__(self):
     print("deatructor called,employee deleted")
    
obj = employee()
del obj
     
