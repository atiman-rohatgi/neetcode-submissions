class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        
        for op in operations:
            if op == "+":
                # Sum of the previous two scores
                record.append(record[-1] + record[-2])
            elif op == "D":
                # Double the previous score
                record.append(2 * record[-1])
            elif op == "C":
                # Remove the previous score
                record.pop()
            else:
                # Record a new integer score
                record.append(int(op))
                
        return sum(record)
        