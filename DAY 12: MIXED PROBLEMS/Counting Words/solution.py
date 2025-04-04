def longest_sentence_length(paragraph):
    # Split the paragraph into sentences based on '.' and ','
    sentences = paragraph.replace('.', ',').split(',')
    
    # Initialize the max length to 0
    max_length = 0
    
    # Iterate through each sentence
    for sentence in sentences:
      
        # Strip any leading/trailing whitespace and split into words
        words = sentence.strip().split()
      
        # Update max_length if this sentence is longer
        max_length = max(max_length, len(words))

    # Return the length of the longest sentence
    return max_length

# Input
paragraph = input().strip()

# Output
print(longest_sentence_length(paragraph))
