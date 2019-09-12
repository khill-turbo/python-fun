class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here

    def computeDifference(self):
        #print("self.__elements = ", self.__elements)
        #print(max(self.__elements))
        #print(min(self.__elements))
        theMax = (max(self.__elements))
        theMin = (min(self.__elements))
        #print(theMax - theMin)
        self.maximumDifference = (theMax - theMin)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
