class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_chars = len(s)
        t_chars = len(t)

        result = True

        if s_chars != t_chars:
            return False

        s_map = {}
        t_map = {}

        k = 0
        while k != s_chars:
            if s[k] in s_map.keys():
                s_map[s[k]] += 1
            else:
                s_map[s[k]] = 1

            if t[k] in t_map.keys():
                t_map[t[k]] += 1
            else:
                t_map[t[k]] = 1
            
            k += 1

        
        if len(s_map.keys()) != len(t_map.keys()):
            result = False
            return False
        else:

            for i in s_map.keys():
                if i not in t_map.keys() or s_map[i] != t_map[i]:
                    result = False
                    break

        return result







        