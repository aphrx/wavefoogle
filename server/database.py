import sqlalchemy as sql
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm
import config as config

engine = sql.create_engine(config.DATABASE_URL)

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative.declarative_base()