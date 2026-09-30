class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        result = []
        for idx in range(len(numbers)):
            if (target - numbers[idx]) in seen:
                result.append(seen[target - numbers[idx]] + 1)
                result.append( idx + 1)
                break

            seen[numbers[idx]] = idx

        return result

        