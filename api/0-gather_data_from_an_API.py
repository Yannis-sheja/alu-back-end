#!/usr/bin/python3

import requests
import sys

if __name__ == "main":
    employee_id = sys.argv[1]
    base = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base, employee_id)).json()

    todos = requests.get("{}/todos".format(base), param={"userId": employee_id}).json()

    tasks_done = [task for task in todos if task.get("Completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(tasks_done), len(todos)))

    for task in tasks_done:
        print("\t {}".format(task.get("title")))

