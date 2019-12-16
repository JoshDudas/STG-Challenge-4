class NumToStringConverter:
    def __init__(self, provided_number):
        self.number = str(provided_number) [::-1]
        self.number_length = len(self.number)
        self.number_word_list = []
        self.number_string = ""
        self.single_to_teens_digit_words = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                                            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
                                            "seventeen", "eighteen", "nineteen"]
        self.tens_digits_words = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        self.hundred = "hundred"
        self.thousand = "thousand"
        self.million = "million"

    def millions_conversion(self):
            self.number_word_list.append(self.single_to_teens_digit_words[int(self.number[6])] + " " + self.million)
            self.hundred_thousands_conversion()

    def hundred_thousands_conversion(self):
        if self.number[5] != '0':
            self.number_word_list.append(self.single_to_teens_digit_words[int(self.number[5])] + " " + self.hundred)
        self.ten_thousands_conversion()

    def ten_thousands_conversion(self):
        if self.number[4] != '0':
            if self.number[4] == '1':
                self.number_word_list.append(self.single_to_teens_digit_words[int(str("1" + self.number[3]))] + " " + self.thousand)
            else:
                self.number_word_list.append(self.tens_digits_words[int(self.number[4])] + " " + self.single_to_teens_digit_words[int(self.number[3])] + " " + self.thousand)
        self.hundreds_conversion()

    def thousands_conversion(self):
        self.number_word_list.append(self.single_to_teens_digit_words[int(self.number[3])] + " " + self.thousand)
        self.hundreds_conversion()
        return

    def hundreds_conversion(self):
        if self.number[2] != '0':
            self.number_word_list.append(self.single_to_teens_digit_words[int(str(self.number[2]))] + " " + self.hundred)
        self.tens_teens_conversion()
        return

    def tens_teens_conversion(self):
        if self.number[1] == '1':
            self.number_word_list.append(self.single_to_teens_digit_words[int(str("1" + self.number[0]))])
        else:
            self.number_word_list.append(self.tens_digits_words[int(self.number[1])])
            self.number_word_list.append(self.single_to_teens_digit_words[int(self.number[0])])
        return

    def single_conversion(self):
        self.number_word_list.append(self.single_to_teens_digit_words[int(self.number)])
        return

    def create_string_from_number(self):
        for item in self.number_word_list:
            self.number_string += item + " "
        return

    def convert_number_to_string(self):
        if self.number_length <= 7:
            if self.number == '0':
                print("Zero")
            if self.number_length == 1:
                self.single_conversion()
            if self.number_length == 2:
                self.tens_teens_conversion()
            if self.number_length == 3:
                self.hundreds_conversion()
            if self.number_length == 4:
                self.thousands_conversion()
            if self.number_length == 5:
                self.ten_thousands_conversion()
            if self.number_length == 6:
                self.hundred_thousands_conversion()
            if self.number_length == 7:
                self.millions_conversion()
            self.create_string_from_number()
            print(self.number_string)
        else:
            print("Number too large. Must be under 10 million")