"""

This module is designed to return time slots for a given week_config.
week_config is collection of day_configs where each day_config is collection of time slots.
for each time slot in day_config, there is an output which is the combination of right date for
that day plus the time slot.

@author: Vishal Srivastava.

"""

import datetime
import pprint

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
    [{"start_time": "09:00", "end_time": "09:30"}],
    [],
    [],
    [],
    []
]

SAMPLE_INPUT_OUTPUTS = [
    (INP_1, OUT_1),
    (INP_2, OUT_2),
    (INP_3, OUT_3),
]

"""Test cases are designed to run at 8:30 PM.

3 test cases are provided. All cases are not covered. Make sure you handle the cases that are not covered in the list of test cases.
Expecting more test cases to be written.
"""


def get_next_n_slots(week_config, time_of_run, n=10):
    """
    week_config: config of the week.
    time_of_run: time from which the user wishes to see output.
    n: number of time slots.
    returns: Array of n slots.
    """
    assert len(week_config) == 7, 'week config length must be exactly 7'
    assert n > 0, 'output length cannot be negative'

    all_empty = True
    for day_config in week_config:
        if day_config:
            all_empty = False
            break
    if all_empty:  # if nothing in input, output is also NULL.
        return []

    output = []
    current_day = get_monday(time_of_run)  # we always start from monday no matter what is the given date.
    target_format = '%Y-%m-%d %H:%M:%S'

    while n > 0:  # as long as we have required output length.
        for day, day_config in enumerate(week_config):  # for all day_configs in week_configs.
            for slot in day_config:  # for all slots in day_configs.

                if n <= 0:  # we should not add any output if we run out of required length.
                    break
                start_time_str = datetime.datetime.strptime(current_day.strftime('%Y-%m-%d') + ' ' + slot['start_time'],
                                                            '%Y-%m-%d %H:%M').strftime(target_format)
                end_time_str = datetime.datetime.strptime(current_day.strftime('%Y-%m-%d') + ' ' + slot['end_time'],
                                                          '%Y-%m-%d %H:%M').strftime(target_format)
                output.append(
                    {
                        "start_time": start_time_str,
                        "end_time": end_time_str
                    })
                n -= 1
            current_day = current_day + datetime.timedelta(days=1)
    return output


def next_weekday(d, weekday):
    """
    d: given date
    weekday: integer which represents number of days after the given date.
    returns:  from the given date, returns the date 'weekday' after.
    """
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


def get_monday(time_of_run):
    """
    time_of_run: datetime object.
    returns:  the next monday from time_of_run.
    """
    d = time_of_run.date()
    return next_weekday(d, 0)  # 0 = Monday, 1=Tuesday, 2=Wednesday...


if __name__ == '__main__':

    time_of_run = datetime.datetime(2017, 1, 1, 20, 30)  # Sunday

    for ip, expected_output in SAMPLE_INPUT_OUTPUTS:
        output = get_next_n_slots(ip, time_of_run)
        # pp = pprint.PrettyPrinter()
        # pp.pprint(output)
        assert output == expected_output

