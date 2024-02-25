import application.salary as salary
import application.db.people as people
import datetime
from colorama import Fore, Back, Style


def main():
    current_date = datetime.datetime.now().date()
    print(f"Current date: {current_date}")
    employees = people.get_employees()
    for employee in employees:
        salary.calculate_salary(employee)
    print(Fore.RED + 'some red text')
    print(Back.GREEN + 'and with a green background')
    print(Style.DIM + 'and in dim text')
    print(Style.RESET_ALL)
    print('back to normal now')

if __name__ == '__main__':
    main()