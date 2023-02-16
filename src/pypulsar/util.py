import json

"""
Helper functions to extend the functionality of our main classes.

"""


def get_status_code(function):
    def wrapper(*args, **kwargs):
        response = function(*args, **kwargs)
        if response.status_code == 200:
            final_response = json.loads(response.content)
            return final_response
        elif response.status_code == 403:
            print("Don't have admin permission")
        else:
            print(
                f"Request could not happen due to the following to error {response.status_code}")
        return {}

    return wrapper
