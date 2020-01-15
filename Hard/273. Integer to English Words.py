class Solution:
    def __init__(self):
        self.numbers = {
                0:"Zero",
                1:"One",
                2:"Two",
                3:"Three",
                4:"Four",
                5:"Five",
                6:"Six",
                7:"Seven",
                8:"Eight",
                9:"Nine",
                10:"Ten",
                11:"Eleven",
                12:"Twelve",
                13:"Thirteen",
                14:"Fourteen",
                15:"Fifteen",
                16:"Sixteen",
                17:"Seventeen",
                18:"Eighteen",
                19:"Nineteen",
                20:"Twenty",
                30:"Thirty",
                40:"Forty",
                50:"Fifty",
                60:"Sixty",
                70:"Seventy",
                80:"Eighty",
                90:"Ninety",
                100:"Hundred",
                1000:"Thousand",
                1000000:"Million",
                1000000000:"Billion"}
    def numberToWords(self, num: int) -> str:
        if num <= 20:
            return self.numbers[num]
        elif num < 100:
            return self.numbers[num - num%10] + (bool(num%10))*(" " + self.numbers[num%10])
        elif num < 1000:
            return self.numbers[num//100] + " " + self.numbers[100] + bool(num%100)*(" " + self.numberToWords(num%100))
        elif num < 1000000:
            return self.numberToWords(num//1000) + " " + self.numbers[1000] + bool(num%1000)*(" " + self.numberToWords(num%1000))
        elif num < 1000000000:
            return self.numberToWords(num//1000000) + " " + self.numbers[1000000] + bool(num%1000000)*(" " + self.numberToWords(num%1000000))
        else:
            return self.numberToWords(num//1000000000) + " " + self.numbers[1000000000] + bool(num%1000000000)*(" " + self.numberToWords(num%1000000000))
 