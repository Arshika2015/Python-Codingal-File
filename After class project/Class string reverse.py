class StringReverser:
    def reverse_words(self, input_string):
        """
        Reverses the order of words in a given string.

        Args:
            input_string (str): The string to be reversed word by word.

        Returns:
            str: The string with words reversed.
        """
        words = input_string.split()  # Split the string into a list of words
        reversed_words = reversed(words)  # Reverse the order of words in the list
        return ' '.join(reversed_words)  # Join the reversed words back into a string with spaces
reverser = StringReverser()
my_string = "This is a sample string"
reversed_result = reverser.reverse_words(my_string)
print(reversed_result)

