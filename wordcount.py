# put your code here.


# Create a function

def word_count(file):
    """
    Docstring goes here
    """

# Create an empty dicitonary

    words_count = {}

# Open the file

    open_file = open(file, 'r')
    for line in open_file:
        words = line.rstrip().split(' ')
        # words = words.split(' ')
        for word in words:
            words_count[word] = words_count.get(word, 0) + 1
    
    for k, v in words_count.items():
        print(k,v)

    # words_count.items()


# Loop through the lines
# Split the lines in to a list of words usign rstrip .split
# Loop over the list of words
# Use the .get (notes from lecture)
# Return the list (Dictionary, or list of tuples? In lectue notes).


# Close the files

print("\n Test Text:\n")
word_count('test.txt')
print("\n Twain Text:\n")
word_count('twain.txt')