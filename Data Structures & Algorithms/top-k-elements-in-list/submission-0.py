class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        value_map = {} # int : count
        for num in nums:
            if num not in value_map:
                value_map[num] = 1
            else:
                value_map[num] += 1

        dict_list = list(value_map.items())
        dict_list.sort(key = lambda item: item[1], reverse = True)
        top_k_pairs = dict_list[:k]
        return [pair[0] for pair in top_k_pairs]