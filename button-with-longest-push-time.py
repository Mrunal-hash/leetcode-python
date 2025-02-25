class Solution:
    def buttonWithLongestTime(self, events: list[list[int]]) -> int:
        
        events = sorted(events, key=lambda x:x[1])
        x = [events[0][1]]

        for i in range(len(events)-1):
            x.append(events[i+1][1]-events[i][1])

        res = [i for i, j in enumerate(x) if j == max(x)] 
        result = []
        
        for i in range(len(res)):
            result.append(events[res[i]][0])
        return min(result)

a = Solution()
print(a.buttonWithLongestTime([[1,2],[2,5],[3,9],[1,13]]))
b = Solution()
print(b.buttonWithLongestTime([[10,2],[1,3]]))

