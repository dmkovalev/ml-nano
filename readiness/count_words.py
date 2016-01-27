# Implement a function count_words() in Python that takes as 
# input a string s and a number n, and returns the n most 
# frequently-occuring words in s. The return value should be 
# a list of tuples - the top n words paired with their respective 
#counts [(<word>, <count>), (<word>, <count>), ...], sorted 
# in descending count order.

# You can assume that all input will be in lowercase and that 
# there will be no punctuations or other characters (only letters and
# single separating spaces). In case of a tie (equal count), order the 
# tied words alphabetically

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    words = set()
    for word in s.split():
        count = 0
        for iterat in s.split():
            if word == iterat:
                count += 1
        words.add((word, count))
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    top_n = sorted(list(words), key=lambda x: (-x[1], x[0]))
    
    return top_n[:n]


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()