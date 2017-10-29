class StringImplementer:

    """
    gets the main string and return the string that is between two strings : first_string and end_string!
    """
    @staticmethod
    def string_cutter(main_string, first_string, end_string):
        first_state = 0
        end_state = 0
        state = 0

        # first_index = 0
        # last_index = 0

        for i in range(0, len(main_string)):
            if state == 0:
                if main_string[i] == first_string[first_state]:
                    first_state += 1
                    if first_state == len(first_string):
                        state = 1
                        start_index = i+1
                else:
                    first_state = 0
            elif state == 1:
                if main_string[i] == end_string[end_state]:
                    end_state += 1
                    if end_state == len(end_string):
                        state = 2
                        end_index = i
                else:
                    first_state = 0

        if state == 2:
            try:
                end_index -= (len(end_string)-1)
                desired_str = main_string[start_index:end_index]
                return desired_str
            except Exception as e:
                print("failed to cut string!")
                return None

        else:
            print("failed to cut string!")
            return None

    @staticmethod
    def third_tokenize(string):
        """
        2,777,123
        len => 7
        index => [1,5]
        [0,1],[1,5],[5,len(str)]

        123,123,123
        len => 9
        index => [3,7]

        12,131,513,512
        len=>11
        index => [2,6,10]
        """
        length = len(string)

        index = length % 3
        if index == 0:
            index = 3
        index_list = [0]
        while index < length:
            index_list.append(index)
            index += 3

        index_list.append(length)

        new_string = ""
        for i in range(0, len(index_list)-1):
            new_string = new_string + string[index_list[i]:index_list[i+1]] + ","

        new_string = new_string[:-1]
        return new_string

