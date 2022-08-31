original_input = '''{
 "description": "<ul><li>поддержка текущих проектов и сервисов компании,</li><li>разработка новых и доработка существующих функций по техническим заданиям,</li><li>активное взаимодействие с командой разработки,</li><li>освоение новых технологий и развитие профессиональных навыков под руководством опытного наставника.</li><li>Написание автотестов</li></ul>",
 "employment": "fullDay",
 "address": {
   "region": "Кировская",
   "city": "Киров",
   "street_type": "",
   "street": "",
   "house_type": "",
   "house": "",
   "value": "г Киров, ул Володарского, д 157",
   "lat": 58.593565,
   "lng": 49.672739
 },
 "name": "Junior Backend-developer",
 "salary": {
   "from": 30000,
   "to": 70000,
   "currency": "RUR",
   "gross": false
 },
 "contacts": {
   "fullName": "Журавлев Илья",
   "phone": "79536762399",
   "email": "ilya.zhuravlev@hrb.software"
 }
}'''

original_output = '''{"address": "г Киров, ул Володарского, д 157", "allow_messages": true, "billing_type": "packageOrSingle", "business_area": 1, "contacts": {"email": "ilya.zhuravlev@hrb.software", "name": "Журавлев Илья", "phone": {"city": "953", "country": "7", "number": "676-23-99"}}, "coordinates": {"latitude": 58.593565, "longitude": 49.672739}, "description": "<ul><li>поддержка текущих проектов и сервисов компании,</li><li>разработка новых и доработка существующих функций по техническим заданиям,</li><li>активное взаимодействие с командой разработки,</li><li>освоение новых технологий и развитие профессиональных навыков под руководством опытного наставника.</li><li>Написание автотестов</li></ul>", "experience": {"id": "noMatter"}, "html_tags": true, "image_url": "https://img.hhcdn.ru/employer-logo/3410666.jpeg", "name": "Junior Backend-developer", "salary": 70000, "salary_range": {"from": 30000, "to": 70000}, "schedule": {"id": "fullDay"}}'''

incorrect_input = '''{
 "description": "<ul><li>поддержка текущих проектов и сервисов компании,</li><li>разработка новых и доработка существующих функций по техническим заданиям,</li><li>активное взаимодействие с командой разработки,</li><li>освоение новых технологий и развитие профессиональных навыков под руководством опытного наставника.</li><li>Написание автотестов</li></ul>",
 "employment": "fullDay",
 "address": {
   "region": "Кировская",
   "city": "Киров",
   "street_type": "",
   "house_type": "",
   "house": "",
   "value": "г Киров, ул Володарского, д 157",
   "lat": 58.593565,
   "lng": 49.672739
 },
 "name": "Junior Backend-developer",
 "salary": {
   "from": 30000,
   "currency": "RUR",
   "gross": false
 },
 "contacts": {
   "fullName": "Журавлев Илья",
   "email": "ilya.zhuravlev@hrb.software"
 }
}'''

int_phone_in_contacts = '''{
   "fullName": "Журавлев Илья",
   "phone": 79536762399,
   "email": "ilya.zhuravlev@hrb.software"
   }
'''

incorrect_coords = '''{
   "region": "Кировская",
   "city": "Киров",
   "street_type": "",
   "street": "",
   "house_type": "",
   "house": "",
   "value": "г Киров, ул Володарского, д 157",
   "lat": 91.593565,
   "lng": 199.672739
 }'''
