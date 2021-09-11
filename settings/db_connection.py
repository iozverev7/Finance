import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings.config_scrips import Config

db_config = Config().get_params_for_db()
connection = psycopg2.connect(
  database=db_config['PG_BASE'],
  user=db_config['PG_USER'],
  host=db_config['PG_HOST'],
  password=db_config['PG_PASSWORD']
)

engine = create_engine(
  f"postgresql://{db_config['PG_USER']}:{db_config['PG_PASSWORD']}@{db_config['PG_HOST']}/{db_config['PG_BASE']}"
)
Session = sessionmaker(bind=engine)
