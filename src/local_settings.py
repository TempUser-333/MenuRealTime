from collections import OrderedDict
import os


my_credentials = OrderedDict({'user': os.environ['DB_USER_NAME'],
                              'password': os.environ['DB_PASSWORD'],
                              'host': os.environ['DB_HOST'],
                              'port': os.environ['DB_PORT'],
                              'database': 'RealTimeMenu_Favicon_Two_DB'})
