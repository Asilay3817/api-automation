from faker import Faker
import random

fake=Faker()
gender = random.choice(["male", "female"])

def generate_phone() -> str:
    return f"+79{random.randint(100000000, 999999999)}"

class Payloads:
    create_student = {
        "email": fake.email(),
        "gender": gender,
        "name": fake.name(),
        "phone_no": generate_phone(),
        "status": 1
    }


