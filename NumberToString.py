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
            if self.number_length % 3 > 0:
                count = self.number_length // 3 + 1
            else:
                count = self.number_length // 3
            i = 0
            start = 0
            end = 3
            while i < count:
                self.num_slice = self.number[start:end]
                self.number_to_word_conversion(i)
                start = end
                end += 3
                i += 1
            self.number_word_list = self.number_word_list[::-1]
            self.number_word_list = ' '.join(self.number_word_list).split()
            print(*self.number_word_list)

    def number_to_word_conversion(self, i):
        if len(self.num_slice) == 1:
            self.number_word_list.append(self.single_to_teens_digit_words[int(self.num_slice)])
        elif len(self.num_slice) >= 2:
            if self.num_slice[1] == '1':
                self.number_word_list.append(self.single_to_teens_digit_words[int("1" + self.num_slice[0])])
                self.number_word_list.append("")
            else:
                self.number_word_list.append(self.single_to_teens_digit_words[int(self.num_slice[0])])
                self.number_word_list.append(self.tens_digits_words[int(self.num_slice[1])])
        if len(self.num_slice) == 3:
            if self.num_slice[2] != '0':
                self.number_word_list.append(self.single_to_teens_digit_words[int(self.num_slice[2])] + " hundred")
            else:
                self.number_word_list.append("")
        if i == 1:
            self.number_word_list.insert(3, "thousand")
        if i == 2:
            self.number_word_list.insert(7, "million")
        if i == 3:
            self.number_word_list.insert(11, "billion")