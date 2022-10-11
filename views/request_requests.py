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

