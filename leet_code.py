# leet_code.py


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :type: List[int]
        """
        count = 1
        current_location = 0
        next_number = 1
        found = False

        while found:
            if nums[current_location] + nums[next_number] == target:
                found = True
                return (nums[current_location], nums[next_number])
            else:
                current_location += 1
                next_number +=1

def test_solution():
    list = [3,2,4]
    targ = 6
    sol = Solution()
    sol.twoSum(list, targ)

    if __name__ == '__main__':
        test_solution()
