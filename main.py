from datetime import datetime

from application.salary import calculate_salary
from application.db.people import get_employees

def print_func_exec_start_time(func):
  print(f'Function "{func.__name__}" execution start time: {datetime.now()}')
  func()

if __name__ == '__main__':
  print_func_exec_start_time(calculate_salary)
  print_func_exec_start_time(get_employees)