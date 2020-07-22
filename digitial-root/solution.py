def digital_root(n):
    # initialize listSummation in case n less than 9 and therefore while loop isn't entered
    listSummation = n
    while n > 9:
        # need to reset nList if n is still greater than one digit
        nList = []
        # which means you also need to reset nToString
        nToString = str(n)
        for i in nToString:
            # need to reset listSummation every time you restart walk through the list
            listSummation = 0
            # add elements to the list
            nList.append(int(i))
            # create a summation of the elements in the list
            for j in nList:
                listSummation = (listSummation + j)
        # need to set n to listSummation to get out of the while loop
        n = listSummation

    return(listSummation)
