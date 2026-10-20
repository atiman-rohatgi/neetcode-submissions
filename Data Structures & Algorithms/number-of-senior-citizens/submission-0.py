class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            # Extract the age from indices 11 and 12
            age = int(detail[11:13])
            
            # Check if strictly strictly older than 60
            if age > 60:
                count += 1
                
        return count
        