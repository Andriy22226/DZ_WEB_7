import random

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from database.db import session
from database.models import  Subject,Teacher


fake = Faker('uk-UA')


def insert_subject():
    teachers = session.query(Teacher).all()
    subject_list = [    "Економіка",
                        "Креслення",
                        "Електроіка",
                        "Алгебра",
                        "Філософія",
                        "Фізкультура",
                        "Історія",
                        "Геометрія",
                        "Математика"]
    for name in subject_list:
        subject = Subject(
            subject_name=name,
            teacher_id=random.choice(teachers).id)
        session.add(subject)







if __name__ == '__main__':
    try:
        insert_subject()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()
