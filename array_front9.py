#Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

#array_front9([1, 2, 9, 3, 4])
#array_front9([1, 2, 3, 4, 9])
#array_front9([1, 4, 5])

def array_front9(nums):
    l=len(nums)
    for i in range(0,3):
      if(i>=l):
          return False
      elif nums[i]==9:
          return True
    return False
    
#array_front9([1, 2, 9, 3, 4])
#array_front9([1, 2, 3, 4, 9])
#array_front9([1, 4, 5])