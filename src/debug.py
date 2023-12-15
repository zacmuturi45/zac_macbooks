from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Inventory, Base

if __name__ == '__main__':
    engine = create_engine('sqlite:///zac_muturi.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    macbook_pro = Inventory(
        model="2023 Macbook Pro 15inches",
        price=1254.98,
        quantity_available = 3
    )

    session.add(macbook_pro)
    session.commit()




