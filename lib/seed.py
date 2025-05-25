#!/usr/bin/env python3
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie
from sqlalchemy import create_engine

# Script goes here!
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

session.query(Freebie).delete()
session.query(Company).delete()
session.query(Dev).delete()

dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")
dev3 = Dev(name="John")

company1 = Company(name="Centrino", founding_year=2012)
company2 = Company(name="Google", founding_year=1998)

freebie1 = Freebie(item_name="T-shirt", value=10, company=company1, dev=dev1)
freebie2 = Freebie(item_name="Sticker", value=1, company=company1, dev=dev2)
freebie3 = Freebie(item_name="Mug", value=15, company=company2, dev=dev1)

session.add_all([dev1, dev2, dev3, company1, company2, freebie1, freebie2, freebie3])
session.commit()