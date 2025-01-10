class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        billMap ={
            5:0, 
            10:0, 
            20:0
        }

        if bills[0] != 5:
            return False

        for b in bills:
            billMap[b] += 1
            changeNeeded = b - 5
            while changeNeeded > 0:
                while changeNeeded >= 10 and billMap[10] > 0:
                    billMap[10] -= 1
                    changeNeeded -= 10
                while changeNeeded >= 5 and billMap[5]:
                    billMap[5] -= 1
                    changeNeeded -= 5
                if changeNeeded > 0:
                    return False
        return True