class Solution:

    def encode(self, strs: List[str]) -> str:

        if strs == []:
            return "258"

        result = ""
        for index, word in enumerate(strs):
            for letter in word:
                letter_ascii = ord(letter)
                if letter_ascii < 100:
                    result = result + "0" + str(letter_ascii)
                else:
                    result += str(letter_ascii) 
            if index != len(strs)-1:
                result += "257"
        return result

    def decode(self, s: str) -> List[str]:

        result = []
        current_word = ""
        char = ""
        position = 0
        count = 0

        if s == "258":
            return []        
        
        while position < len(s):
            char += s[position]
            position += 1
            count += 1

            if count == 3:
                count = 0
                if char != "257":
                    current_word += str(chr(int(char)))
                else : 
                    result.append(current_word)
                    current_word = ""
                char = ""

        result.append(current_word)
        return result
