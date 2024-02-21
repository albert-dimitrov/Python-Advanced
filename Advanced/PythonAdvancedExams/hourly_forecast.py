def forecast(*args):
    weather_info = {}
    result = ''

    charts = {
        'Sunny': 1,
        'Cloudy': 2,
        'Rainy': 3,
    }

    for city, weather in args:
        weather_info[city] = [weather, charts[weather]]

    sorted_weather = sorted(weather_info.items(), key=lambda x: (x[1][1], x[0]))

    for location, weather in sorted_weather:
        result += f"{location} - {weather[0]}\n"

    return result

