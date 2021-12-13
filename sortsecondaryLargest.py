from typing import Optional


def sortnLargest(input: list, position=1) -> Optional[tuple]:
    '''
        Params: [input] list that will contain many different data types ex.int
                , String, float.
                [position] Which position to retrieve from the input data list,
                ex. position=1; [1,2,3] -> 1.


        Summary: This function will filter type int input values and return
                 the original index and value from the desired position. The
                 range is from max to min int values, ex. [10,9,8,7,6,5,4...].

        Return: (index, value) or (-1,1) if not found.
    '''
    position -= 1
    sort_list = list((index, value) for index, value in enumerate(input)
                     if isinstance(value, int))
    sort_list.sort(key=lambda enum_obj: enum_obj[1], reverse=True)
    try:
        s_index, s_value = sort_list[position][0], sort_list[position][1]
        return s_index, s_value
    except IndexError:
        return (-1, -1)


if __name__ == "__main__":
    print(sortnLargest([2, 1, 4, 5, 6, 7, 8, 's', 's', 's', 'uj', 'sdd',
                        223, 'e', 1000, 'g', 2000, 'v', 'v', 'l',
                        900000000], 2))
    print(sortnLargest(['a', 'b'], 2))
    print(sortnLargest(['a', 'b', 2], 2))
    print(sortnLargest(['a', 'b', 2, 3, 4, 6, 100, 80, 80, 80], 2))

# Example Input
    print(sortnLargest(['a', 'b', 1, 4, 5], 2))
