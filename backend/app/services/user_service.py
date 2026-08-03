from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate


def create_user(
    db: Session,
    user_data: UserCreate
):
    user = User(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email=user_data.email,
        password_hash=user_data.password,  # temporal, luego agregamos hash real
        birth_date=user_data.birth_date,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_users(db: Session):
    return db.query(User).all()
