#!/usr/bin/python3
"""
Script that exports a given employee TODO list data to a JSON file
"""
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(base_url)).json()
    todos = requests.get("{}/todos".format(base_url)).json()

    usernames = {}
    for user in users:
        usernames[user.get("id")] = user.get("username")

    result = {}
    for task in todos:
        user_id = task.get("user_Id")
        entry = {}
        entry["username"] = usernames.get(user_id)
        entry["task"] = task.get("title")
        entry["completed"] = task.get("completed")
        result.setdefault(str(user_id), []).append(entry)

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(result, json_file)
