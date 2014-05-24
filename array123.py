#Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere. 

#array123([1, 1, 2, 3, 1]) - True
#array123([1, 1, 2, 4, 1]) - False
#array123([1, 1, 2, 1, 2, 3]) - True


def array123(nums):
  c=0
  for i in nums:
    if(c>0 and len(nums)-1>c):
      if(nums[c-1]==1 and nums[c]==2 and nums[c+1]==3):
        return True
    c+=1
  return False
    
