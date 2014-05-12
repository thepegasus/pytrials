#Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

#rotate_left3([1, 2, 3]) - [2, 3, 1]
#rotate_left3([5, 11, 9]) - [11, 9, 5]
#rotate_left3([7, 0, 0]) - [0, 0, 7]


def rotate_left3(nums):
    rotnums=[0,0,0]
    rotnums[0]=nums[1]
    rotnums[1]=nums[2]
    rotnums[2]=nums[0]
    print(str(rotnums))
  
rotate_left3([1, 2, 3])
rotate_left3([5, 11, 9])
rotate_left3([7, 0, 0])
