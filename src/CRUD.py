import json
import chardet
from MenuApp.models import MENU


class CRUDServer(object):
    def insert_entire_data(self, session_obj, *args, **kwargs):
        print('+++++++++++++++++++++++++++++')
        with open('sample_data/menu_items.json', mode='rb') as f1:
            _encoding = chardet.detect(f1.read())['encoding']  
        print(_encoding)
        print('//////////////////////////////////')
        with open('sample_data/menu_items.json', mode='r', encoding=_encoding) as f:
            res_data = json.load(f)
        
        for rec in res_data:
            rec1 = '' if rec['timeApplicable'] else str(rec['timeApplicable'])
            rec2 = [str(i) for i in rec['menuItems']] if rec['menuItems'] else []
            rec3 = [str(j) for j in rec['subCategories']] if rec['subCategories'] else []
            
            session_obj.add(
                            MENU(_id = rec['id'],
                                 cExternalID = rec['cExternalID'],
                                 name = rec['name'],
                                 level = rec['level'],
                                 categoryAvailability = rec['categoryAvailability'],
                                 checkAllMenuAvailability = rec['checkAllMenuAvailability'],
                                 timeApplicable = rec1,
                                 oExternalID = rec['oExternalID'],
                                 isComboCat = rec['isComboCat'],
                                 subCategories = rec3,
                                 menuItems = rec2
                                )
                            )
        return 'Data inserted successfully'
        
    def get_all_the_categories_in_the_menu(self, session_obj, *args, **kwargs):
    
        res = session_obj.query(MENU).all()
        print('---------------------------------------------')
        return [rec.name.strip(' *') for rec in res] if res else 'No data found'
        
    def check_the_presence_of_menuitems_in_the_categories(self, session_obj, *args, **kwargs):
        
        res = session_obj.query(MENU).all()
        return {rec.name.strip(' *'): ['PRESENT' if rec.menuItems else 'ABSENT'][0] for rec in res} if res else 'No data found'
        
    def get_menuitems_in_the_categories(self, session_obj, *args, **kwargs):
        
        res = session_obj.query(MENU).all()
        print('*******************************************************')
        return {rec.name.strip(' *'): [[eval(rec1)['name'] for rec1 in rec.menuItems] if rec.menuItems else 'No menuItems present'][0] for rec in res} \
                if res else 'No data found'
                
    def check_for_subcategories_in_the_categories(self, session_obj, *args, **kwargs):
        
        res = session_obj.query(MENU).all()
        return {rec.name.strip(' *'): ['PRESENT' if rec.subCategories else 'ABSENT'][0] for rec in res} if res else 'No subcategories present'
        
    def get_subcategories_in_the_categories(self, session_obj, *args, **kwargs):
        
        res = session_obj.query(MENU).all()
        print('************************')
        return {rec.name.strip(' *'): [[eval(rec1)['name'] for rec1 in rec.subCategories] if rec.subCategories else 'No subcategories present'][0] for rec in res} \
                if res else 'No data found'
                
                
    def check_for_menuitems_in_subcategories(self, session_obj, *args, **kwargs):
    
        res = session_obj.query(MENU).all()
        
        d = {}
        if res:
            for rec in res:
                d.update({eval(rec1)['name']: ['PRESENT' if eval(rec1)['menuItems'] else 'ABSENT'][0] for rec1 in rec.subCategories}) if rec.subCategories else ...
            return d
        else:
            return 'No data found'
                
        
    def get_menuitems_in_the_subcategories(self, session_obj, *args, **kwargs):
        
        res = session_obj.query(MENU).all()
        print('*********************')
        
        d = {}
        if res:
            for rec in res:
                d.update({eval(rec1)['name']: [[rec2['name'] for rec2 in eval(rec1)['menuItems']] if eval(rec1)['menuItems'] else 'No menuitems present'][0] for rec1 in rec.subCategories}) \
                          if rec.subCategories else ...
            return d
        else:
            return 'No data found'
            
    def get_overview_of_the_entire_menu(self, session_obj, *args, **kwargs):
        res = session_obj.query(MENU).all()
        
        cat = {}
        sub_cat = {}
        final_dict = {}
        if res:
            for rec in res:
                print('---------------------------------------')
                cat.update({'CATEGORIES': [eval(rec1)['name'] for rec1 in rec.menuItems]}) if rec.menuItems else ...
                sub_cat.update({'SUBCATEGORIES': {eval(rec1)['name']: [[rec2['name'] for rec2 in eval(rec1)['menuItems']] if eval(rec1)['menuItems'] else 'No menuItems present'][0] for rec1 in rec.subCategories}}) if rec.subCategories else ...
                
                if not cat:
                    cat['CATEGORIES'] = 'No categories present'
                if not sub_cat:
                    sub_cat['SUBCATEGORIES'] = 'No subcategories present'
                    
                final_dict[rec.name.strip(' *')] = [cat, sub_cat]
                cat = {}
                sub_cat = {}
            return final_dict
            
        else:
            return 'No data found'
            
                