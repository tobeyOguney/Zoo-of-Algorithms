# Solves the calendar matching problem


# O(1) time | O(1) space
def diff_in_minutes(start_time, end_time):
    hours_diff = end_time[0] - start_time[0]
    mins_diff = end_time[1] - start_time[1]

    return hours_diff*60 + mins_diff

# O(s) time | O(s) space
def get_interstices(schedule, duty_period):
    interstices = []

    if duty_period[0] < schedule[0][0]:
        interstices.append([duty_period[0], schedule[0][0]])

    for i in range(len(schedule)-1):
        if schedule[i][1] < schedule[i+1][0]:
            interstices.append([schedule[i][1], schedule[i+1][0]])
    
    if duty_period[1] > schedule[-1][1]:
        interstices.append([schedule[-1][1], duty_period[1]])
    
    return interstices

# O(sa + sb) time | O(sa + sb) space
def calendar_matching(schedule_a, duty_period_a, schedule_b, duty_period_b, min_period):
    shared_nonduty_periods = []

    interstices_a = get_interstices(schedule_a, duty_period_a)
    interstices_b = get_interstices(schedule_b, duty_period_b)

    i = 0   # Pointer to interstices_a
    j = 0   # Pointer to interstices_b
    while i < len(interstices_a) and j < len(interstices_b):
        if interstices_a[i][0] <= interstices_b[j][0] < interstices_a[i][1] or interstices_b[j][0] <= interstices_a[i][0] < interstices_b[j][1]:
            start_time = max(interstices_a[i][0], interstices_b[j][0])
            end_time = min(interstices_a[i][1], interstices_b[i][1])
            
            if diff_in_minutes(start_time, end_time) >= 30:
                shared_nonduty_periods.append([start_time, end_time])
            
            i += 1
            j += 1
        
        elif interstices_a[i][0] < interstices_b[j][0]:
            i += 1
        
        elif interstices_a[i][0] > interstices_b[j][0]:
            j += 1
    
    return shared_nonduty_periods


if __name__ == "__main__":
    res = calendar_matching(
        [
            [[9, 00], [10, 30]], [[12, 00], [13, 00]], [[16, 00], [18, 00]]
        ],
        [
            [9, 00], [20, 00]
        ],
        [
            [[10, 00], [11, 30]], [[12, 30], [14, 30]], [[14, 30], [15, 00]], [[16, 00], [17, 00]]
        ],
        [
            [10, 00], [18, 30]
        ],
        30
    )

    assert res == [[[11, 30], [12, 0]], [[15, 0], [16, 0]], [[18, 0], [18, 30]]], res

    print("You're all set!")