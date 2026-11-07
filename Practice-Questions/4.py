def convertTime(day: int, hours: int, minutes: int) -> list[int]:

    # Validate input
    if not (1 <= day <= 31 and 0 <= hours < 24 and 0 <= minutes < 60):
        return [-1, -1, -1]

    # Add 9 hours and 30 minutes
    minutes += 30
    hours += 9

    # Adjust minutes
    if minutes >= 60:
        minutes -= 60
        hours += 1

    # Adjust day if time crosses midnight
    if hours >= 24:
        hours -= 24
        day += 1

    return [day, hours, minutes]
print(convertTime(10,10,20))