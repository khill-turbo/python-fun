class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binX = (format(x, "032b"))
        binY = (format(y, "032b"))
        resX = [int(a) for a in str(binX)]
        resY = [int(b) for b in str(binY)]
        counter = 0
        hamDist = 0
        while(counter < (len(resX))):
            if( (resX[counter]) != (resY[counter]) ):
                hamDist = (hamDist + 1)
            counter = (counter + 1)
            
        return hamDist
