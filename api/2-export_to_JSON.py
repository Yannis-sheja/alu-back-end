#!/usr/bin/python3
"""
Script that exports a given employee TODO list data to a CSV file
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get("{}/users/{}".format(base_url,
                                                      employee_id))
    todos_response = requests.get("{}/todos?userId={}".format(base_url,
                                                              employee_id))

    if (user_response.status_code != 200 or
            todos_response.status_code != 200):
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    username = user_data.get("username")

    tasks = []
    for task in todos_data:
        entry = {}
        entry["task"] = task.get("title")
        entry["completed"] = task.get("completed")
        entry["username"] = username
        tasks.append(entry)

    filename = "{}.json".format(employee_id)
    with open(filename, "w") as json_file:
        json.dump({str(employee_id): tasks}, json_file)
