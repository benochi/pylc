class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        if bills[0] != 5:
            return False

        for b in bills:
            if b == 5: fives += 1
            if b == 10: tens += 1
            changeNeeded = b - 5
            while changeNeeded > 0:
                while changeNeeded >= 10 and tens > 0:
                    tens -= 1
                    changeNeeded -= 10
                while changeNeeded >= 5 and fives > 0:
                    fives -= 1
                    changeNeeded -= 5
                if changeNeeded > 0:
                    return False
        return True