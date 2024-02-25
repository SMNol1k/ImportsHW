from application.salary import *
from application.db.people import *
import datetime

def main():
    current_date = datetime.datetime.now().date()
    print(f"Current date: {current_date}")

    employees = get_employees()
    for employee in employees:
        calculate_salary(employee)

if __name__ == '__main__':
    main()