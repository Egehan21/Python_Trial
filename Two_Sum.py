def solution(nums, target):

    lst = []
    lenght = len(nums)

    for i in range(lenght):
        for j in range(i+1, lenght):
            if nums[i]+nums[j]==target:
                lst.append(i)
                lst.append(j)
                return lst
    

nums=[1,3,6,2,9,41,33,5]
print(solution(nums,8))




