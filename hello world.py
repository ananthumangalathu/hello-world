for i in range(1,8):
    for j in range(1,200):
        if(i==1):
            if(j in [1,11,30,44,83,89,95,129] or j in range(15,26,2) or j in range(58,69,2) or j in range (99,110,2) or j in range (114,125,2) or j in range (143,154,2)):
                print("C", end="")
            else:
                print(" " ,end="")
        if(i==2):
            if(j in [1,11,15,30,44,58,68,83,89,95,99,109,114,124,129,143,153]):
                print("C",end="")
            else:
                print(" ",end="")
        if(i==3):
            if(j in [1,11,15,30,44,58,68,83,89,95,99,109,114,124,129,143,153]):
                print("C",end="")
            else:
                print(" ",end="")
        if(i==4):
            if(j in [30,44,58,68,83,89,95,99,109,129,143,153] or j in range (1,12,2) or j in range (15,26,2) or j in range (114,125,2)):
                print("C", end="")
            else:
                print(" ",end="")
        if(i==5):
            if(j in [1,11,15,30,44,58,68,83,89,95,99,109,114,124,129,143,153]):
                print("C",end="")
            else:
                print(" ",end="")
        if(i==6):
            if(j in [1,11,15,30,44,58,68,83,89,95,99,109,114,124,129,143,153]):
                print("C",end="")
            else:
                print(" ",end="")
        if(i==7):
            if(j in [1,11,114,124] or j in range(15,26,2) or j in range (30,41,2) or j in range (44,55,2) or j in range (58,69,2) or j in range (83,96,2) or j in range (99,110,2) or j in range (129,140,2) or j in range (143,154,2)):
                print("C",end="")
            else:
                print(" ",end="")
    print("\r")
        