COMPLETIONS = [
    {
      "CompletedReservationId": 1,
      "clownId": 2,
      "date_created": "2022-09-26",
      "id": 1
    },
    {
      "CompletedReservationId": 2,
      "clownId": 1,
      "date_created": "2022-09-17",
      "id": 2
    },
    {
      "CompletedReservationId": 3,
      "clownId": 2,
      "date_created": "2022-10-06",
      "id": 3
    }
  ]


def get_all_completions():
    return COMPLETIONS

def create_completion(completion):
    # Get the id value of the last completion in the list
    max_id = COMPLETIONS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the completions dictionary
    completion["id"] = new_id

    # Add the completion dictionary to the list
    COMPLETIONS.append(completion)

    # Return the dictionary with `id` property added
    return completion


def get_single_completion(id):
    # Variable to hold the found completion, if it exists
    requested_completion = None

    # Iterate the COMPLETION list above. Very similar to the
    # for..of loops you used in JavaScript.
    for completion in COMPLETIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if completion["id"] == id:
            requested_completion = completion

    return requested_completion