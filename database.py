from sqlalchemy.orm import sessionmaker


from sqlalchemy import create_engine

db_url="postgresql://postgres:12345@localhost:5432/mydatabase"
engine=create_engine(db_url)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
session = SessionLocal()