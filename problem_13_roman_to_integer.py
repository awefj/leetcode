class Solution(object):
    roman = [('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)]
    def romanToInt(self, s):
        """
        :param s: string
        :return: int
        """
        res = 0
        prv = 0
        for i in s:
            for j in self.roman:
                if i == j[0]:
                    if prv < j[1]:
                        res += (j[1] - 2 *prv)
                    else:
                        res += j[1]
                    prv = j[1]
        return res
