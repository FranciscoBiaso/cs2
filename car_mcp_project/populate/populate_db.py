from db.models import Base, Car, get_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random

fake = Faker()

def create_fake_car():
    return Car(
        brand=fake.company(),
        model=fake.word(),
        year=random.randint(1995, 2024),
        engine=random.choice(['1.0', '1.6', '2.0', 'V6', 'V8']),
        fuel=random.choice(['Gasolina', 'Etanol', 'Diesel', 'Flex', 'Elétrico']),
        color=fake.color_name(),
        mileage=random.randint(0, 250_000),
        doors=random.choice([2, 4]),
        transmission=random.choice(['Manual', 'Automático', 'CVT']),
        price=round(random.uniform(20000, 250000), 2)
    )

def main():
    engine = get_engine()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for _ in range(120):
        session.add(create_fake_car())
    session.commit()
    print("Banco populado com 120 veículos fake.")

if __name__ == "__main__":
    main()
