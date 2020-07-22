def digital_root(n):
    
    while n > 9:
        #print(n)
        myList = []
        myString = str(n)
        for i in myString:
            myAdder = 0
            myIntPartTwo = int(i)
            myList.append(myIntPartTwo)
            #print(myList)
            #print("myAdder = ", myAdder)
            for j in myList:
                #print("j = ", j)
                myAdder = (myAdder + j)
            #print("myAdder = ", myAdder)
        n = myAdder

    #print("myAdder = ", myAdder)
    #print("n = ", n)
    #print("myString = ", myString)
    
    return(myAdder)
