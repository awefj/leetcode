import time


class Solution(object):
    def longestPalindrome00(self,s:str)->str:
        """
        brute-force
        :param s:
        :return:
        """
        longest=s[:1]
        for i in range(len(s)+1):
            for j in range(i+2 ,len(s)+1):
                temp = ''.join(reversed(s[i:j]))
                #print(i,j,temp)
                if s[i:j] == temp and len(longest) < len(temp):
                    longest = s[i:j]
        return longest

    def longestPalindrome01(self,s):
        def expand(left:int, right:int)-> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return s[left + 1:right]
        if len(s) < 2 or s == s[::-1]:
            return s
        result = ''
        for i in range(len(s)-1):
            result = max(result, expand(i,i+1), expand(i, i+2), key=len)
        return result

s = Solution()
start = time.time()
print(s.longestPalindrome00("anugnxshgonmqydttcvmtsoaprxnhpmpovdolbidqiyqubirkvhwppcdyeouvgedccipsvnobrccbndzjdbgxkzdbcjsjjovnhpnbkurxqfupiprpbiwqdnwaqvjbqoaqzkqgdxkfczdkznqxvupdmnyiidqpnbvgjraszbvvztpapxmomnghfaywkzlrupvjpcvascgvstqmvuveiiixjmdofdwyvhgkydrnfuojhzulhobyhtsxmcovwmamjwljioevhafdlpjpmqstguqhrhvsdvinphejfbdvrvabthpyyphyqharjvzriosrdnwmaxtgriivdqlmugtagvsoylqfwhjpmjxcysfujdvcqovxabjdbvyvembfpahvyoybdhweikcgnzrdqlzusgoobysfmlzifwjzlazuepimhbgkrfimmemhayxeqxynewcnynmgyjcwrpqnayvxoebgyjusppfpsfeonfwnbsdonucaipoafavmlrrlplnnbsaghbawooabsjndqnvruuwvllpvvhuepmqtprgktnwxmflmmbifbbsfthbeafseqrgwnwjxkkcqgbucwusjdipxuekanzwimuizqynaxrvicyzjhulqjshtsqswehnozehmbsdmacciflcgsrlyhjukpvosptmsjfteoimtewkrivdllqiotvtrubgkfcacvgqzxjmhmmqlikrtfrurltgtcreafcgisjpvasiwmhcofqkcteudgjoqqmtucnwcocsoiqtfuoazxdayricnmwcganugnxshgonmqydttcvmtsoaprxnhpmpovdolbidqiyqubirkvhwppcdyeouvgedccipsvnobrccbndzjdbgxkzdbcjsjjovnhpnbkurxqfupiprpbiwqdnwaqvjbqoaqzkqgdxkfczdkznqxvupdmnyiidqpnbvgjraszbvvztpapxmomnghfaywkzlrupvjpcvascgvstqmvuveiiixjmdofdwyvhgkydrnfuojhzulhobyhtsxmcovwmamjwljioevhafdlpjpmqstguqhrhvsdvinphejfbdvrvabthpyyphyqharjvzriosrdnwmaxtgriivdqlmugtagvsoylqfwhjpmjxcysfujdvcqovxabjdbvyvembfpahvyoybdhweikcgnzrdqlzusgoobysfmlzifwjzlazuepimhbgkrfimmemhayxeqxynewcnynmgyjcwrpqnayvxoebgyjusppfpsfeonfwnbsdonucaipoafavmlrrlplnnbsaghbawooabsjndqnvruuwvllpvvhuepmqtprgktnwxmflmmbifbbsfthbeafseqrgwnwjxkkcqgbucwusjdipxuekanzwimuizqynaxrvicyzjhulqjshtsqswehnozehmbsdmacciflcgsrlyhjukpvosptmsjfteoimtewkrivdllqiotvtrubgkfcacvgqzxjmhmmqlikrtfrurltgtcreafcgisjpvasiwmhcofqkcteudgjoqqmtucnwcocsoiqtfuoazxdayricnmwcg"))
end = time.time()
print(end-start)
start = time.time()
print(s.longestPalindrome01("anugnxshgonmqydttcvmtsoaprxnhpmpovdolbidqiyqubirkvhwppcdyeouvgedccipsvnobrccbndzjdbgxkzdbcjsjjovnhpnbkurxqfupiprpbiwqdnwaqvjbqoaqzkqgdxkfczdkznqxvupdmnyiidqpnbvgjraszbvvztpapxmomnghfaywkzlrupvjpcvascgvstqmvuveiiixjmdofdwyvhgkydrnfuojhzulhobyhtsxmcovwmamjwljioevhafdlpjpmqstguqhrhvsdvinphejfbdvrvabthpyyphyqharjvzriosrdnwmaxtgriivdqlmugtagvsoylqfwhjpmjxcysfujdvcqovxabjdbvyvembfpahvyoybdhweikcgnzrdqlzusgoobysfmlzifwjzlazuepimhbgkrfimmemhayxeqxynewcnynmgyjcwrpqnayvxoebgyjusppfpsfeonfwnbsdonucaipoafavmlrrlplnnbsaghbawooabsjndqnvruuwvllpvvhuepmqtprgktnwxmflmmbifbbsfthbeafseqrgwnwjxkkcqgbucwusjdipxuekanzwimuizqynaxrvicyzjhulqjshtsqswehnozehmbsdmacciflcgsrlyhjukpvosptmsjfteoimtewkrivdllqiotvtrubgkfcacvgqzxjmhmmqlikrtfrurltgtcreafcgisjpvasiwmhcofqkcteudgjoqqmtucnwcocsoiqtfuoazxdayricnmwcganugnxshgonmqydttcvmtsoaprxnhpmpovdolbidqiyqubirkvhwppcdyeouvgedccipsvnobrccbndzjdbgxkzdbcjsjjovnhpnbkurxqfupiprpbiwqdnwaqvjbqoaqzkqgdxkfczdkznqxvupdmnyiidqpnbvgjraszbvvztpapxmomnghfaywkzlrupvjpcvascgvstqmvuveiiixjmdofdwyvhgkydrnfuojhzulhobyhtsxmcovwmamjwljioevhafdlpjpmqstguqhrhvsdvinphejfbdvrvabthpyyphyqharjvzriosrdnwmaxtgriivdqlmugtagvsoylqfwhjpmjxcysfujdvcqovxabjdbvyvembfpahvyoybdhweikcgnzrdqlzusgoobysfmlzifwjzlazuepimhbgkrfimmemhayxeqxynewcnynmgyjcwrpqnayvxoebgyjusppfpsfeonfwnbsdonucaipoafavmlrrlplnnbsaghbawooabsjndqnvruuwvllpvvhuepmqtprgktnwxmflmmbifbbsfthbeafseqrgwnwjxkkcqgbucwusjdipxuekanzwimuizqynaxrvicyzjhulqjshtsqswehnozehmbsdmacciflcgsrlyhjukpvosptmsjfteoimtewkrivdllqiotvtrubgkfcacvgqzxjmhmmqlikrtfrurltgtcreafcgisjpvasiwmhcofqkcteudgjoqqmtucnwcocsoiqtfuoazxdayricnmwcg"))
end = time.time()
print(end-start)