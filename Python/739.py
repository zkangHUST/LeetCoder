class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        i = 0
        res = []
        maxnum = max(temperatures)
        while (i < len(temperatures)):
            value = temperatures[i]
            index = self.find(temperatures, value, i + 1, maxnum)
            if (index == -1):
                res.append(0)
            else:
                res.append(index - i)
            i += 1
            while(i < len(temperatures) and temperatures[i] >= value and i < index):
                    res.append(index - i)
                    i += 1
        return res

    def find(self, nums, value, i, maxnum):
        if (value >= maxnum):
            return -1
        while(i < len(nums)):
            if nums[i] > value:
                return i
            i+=1
        return -1
temperatures = [34,34,47,47,34,34,34,47,34,47,47,47,34,34,34,47,47,34,47,47,34,34,34,34,47,34,34,47,34,34,34,47,47,47,47,47,47,34,34,34,47,34,34,47,34,47,47,47,34,47,47,34,47,34,47,47,34,47,47,34,34,47,47,47,34,34,47,47,47,34,34,47,34,34,34,47,47,34,34,47,47,47,47,47,34,34,34,47,47,34,47,34,47,34,34,47,34,47,47,47,47,47,47,34,34,34,47,34,47,34,47,34,34,34,34,47,34,34,34,34,34,34,34,47,34,34,47,47,34,47,47,47,47,47,47,47,34,34,47,34,47,34,47,34,34,34,47,34,34,47,34,47,47,34,47,47,47,47,34,34,34,34,47,47,34,34,34,47,34,34,47,34,34,47,34,34,34,34,47,34,34,34,47,34,34,47,47,34,47,47,34,34,34,34,34,34,47,47,34,47,34,47,34,47,47,47,34,47,34,34,34,34,34,47,47,47,47,47,47,34,47,34,47,34,34,34,47,47,47,34,47,47,34,47,47,47,34,47,47,34,47,47,34,47,34,34,47,47,34,34,34,34,47,34,34,47,47,34,47,47,34,34,34,34,47,47,34,34,47,47,34,47,34,47,34,47,47,47,47,34,34,47,47,34,34,34,47,34,47,47,47,34,47,47,34,34,34,34,34,47,47,34,47,47,34,34,47,34,47,47,34,47,47,47,47,47,47,47,34,34,34,34,47,47,34,47,34,47,47,34,47,47,34,34,34,47,47,47,34,47,34,47,47,47,34,34,34,34,34,34,34,47,34,34,34,34,47,47,34,34,47,34,47,47,34,47,34,34,47,47,47,47,47,47,34,34,47,34,34,47,34,47,47,47,47,47,34,34,34,47,47,34,47,34,34,47,47,47,34,34,47,47,47,34,34,47,47,34,34,47,47,47,47,34,34,34,47,34,34,47,47,34,34,34,47,34,34,47,34,34,34,34,47,34,47,34,47,47,47,34,34,47,47,47,47,47,34,47,34,34,34,34,34,47,47,34,34,47,47,34,34,47,34,47,34,47,34,47,47,47,47,47,47,47,47,47,34,47,47,47,34,47,47,34,34,47,34,47,34,34,47,47,47,47,34,47,34,34,34,47,47,47,34,34,47,47,34,34,34,34,47,47,34,47,34,34,47,47,34,47,34,47,34,47,34,34,47,34,47,34,47,34,47,47,47,47,47,34,34,47,47,34,34,34,47,34,34,34,34,34,47,47,47,34,47,47,47,47,47,47,47,47,34,34,34,34,47,34,47,34,47,47,47,34,34,34,34,47,34,47,34,47,34,47,34,34,34,47,34,47,34,34,47,34,34,47,34,34,47,47,47,34,47,47,47,34,34,34,34,34,34,34,47,34,34,47,34,47,34,47,34,34,34,34,47,47,47,47,34,47,34,34,34,47,34,47,47,47,34,34,47,34,47,47,34,47,34,34,34,47,34,34,34,47,34,34,34,34,34,34,47,47,47,47,34,47,47,34,47,34,47,34,47,34,47,34,34,47,34,47,34,47,34,34,34,34,34,47,47,47,47,47,47,47,47,47,34,47,47,34,34,34,47,34,34,47,47,34,47,47,47,47,47,47,47,34,47,34,47,47,47,47,47,47,34,47,47,34,34,34,47,47,47,47,34,34,47,47,34,34,34,34,34,47,34,34,34,34,47,47,34,47,47,47,47,47,47,47,34,34,47,34,47,34,47,47,47,47,34,47,47,47,34,34,34,34,34,34,47,47,47,34,34,34,47,47,34,47,34,47,47,47,34,47,47,47,47,47,47,47,34,47,47,47,34,34,47,47,34,47,47,34,34,34,47,34,47,34,34,47,34,47,34,34,34,34,47,47,47,34,47,34,47,47,34,47,34,47,34,47,34,47,47,47,34,34,47,34,47,34,47,47,47,47,47,34,47,34,47,34,47,34,34,47,47,47,47,47,34,47,34,47,47,47,47,47,47,47,34,47,47,47,34,34,34,47,34,47,47,47,47,34,47,47,34,47,34,34,47,47,34,34,47,34,47,47,47,47,34,47,47,34,34,34,47,47,34,34,47,34,47,34,47,34,47,47,47,47,34,47,47,34,34,34,47,34,47,34,47,34,34,34,47,34,34,34,34,34,34,47,47,47,34,47,47,47,34,34,34,34,47,34,34,47,34,34,47,47,34,34,47,34,34,47,34,34,47,34,47,47,34,47,47,34,34,47,47,34,34,47,34,34,47,47,34,47,34,34,47,47,47,34,34,47,47,34,34,34,47,47,34,47,34,47,47,34,34,34,47,47,47,47,34,47,47,34,47,47,34,47,34,47,34,47,47,34,34,47,47,47,34,47,47,47,34,34,34,47,47,47,47,34,47,47,34,34,34,34,34,34,34,34,47,34,47,47,34,47,47,34,47,47,47,47,47,34,47,34,34,34,34,47,47,47,47,34,34,34,47,34,34,34,47,47,34,47,47,34,47,34,34,34,47,34,47,47,47,34,34,34,34,47,47,47,34,47,47,47,34,47,34,47,34,34,47,47,47,47,34,47,34,47,34,47,34,34,34,47,34,34,34,47,34,34,47,34,47,34,47,47,34,34,47,34,47,47,47,34,47,34,47,34,47,47,47,47,34,34,34,34,34,34,34,47,47,47,47,34,47,34,34,47,34,47,34,34,34,47,47,34,34,34,47,34,47,47,47,34,34,47,47,47,47,34,34,34,47,47,34,47,34,34,34,34,34,47,47,47,47,47,34,34,34,34,47,47,34,47,47,47,34,34,47,34,34,34,34,34,34,34,47,47,34,47,34,47,47,34,47,47,47,34,34,47,47,34,34,34,47,47,47,34,34,34,34,47,34,47,34,34,47,47,47,47,34,47,34,47,47,47,47,34,34,47,47,47,34,47,34,47,34,34,47,34,47,47,47,34,34,34,34,47,47,47,34,34,47,47,47,34,34,47,34,47,34,47,34,47,34,34,47,47,47,34,47,34,47,47,47,34,34,34,34,34,47,34,47,47,47,47,34,47,47,47,47,34,34,47,47,47,34,34,34,34,34,47,34,47,47,34,47,47,47,34,47,34,47,47,34,47,34,47,34,34,47,34,34,47,34,34,34,34,34,47,34,47,34,47,47,34,47,47,34,34,47,34,34,47,34,34,47,47,34,47,34,34,47,47,47,47,47,34,47,47,47,47,34,34,34,47,47,34,34,34,47,34,34,47,47,34,34,47,34,34,34,47,47,47,34,34,34,47,47,47,34,47,47,34,47,34,34,47,47,47,34,47,34,47,34,34,47,34,34,47,47,34,34,47,47,34,34,47,47,47,34,34,47,34,34,47,47,47,34,34,47,34,34,34,47,47,47,34,34,47,47,34,34,47,47,34,34,47,47,47,47,47,34,47,47,47,34,47,47,34,34,47,34,47,34,34,34,47,47,47,47,47,47,34,34,47,47,47,34,34,34,34,34,34,34,34,47,34,34,34,34,34,47,34,34,34,47,47,34,34,34,47,34,47,47,34,47,34,34,34,47,47,34,47,34,47,34,34,47,34,47,34,34,47,47,34,34,34,47,34,34,34,34,47,34,47,47,34,34,34,47,47,34,34,34,47,47,47,34,34,47,34,47,34,47,34,34,34,47,34,47,34,34,34,47,47,34,34,47,34,47,34,34,34,34,47,47,47,47,47,34,47,47,34,47,34,34,34,34,34,34,34,47,47,34,34,47,47,47,34,34,34,47,34,34,34,34,34,47,34,47,47,34,47,47,34,34,34,34,47,34,34,47,47,34,34,34,34,47,47,47,47,34,47,34,47,47,34,34,47,34,47,47,34,34,34,34,34,34,34,47,34,34,34,47,34,34,34,34,34,47,47,47,47,34,47,47,34,34,47,34,47,47,34,34,34,47,47,34,47,47,47,47,47,34,47,34,34,47,47,34,34,34,47,47,34,34,47,34,34,34,47,34,34,47,47,34,47,34,34,47,47,47,47,34,34,34,34,34,34,34,47,47,47,34,34,47,47,47,34,47,34,47,34,34,47,47,47,47,34,47,34,47,47,34,34,34,34,47,47,47,47,34,34,47,34,34,47,34,34,47,34,47,34,34,47,34,34,34,47,34,34,34,47,47,47,34,47,34,34,47,47,47,34,34,47,34,47,47,34,47,47,47,47,47,34,34,34,47,34,34,34,34,47,34,34,47,34,34,34,34,47,47,34,47,47,34,47,34,34,47,34,47,47,47,34,47,34,34,34,47,47,47,47,34,47,47,34,34,47,47,34,47,47,34,47,34,34,47,34,34,34,34,34,34,47,47,47,34,47,34,34,34,47,47,34,47,34,47,34,47,34,34,47,34,34,34,47,34,34,47,34,34,47,47,47,34,47,47,34,34,47,47,34,34,34,34,34,34,47,47,34,34,47,34,34,47,34,47,47,34,47,47,34,47,34,34,34,47,34,34,47,34,34,34,34,47,47,34,47,34,34,34,47,47,47,34,34,34,47,34,47,34,34,34,34,47,34,34,34,34,34,47,34,34,34,47,47,34,34,34,47,34,34,47,34,34,34,34,47,34,47,34,34,47,34,34,47,47,47,47,47,34,47,34,47,47,47,47,47,47,47,47,47,34,34,34,34,47,47,47,34,47,47,34,47,47,47,47,34,47,34,34,34,47,34,34,47,47,34,47,47,34,34,34,47,34,34,47,47,47,47,47,34,47,34,34,34,47,47,47,47,47,47,34,47,47,47,47,34,47,34,34,34,34,34,34,47,47,34,34,34,34,47,34,47,47,47,34,34,47,47,47,34,47,34,47,47,34,47,47,34,47,47,34,34,47,47,47,47,34,47,47,47,34,47,47,34,34,34,34,34,34,47,34,47,47,47,47,34,34,34,34,47,47,34,47,34,47,47,34,47,34,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,47,47,34,34,47,34,34,34,47,34,47,34,47,34,47,47,47,34,34,34,34,34,34,47,47,47,47,34,34,47,47,34,34,47,47,47,34,34,34,47,34,34,34,34,34,47,34,34,34,34,34,34,47,34,47,34,34,47,47,47,47,34,34,34,34,47,47,34,47,34,47,34,34,47,34,47,47,47,34,34,34,34,47,34,47,34,47,47,47,34,34,47,47,47,47,34,34,34,47,34,47,47,34,47,34,47,34,47,47,47,47,34,34,47,47,47,47,47,47,47,34,47,34,34,47,47,47,34,47,34,34,47,34,47,47,34,47,47,34,34,34,34,34,47,34,34,34,34,47,34,47,34,34,47,47,47,47,47,34,34,34,47,34,34,47,47,47,47,34,34,34,47,34,34,47,34,47,34,34,47,47,47,34,34,34,47,34,47,47,47,47,34,47,34,47,34,47,34,47,34,34,47,34,47,34,47,47,47,34,34,47,47,34,34,34,47,47,34,34,34,34,34,34,47,34,34,34,47,34,34,34,47,47,34,34,47,47,34,47,47,34,47,34,47,47,47,47,34,34,47,34,34,47,34,34,47,47,34,47,34,34,34,34,34,34,34,47,34,34,47,47,34,47,34,34,34,47,34,34,34,47,47,47,47,47,47,47,47,47,47,34,47,47,47,34,47,34,34,47,34,47,34,47,47,47,34,34,47,34,34,34,47,34,47,34,34,34,47,34,34,47,34,34,34,34,47,47,34,47,34,47,34,47,47,47,34,34,47,34,34,34,47,47,34,34,34,47,47,47,47,34,34,47,47,47,47,34,34,47,47,47,34,34,47,34,47,34,34,34,47,34,34,34,47,34,47,47,34,47,34,34,34,34,47,34,47,34,47,47,47,47,47,34,34,34,47,47,34,34,34,47,47,34,34,34,47,47,47,47,47,34,34,47,47,34,34,47,34,47,47,47,47,47,34,34,47,47,34,34,47,34,34,47,34,34,47,47,47,47,34,34,47,34,34,34,34,34,47,34,47,47,47,47,47,47,34,34,47,34,34,34,47,47,34,47,34,34,34,34,47,34,47,47,34,34,34,34,34,34,47,47,47,47,34,34,47,34,47,34,47,47,34,34,34,34,34,47,34,47,34,34,47,34,47,47,47,34,34,34,34,47,34,47,34,47,47,34,34,47,34,34,34,34,34,47,47,34,47,47,34,47,47,34,34,47,47,47,47,34,47,47,34,34,34,34,34,34,47,34,47,34,47,34,47,34,47,34,47,34,34,47,47,47,47,34,47,34,47,34,34,34,34,47,47,34,34,47,34,34,47,47,34,34,47,47,34,34,34,34,47,47,47,34,47,47,34,47,34,47,47,47,34,47,47,34,47,34,34,34,34,34,34,34,34,47,47,34,34,34,34,47,34,47,47,47,47,47,34,47,47,47,34,47,47,47,47,47,34,47,34,34,47,47,34,47,34,34,34,47,47,34,34,47,47,47,47,34,47,34,47,47,34,34,34,47,47,47,47,34,34,34,47,47,34,34,34,47,34,47,47,47,34,47,34,34,47,34,47,47,34,34,34,34,47,47,47,34,34,34,34,47,47,34,47,47,47,34,34,34,47,47,34,47,34,47,34,47,34,47,47,47,34,34,34,34,34,47,34,47,47,47,47,34,47,34,34,47,34,34,34,47,34,47,34,34,47,47,47,47,34,34,47,34,47,34,34,34,34,34,34,34,47,47,47,34,47,47,34,47,47,34,34,34,34,47,34,47,47,34,34,47,34,47,34,34,34,47,34,47,34,34,34,47,34,34,47,34,47,34,47,34,47,47,34,34,34,34,47,47,34,34,34,34,34,34,34,47,47,34,34,47,47,47,47,34,34,47,34,34,47,34,47,34,34,47,47,47,34,34,47,34,34,34,47,47,47,34,34,47,34,34,34,47,34,34,34,47,34,34,47,34,34,47,34,47,34,34,34,34,47,34,34,34,34,47,34,47,47,47,34,34,34,34,34,47,47,47,47,34,34,47,47,34,47,47,34,34,34,47,34,47,34,47,47,34,34,34,47,47,47,34,47,34,47,34,47,47,47,34,34,47,34,34,47,34,34,47,34,47,34,47,34,34,47,34,34,34,47,34,34,34,47,34,34,47,34,47,34,47,34,34,34,34,47,34,34,47,47,47,47,47,47,34,47,47,34,47,34,34,34,47,34,34,47,47,47,34,34,34,47,34,47,47,47,47,47,47,47,34,34,47,34,47,34,34,47,34,34,47,47,34,34,47,47,47,34,34,34,47,47,34,47,47,34,34,34,47,34,47,47,47,47,47,47,47,47,34,47,34,34,47,47,34,34,34,34,47,34,47,47,34,47,34,47,47,47,34,34,47,34,47,47,47,47,34,34,47,34,34,47,47,34,47,47,47,47,34,47,47,47,47,47,47,47,34,34,47,47,47,34,47,47,34,34,47,47,34,47,34,47,47,47,34,47,47,47,47,47,34,47,47,47,47,34,47,34,34,47,34,47,34,34,34,34,34,34,34,34,34,47,47,34,47,34,47,47,47,34,34,47,34,47,34,47,47,
47,47,47,34,34,34,34,34,34,47,47,47,34,34,34,47,47,34,34,47,47,34,47,34,34,47,34,34,34,47,47,34,34,34,47,47,34,47,34,47,47,34,47,34,34,34,34,47,47,47,34,47,47,47,47,47,47,47,47,47,34,47,34,47,34,47,47,34,34,34,34,34,47,47,47,34,34,47,34,47,34,47,34,34,47,34,47,47,47,34,47,34,47,34,34,34,34,47,34,47,47,34,34,34,34,47,34,47,47,47,34,47,47,34,34,47,34,34,34,47,47,47,34,47,47,34,34,34,47,34,47,34,47,47,47,34,34,47,34,34,47,34,34,34,47,34,47,47,47,47,47,47,34,34,34,47,47,47,34,47,47,47,34,47,34,34,34,34,47,47,47,47,34,34,34,34,34,47,47,34,47,34,34,47,34,34,47,34,47,47,34,47,34,34,47,34,34,34,47,47,34,47,34,34,47,47,47,34,47,34,47,47,34,34,47,47,47,47,47,47,47,34,34,47,34,34,47,47,47,47,47,47,47,34,47,47,47,34,34,47,34,47,47,34,34,34,34,47,47,34,34,34,34,34,34,34,34,34,34,47,34,47,47,34,34,34,47,47,47,34,34,34,34,47,34,47,47,34,47,47,47,34,34,34,34,34,47,34,47,47,34,34,34,47,34,34,47,47,47,47,47,34,34,47,47,34,47,34,34,47,34,47,34,47,34,47,47,34,34,34,34,34,47,34,34,34,47,47,47,34,34,47,47,47,47,34,34,34,34,47,47,47,34,34,34,47,47,34,47,34,47,34,47,47,47,47,34,34,47,47,34,34,47,34,47,47,34,47,34,47,47,47,47,34,34,47,47,34,34,47,34,47,34,34,34,47,47,47,47,34,34,47,47,47,34,47,34,34,47,47,34,34,34,47,34,34,47,47,34,47,47,34,34,47,34,47,34,47,34,47,34,47,47,34,47,47,34,47,34,34,34,34,47,47,47,34,47,47,47,47,47,34,47,34,34,47,34,47,34,34,34,34,47,47,47,47,34,47,34,34,34,34,34,47,47,34,34,47,47,34,34,34,34,47,34,34,47,47,34,47,34,47,34,34,47,47,47,47,34,47,34,34,34,34,34,34,34,34,47,47,34,47,34,47,47,47,34,47,34,47,47,34,34,34,47,34,47,34,34,34,34,47,47,34,34,34,47,34,34,34,34,34,47,34,47,47,47,47,34,34,47,47,34,34,47,47,34,47,47,47,34,34,47,34,47,34,47,34,34,47,47,47,47,34,34,34,47,34,47,34,34,47,47,47,34,47,47,47,47,47,47,34,47,47,47,47,47,34,47,34,47,34,34,34,34,47,34,47,34,34,47,34,34,34,34,47,47,47,47,47,47,47,47,34,47,34,34,47,34,47,34,47,47,47,34,47,34,47,34,34,47,47,47,47,47,47,34,34,34,47,47,47,47,34,34,47,34,34,34,34,47,34,34,34,34,34,47,47,47,47,47,47,47,47,47,47,34,47,47,34,47,47,47,34,34,34,47,47,47,47,47,34,47,47,47,47,34,34,34,47,34,34,47,47,34,47,34,34,47,47,47,34,47,47,47,34,34,34,34,34,47,47,47,47,34,47,34,47,47,34,34,34,34,34,47,34,47,34,47,34,34,47,47,47,47,47,34,34,47,47,47,34,47,34,34,47,47,47,47,34,34,34,34,34,34,47,47,34,34,34,34,34,34,47,47,34,47,47,34,34,47,34,47,34,47,34,47,47,34,34,47,47,34,47,34,47,34,47,34,34,34,34,34,34,47,47,34,34,34,47,47,34,34,34,34,47,34,34,34,47,47,34,47,34,34,34,47,47,47,34,47,34,34,47,34,34,47,47,47,47,47,34,34,34,34,47,34,47,34,47,34,34,47,34,47,34,47,34,34,47,47,47,47,34,47,47,47,47,47,47,47,34,47,47,34,47,47,47,34,47,47,47,34,34,47,47,34,47,34,47,47,34,47,47,47,47,34,47,47,47,34,34,47,47,47,34,34,34,34,47,34,47,34,47,34,47,47,34,47,47,34,34,34,47,34,34,34,47,34,34,34,47,34,47,47,34,34,34,47,34,47,47,34,34,47,34,34,47,47,34,34,34,34,47,34,47,34,47,47,34,47,34,34,47,47,47,34,47,47,34,34,47,47,47,34,34,47,34,47,47,47,47,47,34,47,47,34,47,47,47,47,47,47,47,34,34,47,47,47,47,34,34,47,47,47,47,34,47,47,34,34,34,47,34,34,34,34,34,47,34,47,34,34,47,34,47,47,34,34,34,47,34,47,34,47,34,47,34,47,34,47,47,47,34,47,47,34,34,34,34,47,34,34,47,47,34,47,34,34,47,47,34,47,47,34,34,47,34,34,34,47,34,47,47,47,34,47,34,47,47,34,47,34,47,34,47,47,47,34,47,47,47,47,47,34,34,47,47,34,34,34,47,47,47,34,47,34,47,34,47,47,47,34,47,34,47,34,47,34,34,47,47,34,34,47,47,47,34,34,34,47,34,47,34,34,34,47,34,34,47,34,47,47,34,34,34,34,47,47,47,47,47,47,34,47,34,34,47,47,47,34,47,47,47,34,34,34,34,34,47,47,47,47,34,34,47,47,47,47,47,34,34,47,34,47,47,47,34,34,34,34,47,47,34,47,34,47,34,34,34,47,34,47,47,47,34,34,34,47,47,34,34,34,34,47,47,47,47,47,34,34,47,47,34,34,34,34,47,47,47,34,34,34,34,34,34,34,34,47,34,47,34,34,34,47,47,34,34,47,34,47,47,34,34,47,47,47,34,47,34,47,34,34,34,47,47,47,47,47,34,34,34,47,47,47,34,34,34,47,34,34,47,34,34,47,47,34,34,34,34,34,47,47,47,34,47,47,47,34,34,47,34,47,34,34,34,47,34,47,47,34,47,47,47,47,47,47,47,47,47,47,34,34,47,47,47,47,34,47,47,34,47,34,34,47,47,34,47,47,34,47,34,34,34,34,47,47,34,47,34,47,34,47,47,34,47,34,47,34,47,34,47,47,34,47,47,47,47,47,47,34,47,47,34,34,34,34,47,34,47,47,47,34,34,47,34,47,34,34,47,34,34,34,34,34,34,34,47,47,47,47,47,34,34,47,47,47,47,34,34,47,34,34,34,47,47,34,47,47,34,34,47,47,34,47,34,47,34,47,47,47,47,34,34,34,47,34,47,34,34,47,47,34,47,34,34,34,34,47,47,47,34,47,47,47,47,47,47,47,34,34,34,34,34,34,34,34,47,34,34,47,34,47,34,47,34,34,47,47,47,34,47,47,34,47,47,34,47,34,34,47,34,47,34,34,47,34,34,34,34,34,47,47,47,47,47,47,47,34,34,47,47,47,34,47,47,34,47,34,34,34,47,34,34,47,34,47,47,34,47,47,47,47,47,34,34,47,34,34,34,34,47,47,47,47,34,34,34,34,34,34,47,34,34,34,47,34,47,47,34,34,34,47,34,34,34,47,34,47,34,47,34,47,47,34,47,47,34,47,47,47,47,34,34,47,47,47,34,34,47,34,34,34,47,34,34,34,47,47,34,47,47,34,34,34,34,47,47,47,47,47,47,34,34,34,47,34,34,34,34,34,47,34,34,47,34,34,34,47,47,34,47,47,47,47,34,34,47,34,34,47,47,34,47,34,34,47,34,47,34,47,34,47,34,34,34,34,34,34,47,34,34,47,47,34,34,34,47,34,34,34,34,47,34,34,47,47,47,47,34,34,34,47,34,47,34,34,47,47,34,47,47,34,47,47,34,34,34,34,47,47,47,34,34,47,47,47,34,34,47,47,34,47,34,34,34,47,47,47,34,34,34,34,34,34,47,34,47,34,34,34,34,47,47,47,34,47,47,34,47,34,47,47,34,34,47,47,47,34,47,47,34,34,34,34,34,47,34,47,34,47,47,34,34,47,47,34,47,47,34,47,47,34,47,47,47,34,47,34,47,34,34,47,47,47,34,47,34,47,47,47,47,47,47,47,34,34,34,47,47,47,34,47,47,34,47,34,47,47,47,34,47,47,34,47,47,47,47,47,34,34,47,47,34,47,47,34,47,34,34,47,34,34,34,34,34,47,34,34,47,34,34,47,34,47,47,47,34,34,34,47,34,47,34,34,47,47,34,34,34,34,34,34,34,34,47,34,47,47,34,47,34,47,34,34,34,47,34,47,34,47,47,34,47,47,47,47,47,34,34,34,47,34,34,34,47,34,47,47,34,34,34,34,34,34,34,47,47,47,34,34,47,34,34,47,47,47,47,34,47,34,47,34,47,34,47,47,47,47,47,47,47,47,47,47,47,34,47,34,34,34,47,34,34,47,47,47,34,34,47,34,34,34,34,34,47,34,47,47,34,34,34,47,47,47,47,47,47,34,47,34,34,47,47,34,47,47,34,47,34,34,34,34,34,47,34,34,47,34,34,34,34,47,34,34,34,34,47,34,47,34,34,47,47,47,47,47,34,47,34,47,34,34,34,47,34,47,47,47,34,47,34,34,47,34,34,47,47,47,34,34,34,47,34,47,47,47,34,47,47,34,34,34,34,34,34,34,34,34,47,34,47,34,34,34,34,47,47,34,47,34,34,34,47,47,47,47,47,34,34,34,47,34,47,47,47,47,34,47,34,34,34,34,47,47,34,47,34,47,47,47,34,34,34,34,34,47,47,47,47,34,34,34,47,47,47,34,47,47,47,34,47,34,34,47,47,47,34,47,34,34,34,47,34,34,47,47,47,34,34,47,34,34,34,47,47,34,34,34,47,34,47,34,34,47,34,34,34,47,47,47,34,34,34,47,47,34,47,47,34,47,34,47,47,47,34,47,47,34,34,34,47,34,34,34,34,34,34,47,47,34,34,47,34,34,34,34,34,47,34,47,34,47,34,34,47,34,47,47,34,47,34,34,47,34,34,47,47,47,34,47,34,47,47,47,47,34,34,47,47,34,34,34,34,34,47,34,47,34,34,34,47,47,34,34,47,47,34,47,34,47,34,34,47,34,34,47,34,47,34,47,34,47,47,47,34,34,34,34,34,34,47,47,34,34,34,34,34,34,34,34,34,47,34,47,47,34,47,34,47,34,34,47,47,47,34,34,47,34,47,47,34,47,34,34,34,47,34,34,34,47,47,34,34,47,34,34,34,47,34,47,34,34,34,47,47,34,34,47,34,34,34,47,47,34,34,47,34,34,47,34,47,34,47,47,34,47,47,34,34,34,47,34,47,47,47,47,47,47,34,47,34,47,34,34,34,47,47,34,34,47,34,34,47,34,34,47,34,34,34,34,47,34,34,34,34,34,47,47,47,34,47,47,47,34,34,34,34,47,34,34,47,47,34,34,34,47,34,47,47,34,47,47,34,47,34,34,34,47,34,47,47,34,47,34,34,47,47,34,34,47,34,47,47,47,47,34,47,47,34,34,47,47,47,47,47,47,47,47,47,47,47,34,47,34,47,47,47,47,47,34,47,47,34,34,34,34,34,47,34,47,47,34,34,47,34,47,34,34,47,47,34,47,47,47,47,34,47,34,47,34,34,47,47,34,34,34,34,47,47,47,47,34,34,34,47,34,34,47,47,34,47,34,47,34,47,47,34,47,47,47,34,47,34,47,34,34,47,47,47,34,47,47,47,47,47,34,47,47,47,34,34,47,47,47,47,34,34,47,34,34,47,47,34,34,47,34,47,47,34,34,47,34,47,47,47,34,34,47,47,47,34,34,47,34,34,34,47,47,47,47,47,47,34,34,47,34,34,34,34,47,34,34,47,34,47,47,34,47,34,47,47,34,47,47,34,34,47,34,47,34,47,34,47,47,34,47,47,34,47,34,47,34,47,34,34,34,47,47,47,34,34,47,34,34,47,47,47,47,47,47,47,34,34,47,34,34,34,47,34,34,34,47,34,47,34,34,34,47,34,47,47,47,47,34,47,47,34,47,47,47,34,47,34,34,34,47,34,34,34,34,34,47,34,47,47,34,47,47,47,47,34,47,47,47,47,34,47,47,47,47,34,47,47,47,47,47,34,34,34,47,34,34,47,34,47,47,34,47,47,34,34,47,34,34,47,34,47,47,34,34,34,47,47,47,47,34,34,34,47,34,47,47,34,34,47,34,34,47,34,47,47,34,47,47,34,34,34,47,47,47,34,34,47,34,47,47,34,34,47,47,34,47,47,47,47,47,47,47,34,47,47,47,34,34,34,34,47,47,34,47,34,34,47,34,34,34,47,34,34,34,47,34,34,34,47,34,34,34,47,47,34,47,47,34,47,34,47,47,34,34,34,47,34,47,34,47,47,47,34,47,47,47,47,47,34,47,34,47,47,34,34,34,47,34,34,47,47,34,34,34,34,47,47,47,47,47,34,34,47,47,34,47,34,34,34,47,34,34,34,47,34,34,34,34,34,47,47,47,34,47,34,34,34,47,34,34,47,34,47,34,47,34,47,47,34,34,47,34,47,34,34,47,47,34,47,47,34,34,47,47,34,34,34,47,34,34,47,34,47,34,34,47,47,34,34,47,47,47,34,47,47,47,47,47,34,47,34,34,47,34,34,47,47,34,47,34,34,47,34,34,47,47,34,47,34,47,34,47,47,47,47,34,34,47,47,34,47,34,47,34,34,47,34,47,47,47,47,34,34,47,47,47,47,34,47,47,47,47,34,34,47,34,47,47,47,34,34,34,34,34,34,47,47,47,34,34,47,47,47,34,34,34,34,47,34,47,34,47,34,34,34,34,47,47,47,34,47,34,47,34,34,47,47,34,34,47,47,47,34,34,34,34,47,47,47,34,34,47,47,47,47,47,47,34,34,47,47,47,47,34,34,47,34,34,34,34,34,34,47,47,47,47,34,47,34,47,34,34,47,47,47,34,34,47,47,47,34,47,34,47,34,34,47,34,34,34,34,34,34,34,34,34,34,34,47,47,47,34,34,34,47,47,34,34,34,47,47,47,34,47,34,34,34,34,34,34,34,47,34,34,47,47,47,47,34,47,34,34,47,34,34,47,34,34,47,47,47,47,47,47,47,34,34,34,34,47,34,34,34,34,47,34,47,47,34,47,34,34,47,34,47,34,47,47,47,34,34,47,47,47,47,47,47,34,47,34,34,47,34,34,47,47,47,47,47,47,34,47,34,34,34,34,47,47,34,34,47,34,34,47,47,47,34,34,47,34,34,34,34,34,47,34,47,34,47,34,34,34,47,34,34,34,34,47,47,47,47,47,34,34,47,34,34,47,34,34,34,34,47,34,34,47,47,47,47,47,34,34,47,47,34,47,34,34,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,34,34,34,34,47,47,47,34,47,34,47,34,47,47,47,34,47,47,47,47,47,34,34,34,47,34,47,34,47,47,47,34,47,34,34,47,34,34,34,47,47,47,47,34,34,47,34,47,34,47,34,34,34,34,34,34,47,47,34,34,47,34,34,47,34,34,47,34,34,47,
47,47,34,34,34,47,47,47,47,34,47,47,47,34,47,34,47,47,47,34,47,34,34,47,34,47,47,47,47,34,47,47,34,47,34,47,47,47,34,47,47,47,47,47,34,47,47,34,34,47,34,47,34,34,34,47,47,34,47,34,47,34,34,34,47,47,47,34,47,34,34,47,34,34,34,47,47,47,47,47,47,47,34,47,34,34,47,34,34,47,47,34,47,34,34,34,34,47,34,47,34,47,47,47,47,47,34,47,47,47,34,34,47,47,34,34,47,47,47,34,47,47,34,34,34,47,47,47,34,34,34,47,34,47,47,34,47,47,47,34,47,47,34,47,47,34,47,47,34,34,34,47,47,47,34,47,34,34,47,34,47,34,47,47,34,47,47,47,47,47,34,47,34,47,47,34,34,34,47,47,34,34,47,47,47,47,47,34,34,34,47,47,34,47,47,47,34,34,34,34,47,47,34,34,47,47,47,47,47,34,34,34,47,47,34,47,47,47,34,34,47,34,34,47,34,47,34,47,34,34,47,34,47,47,34,34,47,34,34,34,34,47,34,34,47,47,47,47,47,47,47,34,34,34,34,34,34,34,34,47,47,34,34,47,47,47,47,34,47,47,47,34,34,47,47,34,34,34,34,47,34,34,47,47,34,34,47,47,34,34,34,34,34,34,47,47,34,47,47,34,34,47,34,34,34,34,47,34,34,34,34,34,34,47,47,47,47,34,47,34,34,34,34,47,47,34,34,47,47,47,47,47,34,34,47,47,47,47,47,47,47,47,47,34,34,47,34,47,47,34,47,47,47,34,34,47,47,34,34,47,47,47,34,34,47,34,34,34,34,34,34,47,47,47,47,34,47,47,34,34,47,34,47,34,34,34,47,34,34,47,34,34,34,34,34,47,34,34,47,47,34,34,34,47,47,34,47,47,47,47,47,34,47,34,47,34,34,34,34,47,34,47,34,34,47,47,34,34,47,34,34,34,34,47,47,34,47,34,34,34,34,47,47,47,47,47,47,34,34,47,47,34,34,34,34,34,34,47,34,47,47,34,47,34,47,34,34,34,47,34,34,34,34,34,34,47,47,34,34,47,34,34,47,47,34,34,47,34,34,47,47,34,34,34,34,34,47,34,47,47,47,47,47,34,47,47,34,47,47,34,47,47,34,34,47,34,47,47,47,47,34,47,34,47,34,47,34,47,47,34,47,47,47,47,47,34,34,34,47,47,34,47,47,47,47,34,34,47,47,34,47,34,47,34,34,34,47,34,47,47,34,47,47,34,34,34,47,47,34,34,34,47,47,34,47,47,34,34,34,34,34,47,34,47,34,47,47,34,34,47,34,47,34,34,34,34,47,47,34,47,34,47,34,34,47,34,47,34,34,34,47,47,47,47,34,34,47,47,47,47,34,34,47,47,34,34,47,34,34,47,34,47,47,34,47,34,34,47,47,47,34,47,47,47,47,34,47,34,34,34,34,34,34,34,34,47,34,34,34,34,47,47,47,47,34,47,34,34,34,47,34,34,34,47,34,47,34,34,34,34,47,34,34,34,47,34,47,47,47,34,34,47,47,47,47,47,34,47,47,47,47,34,34,47,34,34,47,34,47,34,47,34,34,47,47,47,34,47,47,34,34,34,47,34,34,47,47,47,34,47,34,34,47,47,47,47,34,34,47,34,47,34,47,34,47,34,34,47,47,47,34,34,34,34,47,34,47,47,47,47,47,34,47,47,47,34,34,47,47,34,47,34,34,34,34,47,34,34,47,34,47,34,47,47,34,34,47,47,34,34,47,34,47,47,34,47,47,34,34,34,34,47,34,47,47,47,34,47,34,34,34,34,34,47,47,34,47,47,47,34,34,47,34,47,34,34,47,34,34,47,47,47,34,47,34,34,34,47,34,34,34,47,47,47,34,34,34,47,47,47,34,34,34,34,34,34,47,34,47,34,34,47,34,34,47,34,47,47,34,47,47,34,47,34,34,47,34,34,34,47,34,47,47,47,34,47,34,47,47,34,47,34,34,47,47,34,34,47,47,47,34,47,47,47,34,34,47,47,34,34,47,34,47,34,34,34,34,47,47,34,47,47,47,47,34,34,47,34,34,34,47,47,34,34,34,47,34,47,34,34,34,47,47,47,47,34,34,47,47,34,47,47,47,47,34,34,47,47,47,34,47,47,47,47,47,47,34,34,47,47,34,34,34,34,47,47,47,34,34,47,47,47,47,47,34,47,34,47,47,34,34,34,47,34,34,34,34,47,47,34,47,47,34,34,47,34,34,47,34,34,34,47,47,34,34,47,34,34,47,47,47,34,34,47,34,47,34,34,34,47,34,47,47,34,34,34,34,34,47,34,47,47,47,47,47,34,34,34,34,47,34,47,34,47,47,34,34,34,47,47,47,47,47,47,34,47,47,47,47,47,34,47,34,34,34,34,47,34,34,34,34,47,47,34,47,34,47,34,47,47,34,34,34,47,34,47,47,47,34,47,34,47,47,34,47,34,47,47,34,47,47,47,47,34,47,34,47,47,47,34,34,47,47,34,47,34,34,34,34,47,34,47,34,47,34,34,34,34,34,47,34,47,47,34,34,34,47,34,34,34,47,47,47,47,34,34,47,34,34,47,47,47,34,47,34,34,47,47,47,34,34,34,34,34,34,47,34,34,34,47,47,47,34,34,34,34,47,47,47,34,34,47,47,47,47,47,34,47,34,34,34,47,34,34,47,47,34,34,47,34,34,47,47,47,34,47,34,47,34,47,47,47,34,47,47,47,34,47,34,47,47,34,47,34,34,47,34,47,34,34,47,47,47,34,47,34,34,47,47,47,47,47,34,47,47,47,34,34,34,34,47,34,47,34,34,34,34,34,34,34,47,47,47,47,34,47,47,47,47,47,34,34,34,47,47,47,47,47,34,34,47,47,34,34,47,47,34,34,47,34,34,34,34,34,47,47,34,34,47,34,34,34,47,47,47,47,47,34,34,34,47,34,34,47,34,47,47,47,47,47,47,34,34,47,47,47,34,34,47,47,47,34,47,34,34,34,47,47,47,47,47,47,47,34,47,34,34,34,34,47,47,34,47,47,34,47,47,34,34,47,47,34,47,47,47,34,34,34,34,34,34,34,34,34,34,47,34,47,34,47,34,34,34,34,47,34,34,34,34,34,34,47,34,47,34,34,34,47,47,34,47,47,34,34,47,34,47,34,47,34,34,47,47,47,34,47,34,47,34,47,47,34,47,34,47,47,34,34,34,34,47,34,47,34,34,34,34,34,34,34,47,47,34,47,34,47,47,34,47,34,34,34,47,47,34,34,47,34,47,47,34,47,34,47,47,34,34,47,47,34,34,34,47,34,34,34,47,47,34,34,47,47,34,47,34,47,34,47,47,34,34,47,34,47,34,47,47,34,47,47,34,47,47,34,34,47,34,34,34,34,47,47,47,34,34,34,47,34,47,47,34,34,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,47,34,47,34,34,34,34,47,47,47,47,47,34,47,47,34,34,34,47,34,47,34,47,34,47,34,47,34,34,34,47,47,47,34,34,34,47,34,34,34,47,47,47,34,47,34,47,34,34,47,34,47,34,34,34,34,34,47,47,47,47,34,34,34,34,47,34,47,47,34,47,34,34,47,47,47,34,34,47,47,34,47,34,34,34,34,34,34,34,47,47,34,34,47,34,34,34,47,47,47,34,34,34,47,47,34,34,47,34,47,47,34,47,47,47,47,34,34,47,47,47,47,34,34,47,34,47,47,47,47,34,34,34,47,47,34,34,47,34,47,34,47,34,47,47,47,34,47,47,34,47,34,34,34,34,47,34,34,47,34,34,47,47,34,47,34,34,47,47,47,47,34,47,47,34,34,34,34,47,34,34,34,34,47,47,34,34,47,47,34,34,34,47,47,34,34,47,34,47,47,47,47,47,34,34,47,34,47,34,47,47,47,47,47,47,47,34,47,34,47,47,47,47,47,47,47,47,34,34,34,47,47,34,47,34,47,34,34,47,47,47,47,47,34,47,34,47,34,34,47,47,47,47,34,34,34,34,47,34,34,34,34,47,34,47,34,34,47,34,34,47,47,34,34,47,47,47,47,47,34,34,47,34,34,34,34,47,47,34,47,47,47,47,47,47,34,47,47,47,47,47,47,47,47,47,47,34,47,47,34,34,47,47,47,34,47,34,34,34,34,34,34,47,47,47,34,34,34,47,34,34,34,34,47,47,34,34,47,47,47,47,34,47,34,47,47,47,47,47,34,34,34,47,34,34,47,47,34,47,34,34,47,34,47,47,47,34,34,47,34,34,47,34,34,47,47,47,47,47,47,47,47,47,34,47,34,34,34,47,47,34,34,47,34,47,34,34,34,47,47,47,34,47,47,34,34,47,47,34,34,34,47,47,47,47,34,47,47,47,34,34,47,47,34,34,47,47,47,47,47,47,34,34,34,47,34,34,34,47,34,47,47,34,34,47,47,34,47,34,47,47,47,34,34,47,47,34,34,34,34,47,47,47,47,34,34,34,34,34,47,34,34,47,34,47,34,34,34,47,47,47,34,47,34,34,34,47,34,34,47,47,47,47,47,47,34,47,47,34,47,47,34,47,47,34,47,47,47,34,34,47,47,34,34,34,34,34,34,47,34,34,47,34,34,34,34,47,47,47,34,34,47,34,34,34,34,47,34,34,34,47,34,47,47,34,47,34,34,34,47,34,34,34,47,34,47,34,34,47,34,47,47,34,47,47,34,34,34,34,34,34,47,47,47,47,47,34,47,34,34,47,47,34,47,47,34,47,47,47,34,34,47,47,47,34,34,47,34,47,47,47,34,34,34,47,47,47,47,47,47,34,47,47,47,47,47,34,34,34,47,34,34,47,47,47,47,34,47,34,34,34,47,47,34,34,47,47,47,47,47,47,34,47,34,47,47,34,34,47,34,34,34,47,34,47,47,47,34,47,47,34,47,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,34,34,47,34,47,47,47,47,47,34,47,34,47,47,47,47,34,47,34,47,47,47,47,47,47,47,34,34,34,34,34,47,34,34,47,34,47,34,34,47,47,47,47,47,47,47,34,47,47,47,47,34,34,47,47,34,34,34,47,47,34,34,34,47,34,47,34,34,34,34,47,34,47,47,34,47,47,47,47,47,47,47,47,47,34,47,47,34,47,47,47,47,47,34,47,34,34,34,47,34,34,47,47,47,34,47,34,34,34,47,47,34,34,34,47,47,34,34,47,34,34,47,34,34,34,47,34,34,34,34,34,47,47,47,34,47,47,34,47,47,34,34,47,34,34,34,47,34,34,47,34,34,47,34,34,34,34,34,34,34,34,47,47,47,47,34,34,34,34,47,34,47,47,47,47,47,34,34,34,34,47,47,47,34,47,34,34,47,47,47,47,34,47,34,47,47,47,34,34,34,47,34,47,47,34,34,34,34,34,47,47,34,34,47,47,47,47,34,47,47,34,47,47,34,47,34,34,34,47,34,34,47,34,34,47,34,47,47,34,47,34,47,34,34,34,34,47,34,47,34,34,34,47,47,47,47,47,47,47,34,34,47,34,34,34,47,47,47,34,47,34,34,47,34,47,47,47,47,34,47,47,47,34,34,47,47,47,34,34,47,34,47,34,34,47,34,34,47,34,34,34,47,47,47,34,34,34,47,34,47,34,47,34,34,47,34,34,47,34,47,47,47,34,34,34,47,47,34,47,34,47,34,47,34,34,34,47,47,47,47,34,47,47,34,47,34,34,34,34,34,34,34,34,47,47,34,34,34,34,34,47,34,34,47,47,34,47,34,34,47,47,34,47,34,34,34,34,34,34,47,47,34,34,34,47,47,47,47,47,47,47,34,34,34,47,34,34,47,47,47,47,34,47,47,34,34,47,47,34,47,47,34,34,47,47,47,47,47,34,34,34,34,47,34,47,34,34,47,34,47,47,47,34,34,47,47,47,47,34,47,34,34,47,34,34,47,34,47,47,34,47,34,47,47,47,47,47,47,47,34,34,34,34,34,34,34,34,34,47,34,47,47,47,47,47,47,47,47,34,47,47,47,47,47,47,34,47,47,47,47,34,34,34,47,47,34,47,47,47,47,47,47,34,47,34,34,34,34,34,34,34,47,34,34,47,34,47,47,34,47,34,34,34,47,34,34,34,34,34,47,47,34,34,34,47,47,47,47,47,34,47,47,34,47,34,47,47,47,34,47,34,34,47,47,47,34,47,47,47,47,47,34,47,34,34,47,34,34,47,34,34,47,34,34,47,47,34,34,47,47,47,34,47,47,47,34,47,34,34,47,47,34,34,34,47,34,34,34,34,47,34,34,47,34,34,47,34,47,47,34,47,47,34,34,47,34,34,34,47,34,47,34,34,34,34,34,47,34,34,47,34,34,34,47,34,47,34,47,47,34,34,34,34,34,47,34,47,34,34,47,47,47,34,47,34,34,47,47,47,34,34,34,34,34,34,47,47,34,47,47,47,34,34,34,34,34,34,47,47,47,47,34,34,47,47,47,47,34,34,34,34,34,47,34,47,34,34,47,47,47,47,47,34,34,34,34,47,34,34,34,34,34,34,47,34,47,34,34,47,47,34,34,47,34,47,34,34,34,47,47,34,34,47,47,47,47,34,34,34,47,34,47,47,34,47,34,34,47,34,47,47,34,47,34,34,47,47,47,47,34,47,47,47,34,47,34,34,47,34,34,47,34,47,47,47,34,34,47,34,47,34,34,34,34,47,47,34,34,34,47,34,47,34,47,34,34,34,47,34,34,47,34,34,34,47,34,34,34,47,34,47,47,47,34,47,34,34,47,47,34,47,47,47,47,47,47,47,47,34,34,47,34,34,34,34,34,47,47,47,34,34,34,47,47,34,47,34,34,34,47,47,47,47,34,34,34,34,47,47,47,34,47,34,34,47,47,47,34,47,47,34,34,47,47,34,47,47,47,34,47,47,47,34,47,34,47,47,34,34,34,47,34,47,47,47,34,47,47,47,47,34,34,34,47,34,34,47,47,34,34,34,34,34,47,34,34,47,47,34,34,47,34,34,34,34,47,47,47,47,47,47,34,34,34,34,47,34,34,34,47,47,34,34,47,47,47,47,47,47,47,34,47,47,47,47,34,34,34,34,34,34,34,34,47,34,34,34,47,47,34,34,47,34,34,34,34,47,47,47,47,47,47,34,34,47,47,34,47,47,34,47,47,34,47,34,47,34,47,47,34,47,34,34,47,34,47,34,34,34,47,47,34,34,34,47,34,47,34,34,34,47,34,47,34,47,34,47,47,34,34,47,47,47,34,47,47,47,34,34,47,34,47,47,47,47,34,47,34,47,34,34,47,34,34,47,47,47,47,47,34,47,47,47,47,47,34,47,34,47,34,34,34,47,47,47,34,47,34,34,34,47,47,47,34,47,47,34,34,34,34,34,47,47,47,47,47,47,34,47,34,47,34,34,34,34,47,47,47,
47,47,34,34,47,34,47,34,34,34,34]
res = Solution()
ans = res.dailyTemperatures(temperatures)
print(ans)

