from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = 'postgresql://root:123456@localhost:5432/triangle_desktop_app'
engine = create_engine(db_url, echo=True)

Session = sessionmaker(bind=engine)
