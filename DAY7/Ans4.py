def reverse_words(s):
    # Split the sentence into individual words using whitespace as the delimiter
    words = s.split()

    # Reverse each word in the list
    reversed_words = [word[::-1] for word in words]

    # Join the reversed words back into a sentence with the original whitespace
    result = " ".join(reversed_words)

    return result

# Example usage:
s = "Let's take LeetCode contest"
print(reverse_words(s))  # Output: "s'teL ekat edoCteeL tsetnoc"
