class Solution:
    def letterCombinations(self, digits):
        if len(digits) < 1:
            return []

        letterMap = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"]
            }
        result = [""]
        for num in digits:
            temp = []
            for combo in result:
                print(combo)
                for letter in letterMap[num]:
                    temp.append(combo + letter)
            result = temp
        
        return result