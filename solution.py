"""

This module is designed to return time slots for a given week_config.
week_config is collection of day_configs where each day_config is collection of time slots.
for each time slot in day_config, there is an output which is the combination of right date for
that day plus the time slot.

@author: Vishal Srivastava.

"""

import datetime
import pprint

target_format = '%Y-%m-%d %H:%M:%S'
target_time_format = '%H:%M'

INP_1 = [
    [  # Monday
        {"start_time": "06:00", "end_time": "06:30"},
        {"start_time": "06:30", "end_time": "07:00"},
        {"start_time": "07:00", "end_time": "07:30"},
        {"start_time": "07:30", "end_time": "08:00"}
    ], [  # Tuesday
    ], [  # Wednesday
        {"start_time": "06:00", "end_time": "06:30"},
        {"start_time": "06:30", "end_time": "07:00"},
        {"start_time": "07:00", "end_time": "07:30"},
        {"start_time": "07:30", "end_time": "08:00"}
    ], [  # Thursday
        {"start_time": "09:00", "end_time": "09:30"},
        {"start_time": "09:30", "end_time": "10:00"},
        {"start_time": "10:00", "end_time": "10:30"},
        {"start_time": "10:30", "end_time": "11:00"}
    ], [  # Friday
    ], [  # Saturday
    ], [  # Sunday
    ]
]

OUT_1 = [
    {"start_time": "2017-01-02 06:00:00", "end_time": "2017-01-02 06:30:00"},
    {"start_time": "2017-01-02 06:30:00", "end_time": "2017-01-02 07:00:00"},
    {"start_time": "2017-01-02 07:00:00", "end_time": "2017-01-02 07:30:00"},
    {"start_time": "2017-01-02 07:30:00", "end_time": "2017-01-02 08:00:00"},
    {"start_time": "2017-01-04 06:00:00", "end_time": "2017-01-04 06:30:00"},
    {"start_time": "2017-01-04 06:30:00", "end_time": "2017-01-04 07:00:00"},
    {"start_time": "2017-01-04 07:00:00", "end_time": "2017-01-04 07:30:00"},
    {"start_time": "2017-01-04 07:30:00", "end_time": "2017-01-04 08:00:00"},
    {"start_time": "2017-01-05 09:00:00", "end_time": "2017-01-05 09:30:00"},
    {"start_time": "2017-01-05 09:30:00", "end_time": "2017-01-05 10:00:00"}
]

INP_2 = [
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

OUT_2 = []

INP_3 = [
    [  # Monday
        {"start_time": "06:00", "end_time": "06:30"},
        {"start_time": "06:30", "end_time": "07:00"},
    ], [  # Tuesday
        {"start_time": "06:00", "end_time": "06:30"},
        {"start_time": "07:00", "end_time": "07:30"},
        {"start_time": "07:30", "end_time": "07:45"}
    ], [  # Wednesday
    ], [  # Thursday
        {"start_time": "09:00", "end_time": "10:00"}
    ], [  # Friday
    ], [  # Saturday
    ], [  # Sunday
    ]]

OUT_3 = [

    {"start_time": "2017-01-02 06:00:00", "end_time": "2017-01-02 06:30:00"},
    {"start_time": "2017-01-02 06:30:00", "end_time": "2017-01-02 07:00:00"},
    {"start_time": "2017-01-03 06:00:00", "end_time": "2017-01-03 06:30:00"},
    {"start_time": "2017-01-03 07:00:00", "end_time": "2017-01-03 07:30:00"},
    {"start_time": "2017-01-03 07:30:00", "end_time": "2017-01-03 07:45:00"},
    {"start_time": "2017-01-05 09:00:00", "end_time": "2017-01-05 10:00:00"},
    {"start_time": "2017-01-09 06:00:00", "end_time": "2017-01-09 06:30:00"},
    {"start_time": "2017-01-09 06:30:00", "end_time": "2017-01-09 07:00:00"},
    {"start_time": "2017-01-10 06:00:00", "end_time": "2017-01-10 06:30:00"},
    {"start_time": "2017-01-10 07:00:00", "end_time": "2017-01-10 07:30:00"}
]


INP_4 = [
    [],
    [],
    [],
    [],
    [],
    [],
    [{"start_time": "20:00", "end_time": "20:30"}]
]

OUT_4 = [{'end_time': '2017-01-08 20:30:00', 'start_time': '2017-01-08 20:00:00'},
 {'end_time': '2017-01-15 20:30:00', 'start_time': '2017-01-15 20:00:00'},
 {'end_time': '2017-01-22 20:30:00', 'start_time': '2017-01-22 20:00:00'},
 {'end_time': '2017-01-29 20:30:00', 'start_time': '2017-01-29 20:00:00'},
 {'end_time': '2017-02-05 20:30:00', 'start_time': '2017-02-05 20:00:00'},
 {'end_time': '2017-02-12 20:30:00', 'start_time': '2017-02-12 20:00:00'},
 {'end_time': '2017-02-19 20:30:00', 'start_time': '2017-02-19 20:00:00'},
 {'end_time': '2017-02-26 20:30:00', 'start_time': '2017-02-26 20:00:00'},
 {'end_time': '2017-03-05 20:30:00', 'start_time': '2017-03-05 20:00:00'},
 {'end_time': '2017-03-12 20:30:00', 'start_time': '2017-03-12 20:00:00'}]


SAMPLE_INPUT_OUTPUTS = [
    (INP_1, OUT_1),
    (INP_2, OUT_2),
    (INP_3, OUT_3),
    (INP_4, OUT_4)
]

"""Test cases are designed to run at 8:30 PM.

3 test cases are provided. All cases are not covered. Make sure you handle the cases that are not covered in the list of test cases.
Expecting more test cases to be written.
"""


def get_next_n_slots(week_config, time_of_run, n=10):
    """
    week_config: config of the week. a dict keyed by it's index.
    time_of_run: time from which the user wishes to see output.
    n: number of time slots.
    returns: Array of n slots.
    """
    assert len(week_config) == 7, 'week config length must be exactly 7'
    assert n > 0, 'output length cannot be negative'

    all_empty = True
    for day_config in week_config.values():
        if day_config:
            all_empty = False
            break
    if all_empty:  # if nothing in input, output is also NULL.
        return []

    output = []
    current_day = time_of_run.date()

    n = run_initial(week_config, time_of_run, n, output)

    while n > 0:  # as long as we have required output length.

        current_day = current_day + datetime.timedelta(days=1)  # increment the day as we are done with that day.
        current_day_index = current_day.weekday() # which day index we are talking about ?
        day_config = week_config[current_day_index] # fetch the right config
        for slot in day_config:
            output.append(generate_mono_output(current_day, slot))
            n -= 1
            if n <= 0:
                break
    return output


def run_initial(week_config, time_of_run, n, output):
    """
    week_config:  dict of week configs.
    time_of_run: the time of run
    n: desired output length.

    returns: integer denoting the remaining length of output.

    This function focuses on the day that is implied by time_of_run. We start adding
    to output from that day, if that day has any configs at all. We also search the right
    time from where we can actually start generating output since time_of_run can contain
    a time t before which there may be several times in that day config.
    """
    given_start_time = time_of_run.time()
    given_day_index = time_of_run.weekday()
    given_day = time_of_run.date()

    day_config = week_config[given_day_index]
    if not day_config:
        return n
    found_first_time_slot = False
    found_first_time_index = -1
    for index, slot in enumerate(day_config):
        if datetime.datetime.strptime(slot['start_time'], target_time_format).time() >= given_start_time:
            found_first_time_slot = True
            found_first_time_index = index
            break
    if found_first_time_slot:
        for slot in day_config[found_first_time_index:]:
            output.append(generate_mono_output(given_day, slot))
            n -= 1
            if n <= 0:  # we should not add any output if we run out of required length.
                break
    return n


def generate_mono_output(current_day, slot):
    """
    current_day: date time object.
    slot: slot dict which contains start_time and end_time
    returns: generates a single output dict which can be added to output array.
    """
    start_time_str = datetime.datetime.strptime(current_day.strftime('%Y-%m-%d') + ' ' + slot['start_time'],
                                                '%Y-%m-%d %H:%M').strftime(target_format)
    end_time_str = datetime.datetime.strptime(current_day.strftime('%Y-%m-%d') + ' ' + slot['end_time'],
                                              '%Y-%m-%d %H:%M').strftime(target_format)

    return {
        "start_time": start_time_str,
        "end_time": end_time_str
    }


if __name__ == '__main__':

    time_of_run = datetime.datetime(2017, 1, 1, 20, 30)  # Sunday

    start_time = time_of_run.time().strftime("%H:%M")
    starting_week_day = time_of_run.weekday()

    for ip, expected_output in SAMPLE_INPUT_OUTPUTS:
        ip = {index: content for index, content in enumerate(ip)} # convert week_config to a dict where key is weekday
        output = get_next_n_slots(ip, time_of_run)
        # pp = pprint.PrettyPrinter()
        # pp.pprint(output)
        assert output == expected_output

