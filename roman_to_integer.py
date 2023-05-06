class Solution:

    def __init__(self):
        self.roman = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }

    def romanToInt(self, s: str) -> int:
        sum = 0
        previous_char = ""
        for c in s:
            if previous_char and self.roman.get(previous_char + c):
                sum += self.roman.get(previous_char + c) - self.roman.get(previous_char)
                previous_char = ""
            elif self.roman.get(c):
                sum += self.roman.get(c)
                previous_char = c
        return sum


if __name__ == "__main__":
    roman = "IXIX"
    solution = Solution()
    x = solution.romanToInt(roman)
    print(x)