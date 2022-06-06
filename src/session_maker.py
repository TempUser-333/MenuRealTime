from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import (create_database,
                              database_exists)
from MenuApp.models import Base
from local_settings import my_credentials as settings
from logger_files.custom_logger import logger


class SessionManager(object):

    def get_engine(self, user, password, host, port, database):
        conn_str = 'postgresql+psycopg2://%s:%s@%s:%s/%s' % (user, password, host, port, database)
        
        if not database_exists(conn_str):
            create_database(conn_str)
            logger.info('session started')
            
        engine = create_engine(conn_str, pool_size=50, echo=True)
        Base.metadata.create_all(engine)
        logger.info('engine created')
        
        return engine

            
    def get_session(self):
        
        engine = self.get_engine(*[settings[i] for i in settings])
        session = sessionmaker(bind=engine)
        
        return session