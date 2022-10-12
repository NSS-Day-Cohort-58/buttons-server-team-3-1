CLOWNS = [
    {
      "id": 1,
      "name": "Mike"
    },
    {
      "id": 2,
      "name": "Leslie"
    }
  ]


def get_all_clowns():
    return CLOWNS


def get_single_clown(id):
    # Variable to hold the found clown, if it exists
    requested_clown = None

    # Iterate the SIZE list above. Very similar to the
    # for..of loops you used in JavaScript.
    for clown in CLOWNS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if clown["id"] == id:
            requested_clown = clown

    return requested_clown