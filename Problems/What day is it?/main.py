offset = int(input())

reference_timepoint = 10.5

reference_dow = "Tuesday"
new_timepoint = reference_timepoint + offset

if new_timepoint >= 24:
    new_dow = "Wednesday"
elif new_timepoint < 0:
    new_dow = "Monday"
else:
    new_dow = reference_dow

print(new_dow)
