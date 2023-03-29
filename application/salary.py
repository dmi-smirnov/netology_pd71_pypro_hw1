import traceback

def calculate_salary():
  print(f'This is: {traceback.extract_stack()[-1].name}')