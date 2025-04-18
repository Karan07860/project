def get_minutes(hours,minutes):
    total = hours * 60 + minutes
    return total

total_minutes = get_minutes(3,14)
print(total_minutes)

print(get_minutes(5,0),"minutes")