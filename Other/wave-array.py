# Wave Array from CTI-ISP 2020 #

# Given an array of integers, sort the array into a wave like array and return it, 
# In other words, arrange the elements into a sequence such that a[1] >= a[2] <= a[3] >= a[4] <= a[5] ...

def swap(lst, index1, index2):
  lst[index1], lst[index2] = lst[index2], lst[index1]

def wave_array(integers):
  for index in range(0, len(integers)-1, 2):
    if integers[index] < integers[index+1]:
      swap(integers, index, index+1)
    
  for index in range(1, len(integers)-1, 2):
    if integers[index] > integers[index+1]:
      swap(integers, index, index+1)
  return integers

if __name__ == '__main__':
    integers = [1, 2, 3, 4, 5]
    wave_array(integers)
    print(integers, [2, 1, 4, 3, 5])
