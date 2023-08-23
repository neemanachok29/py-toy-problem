def convert_to_24_hour(hour, minute, period):
    if period == "pm":
        hour += 12
    return f"{hour:02d}{minute:02d}"
print(convert_to_24_hour(4, 30, "pm"))