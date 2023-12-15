from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Shipments(Base):
    __tablename__ = 'shipments'

    id = Column(Integer(), primary_key=True)
    model = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)

class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer(), primary_key=True)
    model = Column(String, nullable=False, unique=True)
    price = Column(Float, nullable=False)
    quantity_available = Column(Integer, nullable=False)

class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    model = Column(String(), ForeignKey('inventory.model'), nullable=False)
    quantity = Column(Integer(), nullable=False)

    inventory = relationship('Inventory')


def add_shipment(db, model, price, quantity):

    shipment = Shipments(model=model, price=price, quantity=quantity)
    db.add(shipment)
    db.commit()

    inventory_item = db.query(Inventory).filter_by(model=model).first()
    if inventory_item:
        inventory_item.quantity_available += quantity
    else:
        new_inventory_item = Inventory(model=model, price=price, quantity_available=quantity)
        db.add(new_inventory_item)

    db.commit()
    print(f"Shipment added, and inventory updated/created - Model: {model}, Quantity: {quantity}")


def zac_macbooks(db):
    print(
        """Zac Macbooks was started in 2015 to resale American preowned Macbooks. We pride ourselves in offering value for 
money for our clients. We offer tech essentials we consider vital to your setup when you buy from us. We consider
it a priority that our customers get the full tech buy experience by bundling any Macbooks bought from us with what 
we consider useful for the customer. Please check available inventory and what free goodies you get with your purchase.
Our current stock:"""
    )

    show_available_models(db)

    while True:
        print("\nChoose an option:")
        print("1. Proceed to make a purchase")
        print("2. Main Menu")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            model_id = int(input("Please choose the model you want to order (enter the model ID): "))
            quantity = int(input("Enter quantity to order: "))
            place_order(db, model_id, quantity)
        elif choice == "2":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")



def place_order(db, model_id, quantity):
    models = db.query(Inventory).all()

    print("Available Models:")
    for model in models:
        print(f"ID: {model.id}, Model: {model.model}, Price: ${model.price}, Quantity Available: {model.quantity_available}")
        

    selected_model = db.query(Inventory).filter_by(id=model_id).first()

    if selected_model:
        available_quantity = selected_model.quantity_available

        if available_quantity is not None and available_quantity >= quantity:
            order = Orders(model=selected_model.model, quantity=quantity)
            db.add(order)
            db.commit()

            selected_model.quantity_available -= quantity
            db.commit()

            print("\n🎉🎉🎉 Order Placed Successfully! 🎉🎉🎉")
            print(f"Model: {model.model}")
            print(f"Ordered Quantity: {quantity}")
            print(f"Total Price: ${quantity * selected_model.price}")
            print("Thank you for shopping with Zac Macbooks! 🚀")
        else:
            print("❌ Insufficient inventory for the specified order.")
    else:
        print("❌ Invalid model ID. Please choose a valid model.")


def show_available_models(db):
    models = db.query(Inventory).all()

    if models:
        print("Available Models:")
        for model in models:
            print(f"ID: {model.id}, Model: {model.model}, Price: ${model.price}, Quantity Available: {model.quantity_available}")
    else:
        print("No models available in the inventory.")




def reset_database(engine):
    Base.metadata.drop_all(bind=engine)

    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':

    engine = create_engine('sqlite:///zac_muturi.db')
    reset_database(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



