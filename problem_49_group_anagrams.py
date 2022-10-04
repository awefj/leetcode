import collections


class Solution(object):
    def groupAnagrams(self, strs:list[str])->list[list[str]]:
        """
        :param strs:
        :return:
        """
        res = collections.defaultdict(list)
        for item in strs:
            res[''.join(sorted(item))].append(item)
        #return list(res.values())
        return [item for item in res.values()]

s=Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))