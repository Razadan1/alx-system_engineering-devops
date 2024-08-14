#!/usr/bin/python3
import sys
import requests

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    
    user = requests.get(base_url + f"users/{employee_id}").json()
    employee_name = user.get("name")
    to_do = requests.get(base_url + f"to_do?userId={employee_id}").json()
    completedTasks = [task for task in to_do if task.get("completed")]
    totalTasks = len(to_do)
    doneTasks = len(completedTasks)
    
    print(f"Employee {employee_name} is done with tasks({doneTasks}/{totalTasks}):")
    for task in completedTasks:
        print(f"\t {task.get('title')}")
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
        
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)