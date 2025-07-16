import pytest
from db.models import Base, Car, get_engine
from sqlalchemy.orm import sessionmaker

@pytest.fixture
def session():
    engine = get_engine()
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()
    yield sess
    sess.close()

def test_insert_and_query(session):
    car = Car(
        brand="TestBrand",
        model="ModelX",
        year=2022,
        engine="2.0",
        fuel="Flex",
        color="Preto",
        mileage=10000,
        doors=4,
        transmission="Automático",
        price=90000
    )
    session.add(car)
    session.commit()
    result = session.query(Car).filter_by(brand="TestBrand").first()
    assert result is not None
    assert result.model == "ModelX"
