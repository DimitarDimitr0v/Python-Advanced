def forecast(*args):
    locations = {}
    for location, weather in args:
        if weather not in locations:
            locations[weather] = []
        locations[weather].append(location)
    result = []
    for weather in ["Sunny", "Cloudy", "Rainy"]:
        if weather in locations:
            sorted_locations = sorted(locations[weather])
            for location in sorted_locations:
                result.append(f"{location} - {weather}")
    return "\n".join(result)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
