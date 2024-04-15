#!/usr/bin/python3

"""
extend Python script to export data in the CSV format
"""
import csv
import requests
import sys

base_url = "https://jsonplaceholder.typicode.com/"  # the API endpoint
response_users = requests.get(f"{base_url}/users")  # A GET request to the API
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
    TOTAL_NUMBER_OF_TASKS = 0  # total number of tasks initialization
    NUMBER_OF_DONE_TASKS = 0  # number of done tasks initialization
    response_todos = requests.get(f"{base_url}/todos")
    response_todos_json = response_todos.json()
    for index in range(len(response_users_json)):
        if response_users_json[index]["id"] == USER_ID:
            EMPLOYEE_NAME = response_users_json[index]["name"]
            USERNAME = response_users_json[index]["username"]
            # fetching employee names and usernames

    with open(f"{USER_ID}.csv", "w", newline="") as file:
        csvdata = csv.writer(file)  # exporting data in the csv format

        for index in range(len(response_todos_json)):
            if response_todos_json[index]["userId"] == USER_ID:
                TASK_COMPLETED_STATUS = response_todos_json[index]["completed"]
                TASK_TITLE = response_todos_json[index]["title"]
                csvdata.writerow(
                    [
                        '"{}"'.format(USER_ID),
                        '"{}"'.format(USERNAME),
                        '"{}"'.format(TASK_COMPLETED_STATUS),
                        '"{}"'.format(TASK_TITLE),
                    ]
                )  # writing rows
    file.close()
