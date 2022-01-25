class Solution:
    def longestDecomposition(self, text: str) -> int:
        i = 0
        j = len(text) - 1
        count = 0
        front_string = ""
        back_string = ""
        while i < j :
            front_string += text[i]
            back_string = text[j] + back_string
            if front_string == back_string :
                count += 2
                front_string = ""
                back_string = ""
            i += 1
            j -= 1
        if(i == j or len(front_string) > 0):
            return count + 1
        return count