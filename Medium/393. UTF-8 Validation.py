class Solution:
    vaild = [["0"],
             ["110", "10"],
             ["1110", "10", "10"],
             ["11110", "10", "10", "10"]]

    def validUtf8(self, data: list) -> bool:
        data = ["{0:b}".format(x).zfill(8) for x in data]

        i = 0
        while i < len(data):
            for j in range(i,i+4):
                curData = data[i:j+1]
                if self.helper(curData):
                    i = j+1
                    break
            else:
                return False

        return True

    def helper(self, data:list):
        vaild = self.vaild[len(data)-1]
        for i in range(len(data)):
            if not data[i].startswith(vaild[i]):
                return False

        return True