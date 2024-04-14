#The idea behind this solution is to use a binary search algorithm
# to find the correct partition points in the two input arrays 
#such that the left and right halves of the merged array contain roughly half of the total elements. 
#We can then calculate the median based on the maximum element on the left and the minimum element on the right.

#The time complexity of this solution is O(log(min(m, n))) since we perform a binary search on the smaller array. 
#The space complexity is O(1) since we only use a constant amount of memory to store the partition points and the maximum and minimum elements.


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        start = 0
        end = x

        while start <= end:
            partitionX = (start + end) // 2
            partitionY = ((x + y + 1) // 2) - partitionX

            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                end = partitionX - 1
            else:
                start = partitionX + 1

# Testing

array1 = [1,2]
array2 = [3,4]
Solutionclass = Solution()    
median =Solutionclass.findMedianSortedArrays(array1,array2)
print(median)
            