REQUESTS = [
    {
        "parentName": "Patty Patton",
        "childName": "Bratty Patton",
        "numberOfChildren": 8,
        "address": "123 Main St",
        "reservationDate": "2022-09-25",
        "reservationHours": 2,
        "id": 1
    },
    {
        "parentName": "Stanley Steamer",
        "childName": "Stacey Steamer",
        "numberOfChildren": 5,
        "address": "120 Green Dr",
        "reservationDate": "2022-09-15",
        "reservationHours": 2,
        "id": 3
    },
    {
        "parentName": "Danny Dinger",
        "childName": "Daphne Dinger",
        "numberOfChildren": 8,
        "address": "512 Huron Pl",
        "reservationDate": "2022-10-05",
        "reservationHours": 8,
        "id": 4
    }
  ]

def get_all_requests():
    return REQUESTS

def create_request(request):
    # Get the id value of the last request in the list
    max_id = REQUESTS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the request dictionary
    request["id"] = new_id

    # Add the request dictionary to the list
    REQUESTS.append(request)

    # Return the dictionary with `id` property added
    return request

def delete_request():
    # Initial -1 value for request index, in case one isn't found
    request_index = -1

    # Iterate the REQUESTS list, but use enumerate() so that you
    # can access the index value of each item
    for index, request in enumerate(REQUESTS):
        if request["id"] == id:
            # Found the customer. Store the current index.
            request_index = index

    # If the request was found, use pop(int) to remove it from list
    if request_index >= 0:
        REQUESTS.pop(request_index)


def get_single_request(id):
    # Variable to hold the found request, if it exists
    requested_request = None

    # Iterate the REQUEST list above. Very similar to the
    # for..of loops you used in JavaScript.
    for request in REQUESTS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if request["id"] == id:
            requested_request = request

    return requested_request
