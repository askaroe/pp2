def findCombination(nums: list):
  res = ""
  for i in nums:
    if i == 0 or i == 7:
      res+=str(i)

  return True if res.find("007") >=0 else False