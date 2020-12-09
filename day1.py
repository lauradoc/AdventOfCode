"""
Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

>>> find_sum([1721, 979, 366, 299, 675, 1456])
514579
"""

def find_sum(nums):

    checked_nums = []

    for i in range(len(nums)):
        temp = 2020 - nums[i]
        if temp in checked_nums:
            return nums[i] * temp
        else:
            checked_nums.append(nums[i])

"""
In your expense report, what is the product of the three entries that sum to 2020?
>>> find_sum_part2([1721, 979, 366, 299, 675, 1456])
241861950
"""

def find_sum_part2(nums):

    checked_nums = []

    for i in range(len(nums)):
        temp1 = nums[i]
        for j in nums[1:]:
            temp2 = j
            temp3 = 2020 - temp1 - temp2
            if temp3 in checked_nums:
                return temp1 * temp2 * temp3
            else:
                checked_nums.append(j)
        if temp1 not in checked_nums:
            checked_nums.append(temp1)