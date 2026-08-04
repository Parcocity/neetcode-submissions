class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start = 0
        end = len(people) - 1
        boat = 0
        while(start <= end):
            if (start == end):
                boat += 1
                break
            elif (people[start] + people[end]) > limit:
                boat += 1
                end -= 1
            else:
                boat += 1
                start += 1
                end -= 1
        return boat
        