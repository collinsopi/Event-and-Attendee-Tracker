from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
import os

# Create the events.db file in the project's root directory
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
db_url = URL.create(
    drivername="sqlite",
    database=os.path.join(base_dir, "events.db")
)

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()