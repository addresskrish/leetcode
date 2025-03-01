class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def perm(values):
            if len(values) == 1:
                return [values]
            
            ans = []

            for i in range(len(values)):
                pre = [values[i]]
                suff = perm(values[:i] + values[i+1:])

                for suf in suff:
                    ans.append(pre + suf)

            return ans
           
     
        return perm(nums)