class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        s_length = len(s)

        arr = [""] * len(s)

        arr_pos = 0

        if numRows == 1:
            return s

        for i in range(0, s_length, 2 * numRows - 2):
            arr[arr_pos] = s[i]
            arr_pos += 1

        for row in range(1, numRows-1):
            for i in range(row, s_length, 2 * numRows - 2):
                arr[arr_pos] = s[i]
                arr_pos += 1
                if (i + 2*numRows-2-2*row < s_length):
                    arr[arr_pos] = s[i + 2*numRows-2-2*row]
                    arr_pos += 1

        for i in range(numRows - 1, s_length, 2 * numRows - 2):
            arr[arr_pos] = s[i]
            arr_pos += 1

        return "".join(arr)




print(Solution().convert("PAYPALISHIRING", 4))
        

