#!/usr/bin/python3

"""
extend Python script to export data in the CSV format
"""
import requests
import sys


def export_to_csv(USER_ID):
    base_url = "https://jsonplaceholder.typicode.com/"  # the API endpoint
    response_users = requests.get(
        f"{base_url}/users"
        )  # A GET request to the API
    response_users_json = response_users.json()  # JSON decoding
    listofids = []
    for index in range(len(response_users_json)):
        for key in response_users_json[index]:
            if key == "id":
                listofids.append(
                    response_users_json[index]["id"]
                )  # creating a list of user IDs

    USER_ID = int(sys.argv[1])  # the first parameter (user id)
    if USER_ID in listofids:
        response_todos = requests.get(f"{base_url}/todos")
        response_todos_json = response_todos.json()
        for index in range(len(response_users_json)):
            if response_users_json[index]["id"] == USER_ID:
                USERNAME = response_users_json[index]["username"]
                # fetching employee names and usernames

        with open(f"{USER_ID}.csv", "w", newline="") as file:

            for index in range(len(response_todos_json)):
                if response_todos_json[index]["userId"] == USER_ID:
                    TASK_COMPLETED_STATUS = response_todos_json[index]["completed"]
                    TASK_TITLE = response_todos_json[index]["title"]
                    file.write(
                        f'"{USER_ID}","{USERNAME}",\
"{TASK_COMPLETED_STATUS}","{TASK_TITLE}"\n'
                    )  # writing rows
        file.close()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        USER_ID = int(sys.argv[1])  # the first parameter (user id)
        export_to_csv(USER_ID)
