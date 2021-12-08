from typing import Optional


def sortsecondLargest(input: list) -> Optional[tuple]:
    '''
            params: input of  type list
            - We Ensure our input is of class List
            - We create a storage to keep the original Index O(1), this  means
                if there are copies it will return the latest secondary
                integer value from the list
            -  Iterates through the list O(n) and checks to ensure its a type
                Integer and compates whether its a max integer or secondary
            - Insert index to index_storage if its an integer
            - If  there is no integers found it will return None if no integer
            are found, otherwise it will return tuple with (index,value)
            - If there is NO second largest it will return None instead of
            largest This solutions runs a time Complexity at about
            O(n) * O(1) --  O(1) From python Dictonary lookup & retrieval
    '''
    try:
        assert isinstance(input, list)
        index_storage = dict()
        max_value = None
        second_value = None
        for index in range(len(input)):
            if isinstance(input[index], int):
                index_storage[input[index]] = index
                if max_value is None:
                    max_value = input[index]
                else:
                    if input[index] > max_value:
                        second_value = max_value
                        max_value = input[index]
                    elif second_value is None or input[index] > second_value:
                        second_value = input[index]

        if max_value == second_value:
            return (-1, -1)
        return index_storage[second_value], second_value
    except (AssertionError, KeyError):
        # In case there is no integer values or incorrect input type
        return (-1, -1)


if __name__ == "__main__":
    print(sortsecondLargest([2, 1, 4, 5, 6, 7, 8, 's', 's', 's', 'uj', 'sdd',
                            223, 'e', 1000, 'g', 2000, 'v', 'v', 'l',
                            900000000]))
    print(sortsecondLargest(['a', 'b']))
    print(sortsecondLargest(['a', 'b', 2]))
    print(sortsecondLargest(['a', 'b', 2, 3, 4, 6, 100, 80, 80, 80]))


# Example Input
    print(sortsecondLargest(['a', 'b', 1, 4, 5]))
