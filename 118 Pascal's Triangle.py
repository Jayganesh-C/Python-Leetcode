class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        # Recursive solution
        if(numRows == 0):
            return []
        if(numRows==1):
            return [[1]]
        
        prevRows = self.generate(numRows-1)
        newRows = [1] * numRows

        for i in range(1, numRows-1):
            newRows[i] = prevRows[-1][i-1] + prevRows[-1][i] 
        
        prevRows.append(newRows)

        return prevRows
        
        # Using Dynamic Programming with 1D Array Saves Space
        # if numRows == 0:
        #     return []
        # if numRows == 1:
        #     return [[1]]

        # prev_rows = self.generate(numRows - 1)
        # prev_row = prev_rows[-1]
        # current_row = [1]

        # for i in range(1, numRows - 1):
        #     current_row.append(prev_row[i - 1] + prev_row[i])

        # current_row.append(1)
        # prev_rows.append(current_row)

        # return prev_rows