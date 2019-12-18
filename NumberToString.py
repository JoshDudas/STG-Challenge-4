class NumToStringConverter:
    def __init__(self, provided_number):
        self.number = str(provided_number)[::-1]
        self.number_length = len(self.number)
        self.num_slice = ""
        self.number_word_list = []
        self.single_to_teens_digit_words = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                                            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
                                            "seventeen", "eighteen", "nineteen"]
        self.tens_digits_words = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    def convert_number_to_string(self):
        if self.number == '0':
            print("Zero")
        else:
            # see how many times the number needs to be sliced and the conversion function called.
            # using float division instead of int so the if/else has been removed
            count = self.number_length / 3
            i = 0
            start = 0
            end = 3
            while i < count:
                self.num_slice = self.number[start:end]
                self.number_slice_to_word_conversion(i)
                start = end
                end += 3
                i += 1
            # reverse the order of the words to match the number (its checked from lowest digit to highest initially)
            self.number_word_list = self.number_word_list[::-1]
            # removes any whitespace items in the list for formatting reasons
            self.number_word_list = ' '.join(self.number_word_list).split()
            # prints out the list of words as a single string
            print(*self.number_word_list)

    def number_slice_to_word_conversion(self, i):
        # checks how long the slice is and converts the numbers based on the size of the slice (up to 3)
        if len(self.num_slice) == 1:
            self.number_word_list.append(self.single_to_teens_digit_words[int(self.num_slice)])
        elif len(self.num_slice) >= 2:
            # Checks if the 2nd number is a 1 - meaning the number will be a teen
            if self.num_slice[1] == '1':
                self.number_word_list.append(self.single_to_teens_digit_words[int("1" + self.num_slice[0])])
                # Need a second value entered in order for the additional word pattern to work (ie: thousand, million, billion)
                # otherwise the items in the list is too short and messes up the sequence of the string
                self.number_word_list.append("")
            else:
                self.number_word_list.append(self.single_to_teens_digit_words[int(self.num_slice[0])])
                self.number_word_list.append(self.tens_digits_words[int(self.num_slice[1])])

        if len(self.num_slice) == 3:
            # Similar to the teen check. If the last value in the slice is 0
            # it will insert a blank item in the list for the additional word pattern
            if self.num_slice[2] != '0':
                self.number_word_list.append(self.single_to_teens_digit_words[int(self.num_slice[2])] + " hundred")
            else:
                self.number_word_list.append("")

        # Additional word insertion based on number of items in element and how many times the number_slice_to_word_conversion function has been called
        if i == 1:
            self.number_word_list.insert(3, "thousand")
        if i == 2:
            self.number_word_list.insert(7, "million")
        if i == 3:
            self.number_word_list.insert(11, "billion")