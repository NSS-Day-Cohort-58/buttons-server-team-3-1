

















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