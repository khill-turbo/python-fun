class Solution:
    def canWinNim(self, n: int) -> bool:
        # carefully map out possible game play
        # this shows numbers evenly divisble by 4 result in you losing the game
    
        if((n%4) == 0 ):
            return(0)
        else:
            return(1)
