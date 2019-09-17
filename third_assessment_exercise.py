# 1. Write a function named `extract_time_components`. It should take in a string
#    that is a 24-hour time with the hour, minutes, and seconds seperated by `:`s,
#    and return a dictionary with keys `hour`, `minutes`, and `seconds` with
#    corresponding integer values.
#     ```python
#     >>> extract_time_components('21:30:00')
#     {'hours': 21, 'minutes': 30, 'seconds': 0}
#     >>> extract_time_components('09:01:53')
#     {'hours': 9, 'minutes': 1, 'seconds': 53}
#     ```

def extract_time_components(input_time):
    """
    Takes a string and breaks it up into componenets seperated by a colon. Inserts them into a dictionary.
    >>> extract_time_components('21:30:00')
    {'hours': 21, 'minutes': 30, 'seconds': 0}
    >>> extract_time_components('11:33:03')
    {'hours': 11, 'minutes': 33, 'seconds': 3}
    """

    timelist = input_time.split(":")
# the sexier way to do this
# hours, minutes, seconds = [int(i) for i in input_time.split(":")]
# timedict = {'hours': hours,
#                 'minutes': minutes,
#                 'seconds': seconds}


    timedict = {'hours': int(timelist[0]),
                'minutes': int(timelist[1]),
                'seconds': int(timelist[2])
    }
    return timedict
