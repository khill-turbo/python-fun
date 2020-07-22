def digital_root(n):
    print(n)

    myList = []
    print(myList)

    myAdder = 0
    print(myAdder)
    
    myString = str(n)
    
    for i in myString:
        myIntPartTwo = int(i)
        myList.append(myIntPartTwo)
        myAdder = (myAdder + myIntPartTwo)
        
    print(myAdder)
    if myAdder > 9:
        digital_root(myAdder)
    else:
        return(myAdder)
