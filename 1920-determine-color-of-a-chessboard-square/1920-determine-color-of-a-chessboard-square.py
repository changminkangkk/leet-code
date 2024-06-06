class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        alfa = "abcdefghijklmnopqrstuvwxyz"
        if alfa.index(coordinates[0]) % 2 == 0:
            if int(coordinates[1]) % 2 == 0:
                return True
            else:
                return False
        else:
            if int(coordinates[1]) % 2 == 0:
                return False
            else:
                return True           