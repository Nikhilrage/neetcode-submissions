class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in hm:
                hm[sorted_word] = [word]
            else:
                hm[sorted_word].append(word)


        return list(hm.values())