from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


config  = {
    **dotenv_values('.env')
}

engine = create_engine(f"postgresql://{config['DB_USER']}:{config['DB_PASSWORD']}@{config['DB_HOST']}/{config['DB_NAME']}", echo=True)
Session = sessionmaker(autoflush=False, bind=engine)
