capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# print Lille
# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

# print D
# print(nested_list[-1][1])

# Nesting a Dictionary inside a Dictionary
travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "num_times_visited": 12,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    }
}

# Print Stuttgart
print(travel_log["Germany"]["cities_visited"][2])
