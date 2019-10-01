class Solution:
    def candy(self, ratings: list) -> int:
        if not ratings: return 0

        width = 0
        height = 0
        change = 0
        candy = len(ratings)
        
        for i in range(1, len(ratings)):
            if ratings[i-1] > ratings[i]:
                candy += width
                height = 0
                if change <= width:
                    candy += 1
                width += 1

            elif ratings[i-1] < ratings[i]:
                width = 0
                height += 1
                candy += height
                change = height

            else:
                width = 0
                height = 0
                change = 0

        return candy