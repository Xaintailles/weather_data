# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 12:18:03 2023

@author: Calixte
"""

#%% Function made to take as input a date with Dutch names and spit it as an english formatted date
def replace_with_dict(string_to_format: str, dict_to_use: dict) -> str:
    
    for dutch_word, english_word in dict_to_use.items():
        
        transformed_string = ''
                
        if string_to_format.find(dutch_word) >= 0:
            transformed_string = string_to_format.replace(dutch_word,english_word)
        else:
            continue
    
    return(transformed_string)

def format_dutch_date(date_to_format: str) -> str:
    
    dutch_days = {
        'Maandag': 'Monday',
        'Dinsdag': 'Tuesday',
        'Woensdag': 'Wednesday',
        'Donderdag': 'Thursday',
        'Vrijdag': 'Friday',
        'Zaterdag': 'Saturday',
        'Zondag': 'Sunday',
        }

    dutch_months = {
        'Januari':'January',
        'Februari':'February',
        'Maart':'March',
        'April':'April',
        'Mei':'May',
        'Juni':'June',
        'Juli':'July',
        'Augustus':'August',
        'September':'September',
        'Oktober':'October',
        'November':'November',
        'December':'December',
        }
    
    date_to_format = replace_with_dict(string_to_format = date_to_format, dict_to_use = dutch_days)
    date_to_format = replace_with_dict(string_to_format = date_to_format, dict_to_use = dutch_months)
    
    return(date_to_format)