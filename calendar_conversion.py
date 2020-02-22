dayConversions = {
    "Mon": "Monday",
    "Tue": "Tuesday",
    "Wed": "Wednesday",
    "Thu": "Thursday",
    "Fri": "Friday",
    "Sat": "Saturday",
    "Sun": "Sunday",
}

print(dayConversions["Fri"])
print(dayConversions.get("Sun"))
print(dayConversions.get("XXX", "Ivalid day"))
