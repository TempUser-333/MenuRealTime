from django.db import models
from sqlalchemy import (
                        Column,
                        Integer,
                        String,
                        ARRAY,
                        Boolean,
                        )
from sqlalchemy.ext.declarative import declarative_base
# Create your models here.

Base = declarative_base()


# class MENU(Base):
    # __tablename__ = 'menu_info'
    
    # _id = Column(String(100), primary_key=True)
    # cExternalID = Column(String(100))
    # name = Column(String(100))
    # level = Column(String(100))
    # categoryAvailability = Column(Boolean)
    # checkAllMenuAvailabilty = Column(Boolean)
    # timeApplicable = Column(String(200))
    # oExternalID = Column(String(200))
    # isComboCat = Column(Boolean)
    # subCategories = Column(ARRAY(String(600)))
    # menuItems = Column(ARRAY(String(600)))
    
 
# class MENU(Base):
    # __tablename__ = 'menu_info_1'
    
    # _id = Column(String(100), primary_key=True)
    # cExternalID = Column(String(100))
    # name = Column(String(100))
    # level = Column(String(100))
    # categoryAvailability = Column(Boolean)
    # checkAllMenuAvailabilty = Column(Boolean)
    # timeApplicable = Column(String(200))
    # oExternalID = Column(String(200))
    # isComboCat = Column(Boolean)
    # subCategories = Column(ARRAY(String(600)))
    # menuItems = Column(ARRAY(String(600)))
    
 
# class MENU(Base):
    # __tablename__ = 'menu_info_2'
    
    # _id = Column(String(100), primary_key=True)
    # cExternalID = Column(String(100))
    # name = Column(String(100))
    # level = Column(String(100))
    # categoryAvailability = Column(Boolean)
    # checkAllMenuAvailability = Column(Boolean)
    # timeApplicable = Column(String(200))
    # oExternalID = Column(String(200))
    # isComboCat = Column(Boolean)
    # subCategories = Column(ARRAY(String(600)))
    # menuItems = Column(ARRAY(String(600)))
    
  
# class MENU(Base):
    # __tablename__ = 'menu_info_3'
    
    # _id = Column(String(), primary_key=True)
    # cExternalID = Column(String())
    # name = Column(String())
    # level = Column(String())
    # categoryAvailability = Column(Boolean)
    # checkAllMenuAvailabilty = Column(Boolean)
    # timeApplicable = Column(String())
    # oExternalID = Column(String())
    # isComboCat = Column(Boolean)
    # subCategories = Column(ARRAY(String()))
    # menuItems = Column(ARRAY(String()))
    
# class MENU(Base):
    # __tablename__ = 'menu_info_4'
    
    # _id = Column(String(), primary_key=True)
    # cExternalID = Column(String())
    # name = Column(String())
    # level = Column(String())
    # categoryAvailability = Column(Boolean)
    # checkAllMenuAvailability = Column(Boolean)
    # timeApplicable = Column(String())
    # oExternalID = Column(String())
    # isComboCat = Column(Boolean)
    # subCategories = Column(ARRAY(String()))
    # menuItems = Column(ARRAY(String()))
    
class MENU(Base):
    __tablename__ = 'menu_info_5'
    
    _id = Column(String(), primary_key=True)
    cExternalID = Column(String())
    name = Column(String())
    level = Column(String())
    categoryAvailability = Column(Boolean)
    checkAllMenuAvailability = Column(Boolean)
    timeApplicable = Column(String())
    oExternalID = Column(String())
    isComboCat = Column(Boolean)
    subCategories = Column(ARRAY(String()))
    menuItems = Column(ARRAY(String()))