# PERSON = ('ticket_number', 'first_name', 'last_name', POSITION[HR], SALARIES[HR_SALARY])
import random
from decimal import Decimal
from faker import Faker
fake = Faker()


DEVELOPER = 'DEV'
CEO = 'CEO'
HR = 'HR'

POSITION = {
    DEVELOPER: 1,
    CEO: 2,
    HR: 3,
}


DEV_SALARY = '1000-4000'
CEO_SALARY = '3000-18000'
HR_SALARY = '500-5000'

SALARIES = {
    DEV_SALARY: 1,
    CEO_SALARY: 2,
    HR_SALARY: 3,
}

DEV_SKILLS = "DEV_SKILLS"
CEO_SKILLS = "CEO_SKILLS"
HR_SKILLS = "HR_SKILLS"

SKILLS = {
    DEV_SKILLS: ["PHP", "Python", "Ruby", "HTML", "CSS"],
    CEO_SKILLS: ["Social Media", "Link Building", "Usability", "Content Marketing"],
    HR_SKILLS: ["Teamwork", "Coaching", "Communication", "Advising"],
}


def filter_employers_by_position(employers_in: list, position: int) -> list:
    return [employer for employer in employers_in if employer[3] == position]


def filter_employers_by_skills(employers_in: list, skill: str) -> list:
    filter_employer = list()
    for employer in employers_in:
        for skills in employer[-1]:
            if skills == skill:
                filter_employer.append(employer)
    return filter_employer


def salary_to_number_value(salary: int) -> Decimal:
    salaries_inner = {v: k for k, v in SALARIES.items()}
    salary_name = salaries_inner.get(salary, SALARIES[HR_SALARY])
    salary_range = tuple(map(int, salary_name.split('-')))
    return Decimal(salary_range[0] + salary_range[1]) / 2


def get_average_salary(employers_in: list):
    all_salaries = [salary_to_number_value(employer[-2]) for employer in employers_in]
    return sum(all_salaries) / len(all_salaries)


def hire_person(position):
    ticket_number = random.randint(1000, 9999)
    fake_name = fake.name().split()
    position_name = POSITION.get(position, 'HR')
    salary_name = eval(f'{position}_SALARY')
    salary = SALARIES.get(salary_name)
    # Расширяем структуру новыми данными, добавляем навыки
    skills_name = eval(f'{position}_SKILLS')
    # Рандомно выбираем навыки из словаря
    skills = random.sample(SKILLS[skills_name], random.randint(1, len(SKILLS[skills_name])))

    return ticket_number, fake_name[0], fake_name[1], position_name, salary, skills


def get_unique_salary(employers_in: list) -> list:
    salaries_inner = {v: k for k, v in SALARIES.items()}
    salary_name = salaries_inner.get(employers_in[0][-2], SALARIES[HR_SALARY])
    salary_range = tuple(map(int, salary_name.split('-')))
    unique_salary = random.sample(range(salary_range[0], salary_range[1]), len(employers_in))
    result = list()
    i = 0
    for employer in employers_in:
        empl = []
        for v in employer:
            empl.append(v)
        empl.append(unique_salary[i])
        result.append(empl)
        i += 1

    return result


if __name__ == '__main__':
    employers = [hire_person(random.choice(list(POSITION.keys()))) for i in range(200)]
    hr_employers = filter_employers_by_position(employers, POSITION[HR])
    ceo_employers = filter_employers_by_position(employers, POSITION[CEO])
    dev_employers = filter_employers_by_position(employers, POSITION[DEVELOPER])
    # Получаем уникальную зарплату из диапазона
    hr_employers = get_unique_salary(hr_employers)
    ceo_employers = get_unique_salary(ceo_employers)
    dev_employers = get_unique_salary(dev_employers)
    print(len(employers), employers)
    print(len(hr_employers), hr_employers)
    print(len(ceo_employers), ceo_employers)
    print(len(dev_employers), dev_employers)
    print(get_average_salary(employers))

    print()

    # Фильтруем по навыкам
    php_employers = filter_employers_by_skills(employers, SKILLS[DEV_SKILLS][0])
    usability_employers = filter_employers_by_skills(employers, SKILLS[CEO_SKILLS][2])
    coaching_employers = filter_employers_by_skills(employers, SKILLS[HR_SKILLS][2])
    print("PHP", len(php_employers), php_employers)
    print("Usability", len(usability_employers), usability_employers)
    print("Coaching", len(coaching_employers), coaching_employers)
