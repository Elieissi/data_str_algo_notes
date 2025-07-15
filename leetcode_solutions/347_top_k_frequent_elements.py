class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        the = {}

        for num in nums:
            the[num] = the.get(num, 0) + 1

        sorte = sorted(the.items(), key=lambda x: x[1], reverse=True)

        top_k = []
        counter = 0
        for key, value in sorte:
            if counter == k:
                break
            top_k.append(key)
            counter += 1

        return top_k