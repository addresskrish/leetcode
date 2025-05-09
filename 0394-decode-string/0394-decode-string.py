class Solution:
    def decodeString(self, s: str) -> str:
        length = len(s)
        index = 0
        result = ""
        pending_string = ""

        while index < length:
            if s[index].isdigit():
                count_str = ""
                # Extract the complete number
                while index < length and s[index].isdigit():
                    count_str += s[index]
                    index += 1
                repeat_count = int(count_str)

                # Skip the opening bracket '['
                index += 1
                open_brackets = 1
                close_brackets = 0
                encoded_part = ""

                # Find the substring within matching brackets
                while index < length and open_brackets != close_brackets:
                    if s[index] == '[':
                        open_brackets += 1
                    elif s[index] == ']':
                        close_brackets += 1
                    encoded_part += s[index]
                    index += 1

                # Recursively decode the substring (excluding the last ']')
                decoded_substring = self.decodeString(encoded_part[:-1])
                result += pending_string + repeat_count * decoded_substring
                pending_string = ""
            else:
                pending_string += s[index]
                index += 1

        return result + pending_string