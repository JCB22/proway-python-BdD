from database import engine, Base, session
from models import User, UserProfile, Order

if __name__ == '__main__':

    Base.metadata.create_all(engine)



