for i in range(1,8):
    for j in range(1,200):
        if(i==1):
            if(j in [1,11,30,44,73,79,85,119] or j in range(15,26,2) or j in range(58,69,2) or j in range (89,100,2) or j in range (104,115,2) or j in range (132,143,2)):
                print("C", end="")
            else:
                print(" " ,end="")
        if(i==2):
            if(j in [1,11,15,30,44,58,68,73,79,85,89,99,104,114,119,132,142]):
                print("C",end="")
            else:
                print(" ",end="")
    print("\r")
        