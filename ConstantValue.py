def solve(s):
    def value_of_consonants(substring):
        return sum(ord(c) - ord('a') + 1 for c in substring)

    consonant_substrings = []
    current_substring = ""

    for char in s:
        if char not in "aeiou":
            current_substring += char
        else:
            if current_substring:
                consonant_substrings.append(current_substring)
                current_substring = ""

    if current_substring:
        consonant_substrings.append(current_substring)

    max_value = 0

    for substring in consonant_substrings:
        substring_value = value_of_consonants(substring)
        if substring_value > max_value:
            max_value = substring_value

    return max_value

# Test cases
print(solve("zodiacs"))