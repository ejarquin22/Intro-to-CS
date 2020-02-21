####List-2####

def count_evens(nums):
  num = 0
  for x in nums:
    if x % 2 == 1:
      num += 0
    else:
      num += 1
  return num

def big_diff(nums):
    return max(nums) - min(nums)

def centered_average(nums):
  x = 0
  for num in nums:
    x += num
  return (x - max(nums) - min(nums)) / (len(nums)-2)

def sum13(nums):
  if len(nums)==0:
    return 0
  for num in range(0, len(nums)):
    if nums[num] == 13:
      nums[num] = 0
      if num+1 < len(nums):
        nums[num + 1] = 0
  return sum(nums)

def has22(nums):
  for num in range(0, len(nums)):
    if nums[num] == 2:
      if num + 1 < len(nums):
        if nums[num+1] == 2:
          return True
  return False

  #String-2

def double_char(str):
  result = ''
  for c in str:
    result += c*2
  return result

def count_hi(str):
  count = 0
  for x in range(0, len(str)-1):
    if str[x] == 'h' and str[x+1] == 'i':
      count += 1
  return count

def cat_dog(str):
  cat = 0
  dog = 0
  for x in range(0, len(str)-2):
    if str[x:x+3] == 'cat':
      cat += 1
    if str[x:x+3] == 'dog':
      dog += 1
  return cat == dog

def xyz_there(str):
  for x in range(len(str)):
    if str[x] != '.':
      if str[x+1:x+4] == 'xyz':
        return True
    if str[0:3] == 'xyz':
      return True
  return False

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (b.endswith(a) or a.endswith(b))

def count_code(str):
  count = 0
  for i in range(0, len(str)-3):
    if str[i:i+2] == 'co':
        if str[i+3] == 'e':
            count += 1
  return count

def sum67(nums):
  for num in range(0, len(nums)):
    if nums[num] == 6:
      nums[num] = 0
      for x in range(num+1, len(nums)):
        y = nums[x]
        nums[x] = 0
        if y == 7:
          num = x + 1
          break
  return sum(nums)
