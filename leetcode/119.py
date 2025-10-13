class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            row = next_row(row)
        return row

def next_row(row: List[int]):
    toreturn = []

    for p in range(len(row)):
        sum = row[p]
        if p > 0:
            sum += row[p-1]
        toreturn.append(sum)
    toreturn.append(1)
    return toreturn