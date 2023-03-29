import traceback

def get_employees():
  print(f'This is: {traceback.extract_stack()[-1].name}')