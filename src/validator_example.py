import csv

from pydantic import BaseModel, PositiveInt


class Person(BaseModel):
    name: str
    age: PositiveInt


with open('data/people.csv') as f:
    reader = csv.DictReader(f)
    people = [Person.model_validate(row) for row in reader]

print(people)
#> [Person(name='John Doe', age=30, email='john@example.com'), Person(name='Jane Doe', age=25, email='jane@example.com')]