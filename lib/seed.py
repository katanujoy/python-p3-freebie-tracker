from database import Session, engine
from models import Company, Dev, Freebie, Base

def seed():
    # Dropped and recreated all tables
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # Started a session
    session = Session()

    # Created sample companies
    company1 = Company(name="Tech Corp", founding_year=1995)  
    company2 = Company(name="Innovate Inc", founding_year=2015)
    company3 = Company(name="Joyemy Company", founding_year=2002)  

    # Created sample developers
    devs = [
        Dev(name="Joy Katanu"),
        Dev(name="Alex Mwangi"),
        Dev(name="Sam Njeri"),
        Dev(name="Liam Otieno"),
        Dev(name="Chloe Wambui"),
        Dev(name="Brian Oloo"),
        Dev(name="Zara Kimani"),
        
    ]

    # Created sample freebies
    freebies = [
        Freebie(item_name="Jacket", value=50, company=company1, dev=devs[0]),
        Freebie(item_name="Tote Bag", value=20, company=company2, dev=devs[1]),
        Freebie(item_name="Hoodie", value=60, company=company1, dev=devs[2]),
        Freebie(item_name="T-Shirt", value=25, company=company3, dev=devs[3]),
        Freebie(item_name="Blanket", value=40, company=company3, dev=devs[4]),
        Freebie(item_name="Baseball Cap", value=15, company=company2, dev=devs[5]),
        Freebie(item_name="Laptop Sticker Pack", value=10, company=company1, dev=devs[6]),
    ]

    # Added all data to the session
    session.add_all([company1, company2, company3] + devs + freebies)

    # Committed and closed
    session.commit()
    session.close()

    print("Sprinkled some sample data,Yay!✨")

if __name__ == '__main__':
    seed()
