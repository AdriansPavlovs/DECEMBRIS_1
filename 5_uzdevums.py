def greet_based_on_hour(hour):
    if 5 <= hour < 12:
        return "Labrīt!"
    elif 12 <= hour < 18:
        return "Labdien!"
    else:
        return "Labvakar!"
    