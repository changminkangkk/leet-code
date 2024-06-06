class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # converting the string to lower case
        string = s.lower()
        #computing the length
        n = int(len(string))
        # computing the half length
        half = int((n/2))
        # two vairbales to maintain count for each half's
        count1 = 0
        count2 = 0
        # loop for first half
        for i in string[:half]:
            if i in {'a','e','i','o','u'} :
                count1 = count1 + 1

        # loop fo rsecond half
        for j in string[half:n+1]:
            if j in {'a','e','i','o','u'}:
                count2 = count2 + 1
        # to check both the counts
        if count1 == count2:
            return True
        else:
            return False