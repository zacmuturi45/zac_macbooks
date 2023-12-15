import click
from alembic.config import Config as AlembicConfig
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base
from models import add_shipment, place_order, show_available_models, zac_macbooks


ALEMBIC_INI_PATH = "/home/isaac/Documents/SQL/mapping/Alembic/project-mode/cli-project/alembic.ini"
alembic_cfg = AlembicConfig(ALEMBIC_INI_PATH)
DATABASE_URL = alembic_cfg.get_section_option("alembic", "sqlalchemy.url")

@click.command()
def cli():

    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()


    print("Welcome to Zac Muturi's MacBook Shop.")

    while True:
        print("\nChoose an option:")
        print("1. About Zac's Macbook Shop")
        print("2. See available models")
        print("3. Place Order")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3): ")

        
        if choice == "1":
            zac_macbooks(db)
        elif choice == "0":
            model = input("Please enter MacBook model: ")
            quantity = int(input("Enter quantity received: "))
            price = float(input("Please enter price: "))
            add_shipment(db, model, price, quantity)
        elif choice == "2":
            show_available_models(db)
            model_id = int(input("Please choose the model you want to order: "))
            quantity = int(input("Enter quantity to order: "))
            place_order(db, model_id, quantity)
        elif choice == "3":
            model = input("Please enter MacBook model: ")
            quantity = int(input("Enter quantity to order: "))
            place_order(db, model, quantity)
        elif choice == "4":
            print("Now exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")



if __name__ == "__main__":
    cli()