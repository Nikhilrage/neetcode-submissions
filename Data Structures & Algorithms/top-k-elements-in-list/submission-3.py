class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sequence_tracker = {}


        for i in nums:
            if i in sequence_tracker:
                sequence_tracker[i] += 1
            else:
                sequence_tracker[i] = 1

        k_el = []

        while len(k_el) != k:
            max_freq = (list(sequence_tracker.keys()))[0]

            for key, value in sequence_tracker.items():
                if value > sequence_tracker[max_freq] and key not in k_el:
                    max_freq = key

            k_el.append(max_freq)
            del sequence_tracker[max_freq]

        return k_el