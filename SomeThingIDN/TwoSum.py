'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].'''

class  Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for i in xrange(0,len(nums)):

                dic[nums[i]]=i
        try:

            item=dic[nums[i]]
            item2=dic[target-nums[i]]
            if item>item2 and dic[item2] !=dic[item]:
                l=[item2,item]
            elif item<item2 and dic[item2] !=dic[item]:
                l=[item,item2]
            return l

        except:
            pass
    def Twosum(self,nums,target):
        lookup = dict(((v, i) for i, v in enumerate(nums)))
        return next(((i , lookup.get(target - v))
                     for i, v in enumerate(nums)
                     if lookup.get(target - v, i) != i), None)
    # def twosum(self,nums,target):
    #     lookup=dict((v,i)for i,v in enumerate(nums))
    #     for i, v in lookup:
    #         if lookup.get(target-v,i) !=i


if __name__=='__main__':
    a=Solution()
    print a.twoSum([1,3,4],7)