states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia",
                     "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia",
                     "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana",
                     "Indiana", "Mississippi", "Illinois", "Alabama",
                     "Maine", "Missouri", "Arkansas", "Michigan", "Florida",
                     "Texas", "Iowa", "Wisconsin", "California",
                     "Minnesota", "Oregon", "Kansas", "West Virginia",
                     "Nevada", "Nebraska", "Colorado", "North Dakota",
                     "South Dakota", "Montana", "Washington", "Idaho",
                     "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona",
                     "Alaska", "Hawaii"]

print(states_of_america[-1])

states_of_america[1] = "Pencilvania"

print(states_of_america)

states_of_america.append("Angelaland")  # add an item to the end of the list

# add multiple items to the end of the list
states_of_america.extend(["Renanland", "Jack Bauer Land"])

print(states_of_america)
