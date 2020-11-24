class Solution:
    def romanToInt(self, s: str) -> int:
        romanSymbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        tmp = 0
        res = 0
        for ch in s:
            digit = romanSymbols[ch]
            if digit < tmp:
                res += tmp
                tmp = digit
            elif digit > tmp:
                if tmp == 0:
                    tmp = digit
                else:
                    res += digit - tmp
                    tmp = 0
            elif digit == tmp:
                res += digit + tmp
                tmp = 0
        return res + tmp

data = input("Введите число в римской нотации")
solution = Solution()
print(solution.romanToInt(data))
input()


