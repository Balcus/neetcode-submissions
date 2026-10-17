class Solution:
    def compress(self, chars: list[str]) -> int:
        '''
        2 pointes:
        - w: write pointer, remember where to write in the given string
        - r: read pointer, used to explore the array
        '''
        w, r = 0, 0
        while r < len(chars):
            # Take the character that read points to
            c = chars[r]
            count = 0

            # Count how many times the same character is repeated
            while r < len(chars) and c == chars[r]:
                r += 1
                count += 1
            
            # Write the character at write index
            chars[w] = c
            w += 1
            # If the count of the character is > 1 then write it as well at the write index
            if count > 1:
                for digit in str(count):
                    chars[w] = digit
                    w += 1
        
        return w