class Solution:

    def nextSmallerElement(self, arr, n):
        stack = [-1]
        ans = [0] * n

        for i in range(n - 1, -1, -1):
            curr = arr[i]

            while stack[-1] != -1 and arr[stack[-1]] >= curr:
                stack.pop()

            ans[i] = stack[-1]
            stack.append(i)

        return ans

    def prevSmallerElement(self, arr, n):
        stack = [-1]
        ans = [0] * n

        for i in range(n):
            curr = arr[i]

            while stack[-1] != -1 and arr[stack[-1]] >= curr:
                stack.pop()

            ans[i] = stack[-1]
            stack.append(i)

        return ans

    def largestRectangleArea(self, heights):
        n = len(heights)

        next_smaller = self.nextSmallerElement(heights, n)
        prev_smaller = self.prevSmallerElement(heights, n)

        area = float('-inf')

        for i in range(n):
            length = heights[i]

            if next_smaller[i] == -1:
                next_smaller[i] = n

            breadth = next_smaller[i] - prev_smaller[i] - 1

            new_area = length * breadth

            area = max(area, new_area)

        return area