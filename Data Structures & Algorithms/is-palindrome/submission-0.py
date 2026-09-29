class Solution:
    def isPalindrome(self, s: str) -> bool:

        d = "".join(char.lower() for char in s if char.isalnum())

        result = True

        p1 = 0
        p2 = len(d) - 1


        while p1 < p2:
            print("dd")

            if d[p1] != d[p2]:
                result = False
                break
            p1 += 1
            p2 -= 1


        return result

        