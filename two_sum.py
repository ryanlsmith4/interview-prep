def two_sum_b(nums: list, total: int) -> [int]:

  for num in nums:
    for num2 in nums:
      if num + num2 == total:
        return [num, num2]
      else:
        continue
  raise ValueError('No two Sum')
      

def two_sum(nums: list, total: int) -> [int]:
  previous_dict = {}

  for num in nums:

    compliment = total - num
    if compliment in previous_dict.keys():
      print('here')
      return [compliment, num]

    previous_dict[compliment] = num     

    
  return previous_dict

if __name__ == "__main__":

  # print(two_sum([1, 2, 3], 4)) # [1, 3]

  print(two_sum([1, 2, 3], 4)) # [1, 3]
  print(two_sum([3, 9, 12, 20], 21)) # [9, 12]
