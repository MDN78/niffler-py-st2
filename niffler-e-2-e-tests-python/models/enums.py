from dataclasses import dataclass
from faker import Faker
import random

fake = Faker()


@dataclass
class Category:
    TEST_CATEGORY1 = fake.word()
    TEST_CATEGORY2 = fake.word()
    TEST_CATEGORY3 = fake.word()
    TEST_CATEGORY4 = fake.word()




@dataclass
class Information:
    DESCRIPTION = fake.word()
    AMOUNT = random.randint(10, 1000)
    NAME = fake.name()
