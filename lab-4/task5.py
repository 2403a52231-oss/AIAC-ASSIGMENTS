import re

def most_frequent_word(paragraph):
    # Convert to lowercase
    paragraph = paragraph.lower()
    # Remove punctuation and split into words
    words = re.findall(r'\b\w+\b', paragraph)
    # Count frequency
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    # Find the word(s) with the highest frequency
    max_count = max(freq.values())
    most_frequent = [word for word, count in freq.items() if count == max_count]
    # Return the first most frequent word (as per examples)
    return most_frequent[0]

# Example usage:
praragraph1 = "Hello world! Hello again"
print(most_frequent_word(praragraph1))  
paragraph2 = "python is great. Python is dynamic."
print(most_frequent_word(paragraph2))   
paragraph3 = "cats, dogs  and birds. Dogs are friendly"
print(most_frequent_word(paragraph3))   
