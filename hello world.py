for i in range(1,8):
    for j in range(1,200):
        if(i==1):
            if(j in [1,13,33,49,86,92,98,134] or j in range(17,30,2) or j in range(66,75,2) or j in range (104,113,2) or j in range (118,129,2) or j in range (150,161,2)):
                print("C", end="")
            else:
                print(" " ,end="")
        if(i==2):
            if(j in [1,13,17,33,49,64,76,86,92,98,102,114,118,130,134,150,162]):
                print("C",end="")
            else:
                print(" ",end="")
        if(i==3):
            if(j in [1,13,17,33,49,64,76,86,92,98,102,114,118,130,134,150,162]):
                print("C",end="")
            else:
                print(" ",end="")
        if(i==4):
            if(j in [33,49,64,76,86,92,98,102,114,134,150,162] or j in range (1,14,2) or j in range (17,30,2) or j in range (118,129,2)):
                print("C", end="")
            else:
                print(" ",end="")
        if(i==5):
            if(j in [1,13,17,33,49,64,76,86,92,98,102,114,118,130,134,150,162]):
                print("C",end="")
            else:
                print(" ",end="")
        if(i==6):
            if(j in [1,13,17,33,49,64,76,86,92,98,102,114,118,130,134,150,162]):
                print("C",end="")
            else:
                print(" ",end="")
        if(i==7):
            if(j in [1,13,88,90,94,96,118,130] or j in range(17,30,2) or j in range (33,46,2) or j in range (49,61,2) or j in range (66,75,2) or j in range (104,113,2) or j in range (134,147,2) or j in range (150,161,2)):
                print("C",end="")
            else:
                print(" ",end="")
    print("\r")
        