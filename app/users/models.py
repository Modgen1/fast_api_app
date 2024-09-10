from app.database import Base, int_pk, str_uniq
from sqlalchemy.orm import Mapped

class User(Base):
    id: Mapped[int_pk]
    username: Mapped[str_uniq]
    pass_hash: Mapped[str_uniq]

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username}"