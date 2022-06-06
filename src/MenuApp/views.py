from django.shortcuts import render
from sqlalchemy.exc import (InterfaceError,
                            IntegrityError,
                            OperationalError,
                            ArgumentError,
                            ProgrammingError,)
from rest_framework.views import APIView
import psycopg2
import sys
from session_maker import SessionManager
from CRUD import CRUDServer
from logger_files.custom_logger import logger
# Create your views here.

session = SessionManager().get_session()

class InsertSampleData(APIView):
    def put(self, request):
        l = []
        try:
            session_obj = session()
            print('*****************************************')
            res = CRUDServer().insert_entire_data(session_obj)
            
        except (ImportError, NameError, AttributeError, TypeError):
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except (OperationalError, ArgumentError, InterfaceError, IntegrityError, ProgrammingError):
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except psycopg2.OperationalError:
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except Exception as ex:
            l.append((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
            session_obj.rollback()
            logger.info('session rolled back')
            
        else:
            l.append(res)
            session_obj.commit()
            logger.info('session committed')
            
        finally:
            with open('templates/template_1.html', mode='w', encoding='utf-8') as f:
                f.write('<doctype html>\n<html>\n<body><p><font color = #FF0000>' + str(l) + '</p></font></body>\n</html>')
            session_obj.close()
            logger.info('session closed')
            
            return render(request, 'template_1.html', {})
            
    
class GetCategoriesInTheMenu(APIView):
    def get(self, request):
        l = []
        try:
            session_obj = session()
            logger.info('session started')
            print('******************************')
            res = CRUDServer().get_all_the_categories_in_the_menu(session_obj)
            
            with open('href_file.txt', mode='r') as f1:
                data = f1.read()
         
        except (ImportError, NameError, TypeError, AttributeError):
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except (IntegrityError, InterfaceError, OperationalError, ArgumentError, ProgrammingError):
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except psycopg2.OperationalError:
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except Exception as ex:
            l.append((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
            session_obj.rollback()
            logger.info('session rolled back')
            
        else:
            l.append(res)
            session_obj.commit()
            logger.info('session committed')
            
        finally:
            with open('templates/template_2.html', mode='w', encoding='utf-8') as f:
                f.write('{% load static %}\n<!doctype html>\n<html>\n<head>\n<title>' + 'MENU' + '</title>\n</head>\n' + 
                        '<link rel="icon" href=' + '"' + data + '"' + ' type="image/x-icon"/>\n' + 
                        '<body><p>' + 'The categories in the menu are: ' + '<font color = #00FF00>' + str(l) + 
                        '</font></p></body>\n</html>')
            session_obj.close()
            logger.info('session closed')
            
            return render(request, 'template_2.html', {})
            
            
         
class CheckThePresenceOfMenuItemsInTheCategories(APIView):
    def get(self, request):
        l = []
        try:
            session_obj = session()
            logger.info('session started')
            res = CRUDServer().check_the_presence_of_menuitems_in_the_categories(session_obj)
            
            with open('href_file.txt', mode='r') as f1:
                data = f1.read()
            
        except (TypeError, NameError, AttributeError, ImportError):
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except (IntegrityError, InterfaceError, OperationalError, ArgumentError, ProgrammingError):
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except psycopg2.OperationalError:
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except Exception as ex:
            l.append((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
            session_obj.rollback()
            logger.info('session rolled back')
            
        else:
            l.append(res)
            session_obj.commit()
            logger.info('session committed')
            
        finally:
            with open('templates/template_3.html', mode='w', encoding='utf-8') as f:
                f.write('{% load static %}\n<!doctype html>\n<html>\n<head>\n<title>' + 'MENU' + '</title>\n</head>' + 
                        '<link rel="icon" href=' + '"' + data + '"' + ' type="image/x-icon"/>\n' + 
                        '<body><p>' + 'Whether menuitems present or not in the categories' + '<font color = #0000FF>' + str(l) + 
                        '</font></p></body>\n</html>')
            session_obj.close()
            logger.info('session closed')
            
            return render(request, 'template_3.html', {})
            
class GetMenuItemsInTheCategories(APIView):
    def get(self, request):
        l = []
        try:
            session_obj = session()
            logger.info('session started')
            
            res = CRUDServer().get_menuitems_in_the_categories(session_obj)
            with open('href_file.txt', mode='r') as f1:
                data = f1.read()
            
        except (ImportError, NameError, TypeError, AttributeError):
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except (IntegrityError, InterfaceError, OperationalError, ArgumentError, ProgrammingError):
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session closed')
            
        except psycopg2.OperationalError:
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except Exception as ex:
            l.append((type(ex), sys.exc_info(), sys.exc_info()))
            session_obj.rollback()
            logger.info('session rolled back')
            
        else:
            l.append(res)
            session_obj.commit()
            logger.info('session committed')
            
        finally:
            with open('templates/template_4.html', mode='w', encoding='utf-8') as f:
                f.write('{% load static %}\n<!doctype html>\n<html>\n<head>\n<title>' + 'MENU' + '</title>\n</head>\n' + 
                        '<link rel="icon" href=' + '"' + data + '"' + ' type="image/x-icon"/>\n' + 
                        '<body><p>' + 'The menuitems in the categories are: ' + '<font color = #FFFF00>' + str(l) + 
                        '</font></p></body>\n</html>')
            session_obj.close()
            logger.info('session closed')
            
            return render(request, 'template_4.html', {})
            
            
class CheckForSubCategoriesInTheCategories(APIView):
    def get(self, request):
        l = []
        try:
            session_obj = session()
            logger.info('session started')
            res = CRUDServer().check_for_subcategories_in_the_categories(session_obj)
            
            with open('href_file.txt', mode='r') as f1:
                data = f1.read()
            
        except (ImportError, NameError, TypeError, AttributeError):
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except (IntegrityError, InterfaceError, OperationalError, ArgumentError, ProgrammingError):
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session closed')
            
        except psycopg2.OperationalError:
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session closed')
            
        except Exception as ex:
            l.append((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
            session_obj.rollback()
            logger.info('session roll back')
            
        else:
            l.append(res)
            session_obj.commit()
            logger.info('session committed')
            
        finally:
            with open('templates/template_5.html', mode='w', encoding='utf-8') as f:
                f.write('{% load static %}\n<!doctype html>\n<html>\n<head>\n<title>' + 'MENU' + '</title>\n</head>\n' + 
                        '<link rel="icon" href=' + '"' + data + '"' + ' type="image/x-icon"/>\n' + 
                        '<body><p>' + 'Whether subcategories present in the categories or not: ' + '<font color = #00FFFF>' + str(l) + 
                        '</font></p></body>\n</html>')
            session_obj.close()
            logger.info('session closed')
            
            return render(request, 'template_5.html', {})
            

class GetSubCategoriesInTheCategories(APIView):
    def get(self, request):
        l = []
        try:
            session_obj = session()
            logger.info('session started')
            res = CRUDServer().get_subcategories_in_the_categories(session_obj)
            print(res)
            
            with open('href_file.txt', mode='r') as f1:
                data = f1.read()
            
        except (ImportError, NameError, TypeError, AttributeError):
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except (InterfaceError, IntegrityError, OperationalError, ArgumentError, ProgrammingError):
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session closed')
            
        except psycopg2.OperationalError:
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except Exception as ex:
            l.append((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
            session_obj.rollback()
            logger.info('session rolled back')
            
        else:
            l.append(res)
            session_obj.commit()
            logger.info('session committed')
            
        finally:
            with open('templates/template_6.html', mode='w', encoding='utf-8') as f:
                print('-------------------------------')
                print(str(l))
                f.write('{% load static %}\n<!doctype html>\n<html>\n<head>\n<title>\n' + 'MENU' + '</title>\n</head>\n' + 
                        '<link rel="icon" href=' + '"' + data + '"' + ' type="image/x-icon"/>\n' + 
                        '<body><p>' + 'The subcategories in the categories are: ' + '<font color = #FF00FF>' + str(l) + 
                        '</font></p></body>\n</html>')
                print('///////////////////////////////////////////')
            session_obj.close()
            logger.info('session closed')
            print('=============================================')
            
            return render(request, 'template_6.html', {})
            
class CheckForMenuItemsInTheSubCategories(APIView):
    def get(self, request):
        l = []
        try:
            session_obj = session()
            logger.info('session started')
            res = CRUDServer().check_for_menuitems_in_subcategories(session_obj)
            
            with open('href_file.txt', mode='r') as f1:
                data = f1.read()
            
        except (ImportError, NameError, TypeError, AttributeError):
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except (ArgumentError, InterfaceError, IntegrityError, OperationalError, ProgrammingError):
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except psycopg2.OperationalError:
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except Exception as ex:
            l.append((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
            session_obj.rollback()
            logger.info('session rolled back')
            
        else:
            l.append(res)
            session_obj.commit()
            logger.info('session committed')
            
        finally:
            with open('templates/template_7.html', mode='w', encoding='utf-8') as f:
                f.write('{% load static %}\n<!doctype html>\n<html>\n<head>\n<title>' + 'MENU' + '</title>\n</head>\n' + 
                        '<link rel="icon" href=' + '"' + data + '"' + ' type="image/x-icon"/>\n' + 
                        '<body><p>' + 'Whether menu items present or not in the subcategories' + '<font color = #000080>' + str(l) + 
                        '</font></p></body>\n</html>')
            session_obj.close()
            logger.info('session closed')
            
            return render(request, 'template_7.html', {})
            
        
class GetMenuItemsInTheSubCategories(APIView):
    def get(self, request):
        l = []
        try:
            session_obj = session()
            logger.info('session started')
            res = CRUDServer().get_menuitems_in_the_subcategories(session_obj)
            
            with open('href_file.txt', mode='r') as f1:
                data = f1.read()
                
            
        except (ImportError, NameError, AttributeError, TypeError):
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except (ArgumentError, InterfaceError, IntegrityError, OperationalError, ProgrammingError):
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except psycopg2.OperationalError:
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except Exception as ex:
            l.append((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
            session_obj.exc_info()
            logger.info('session rolled back')
            
        else:
            l.append(res)
            session_obj.commit()
            logger.info('session committed')
            
        finally:
            with open('templates/template_8.html', mode='w', encoding='utf-8') as f:
                f.write('{% load static %}\n<!doctype html>\n<html>\n<head>\n<title>' + 'MENU' + '</title>\n</head>\n' + 
                        '<link rel="icon" href=' + '"' + data + '"' + ' type="image/x-icon"/>\n' + 
                        '<body><p>' + 'The menuitems in the subcategories are: ' + '<font color = #328f8a>' + str(l) + 
                        '</font></p></body>\n</html>')
            session_obj.close()
            logger.info('session closed')
            
            return render(request, 'template_8.html', {})
            
            
class GetOverviewOfTheEntireMenu(APIView):
    def get(self, request):
        l = []
        try:
            session_obj = session()
            logger.info('session started')
            print('///////////////////////////////')
            res = CRUDServer().get_overview_of_the_entire_menu(session_obj)
            print('**********************')
            
            with open('href_file.txt', mode='r') as f1:
                data = f1.read()
            
        except (ImportError, NameError, TypeError, AttributeError):
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except (InterfaceError, IntegrityError, OperationalError, ProgrammingError, ArgumentError):
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except psycopg2.OperationalError:
            l.append(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')
            
        except Exception as ex:
            l.append((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
            session_obj.rollback()
            logger.info('session rolled back')
            
        else:
            l.append(res)
            session_obj.commit()
            logger.info('session committed')
            
        finally:
            with open('templates/template_9.html', mode='w', encoding='utf-8') as f:
                f.write('{% load static %}\n<!doctype html>\n<html>\n<head>\n<title>' + 'MENU' + '</title>\n</head>\n' + 
                        '<link rel="icon" href=' + '"' + data + '"' + ' type="image/x-icon"/>\n' + 
                        '<body><p>' + 'Overview of the menu: ' + '<font color = #00df67>' + str(l) + 
                        '</font></p></body>\n</html>')
            session_obj.close()
            logger.info('session closed')
            
            return render(request, 'template_9.html', {})
            