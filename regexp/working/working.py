import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # pattern = r'(\d{1,2}):?(\d{0,2})? (AM|PM) to (\d{1,2}):?(\d{0,2})?'
    pattern_match = re.match(r'(\d{1,2}):?(\d{0,2})? (AM|PM) to (\d{1,2}):?(\d{0,2})? (AM|PM)', s)
    if not pattern_match:
        raise ValueError()
    
    start_hour = int(pattern_match.group(1))
    start_min = int(pattern_match.group(2)) if pattern_match.group(2) else 0
    start_period = (pattern_match.group(3))
    
    end_hour = int(pattern_match.group(4))
    end_min = int(pattern_match.group(5)) if pattern_match.group(5) else 0
    end_period = (pattern_match.group(6))

    if not (0<= start_min < 60) or not (0 <= end_min <= 60):
        raise ValueError()


    start_time_24_hr = convert_to_24(start_hour,start_min,start_period)
    end_time_24_hr = convert_to_24(end_hour,end_min,end_period)

    return f"{start_time_24_hr} to {end_time_24_hr}"
    # return start_hour

def convert_to_24(hour,minute,period):
    if period == "PM" and hour != 12:
        hour +=12
    elif period == "AM" and hour == 12:
        hour = 0
    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
