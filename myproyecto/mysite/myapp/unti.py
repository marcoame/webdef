from myapp.models import Projects
import json

f = open ('mydefjson.json', "r")
  
# Reading from file
data = json.loads(f.read())

for i in data:
    p=Projects(id_project=i["id"], publishable = i["publishable"], published =i["published"], title = i["title"], main_language = i["main_language"],start_date = i["start_date"], end_date = i["end_date"],status=i["status"], coordinating_institution=i["coordinating_institution"],department = i["department"],manager_name = i["manager_name"]+" "+i["manager_surname"], participant1_name = i["participant1_name"], participant1_surname = i["participant1_surname"], participant2_name = i["participant2_name"], participant2_surname = i["participant2_surname"],participant3_name = i["participant3_name"], participant3_surname = i["participant3_surname"],participant4_name = i["participant4_name"], participant4_surname = i["participant4_surname"],participant5_name = i["participant5_name"], participant5_surname = i["participant5_surname"],participant6_name = i["participant6_name"], participant6_surname = i["participant6_surname"],participant7_name = i["participant7_name"], participant7_surname = i["participant7_surname"],participant8_name = i["participant8_name"], participant8_surname = i["participant8_surname"], participant9_name = i["participant9_name"], participant9_surname = i["participant9_surname"],participant10_name = i["participant10_name"], participant10_surname = i["participant10_surname"], project_category1 = i["project_category1"],project_category2 = i["project_category2"],project_category3 = i["project_category3"],project_category4 = i["project_category4"],project_category5 = i["project_category5"], academic_discipline1 = i["academic_discipline1"], academic_discipline2 = i["academic_discipline2"],academic_discipline3 = i["academic_discipline3"],academic_discipline4 = i["academic_discipline4"],academic_discipline5 = i["academic_discipline5"], keyword1 = i["keyword1"],keyword2 = i["keyword2"],keyword3 = i["keyword3"], keyword4 = i["keyword4"], keyword5 = i["keyword5"], summary = i["summary"], funding1 = i["funding1"], funding2 = i["funding2"], funding3 = i["funding3"], funding4 = i["funding4"],funding5 = i["funding5"],total_funding_amount= i["amount"], currency = i["currency"], contact_email = i["contact_email"], contact_phone=i["contact_phone"])
    p.save()
    

