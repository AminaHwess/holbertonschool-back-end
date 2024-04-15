#!/usr/bin/python3

"""
a Python script that,
using jsonplaceholder REST API, for a given employee ID,
returns information about his/her todo list progress.
"""
import requests
import sys


def Gather_data(arg1):
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

    if arg1 in listofids:  # check if the first parameter is a user id
        TOTAL_NUMBER_OF_TASKS = 0  # total number of tasks initialization
        NUMBER_OF_DONE_TASKS = 0  # number of done tasks initialization
        response_todos = requests.get(f"{base_url}/todos")
        response_todos_json = response_todos.json()
        for index in range(len(response_users_json)):
            if response_users_json[index]["id"] == arg1:
                EMPLOYEE_NAME = response_users_json[index][
                    "name"
                ]  # fetching employee names

        for index in range(len(response_todos_json)):
            if response_todos_json[index]["userId"] == arg1:
                TOTAL_NUMBER_OF_TASKS += 1
                if response_todos_json[index]["completed"] is True:
                    NUMBER_OF_DONE_TASKS += 1
        print(
            f"Employee {EMPLOYEE_NAME} is \
done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

        for index in range(len(response_todos_json)):
            if response_todos_json[index]["userId"] == arg1:
                if response_todos_json[index]["completed"] is True:
                    TASK_TITLE = f"\t {response_todos_json[index]['title']}"
                    print(TASK_TITLE)  # printing list of done tasks


if __name__ == "__main__":
    if len(sys.argv) == 2:
        arg1 = int(sys.argv[1])  # the first parameter (user id)
        Gather_data(arg1)
