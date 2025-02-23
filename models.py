# tests/test_models.py
from models import Student, Base
from sqlalchemy import create_engine # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore
import pytest

# Create an in-memory SQLite database for testing
@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_student_creation(session):
    # Create a new student
    new_student = Student(name="John Doe", email="john@example.com", grade=10)
    session.add(new_student)
    session.commit()

    # Query the student
    student = session.query(Student).filter_by(name="John Doe").first()
    assert student is not None
    assert student.name == "John Doe"
    assert student.email == "john@example.com"
    assert student.grade == 10