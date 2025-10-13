class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row = [1]
        sol = [row]
        for i in range(numRows-1):
            row = next_row(row)
            sol.append(row)
        return sol

        
def next_row(row: List[int]):
    toreturn = []

    for p in range(len(row)):
        sum = row[p]
        if p > 0:
            sum += row[p-1]
        toreturn.append(sum)
    toreturn.append(1)
    return toreturn