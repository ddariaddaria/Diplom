import requests
import time
from pprint import pprint

def get_api_data(url, params = ''):
    r = requests.get(url, params)
    return r.json()

url = r'https://api.hh.ru/vacancies'
par = {'text': 'аналитик', 'area': 113}
data = get_api_data(url, params=par)

vac_ids = []
for one_vac in data['items']:
    vac_ids.append(one_vac['id'])

vac_info = []
for one_vac in data['items']:
    url = f'https://api.hh.ru/vacancies/{one_vac["""id"""]}'
    vac_descr = get_api_data(url)
    vac_info.append({
        'area': vac_descr['area']['name'],
        'description': vac_descr['description'],
        'employment': vac_descr['employment']['name'],
        'experience': vac_descr['experience']['name'],
        'id': vac_descr['id'],
        'key_skills': vac_descr['key_skills'],
        'name': vac_descr['name'],
        'publication_date': vac_descr['published_at'],
        'salary': vac_descr['salary'],
        'schedule': vac_descr['schedule']['name'],
        'specializations': vac_descr['specializations'],
        'proffesional_roles': vac_descr['professional_roles']
        
    })
    time.sleep(0.8)
pprint(vac_info)
    






