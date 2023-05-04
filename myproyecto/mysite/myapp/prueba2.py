

import requests
import json





def get_projects_from_cristin():
    num_pages = 5
    counter = 1
    projects = []
    
    #NTNU unit = 194.0.0.0 ---> I filtered all the projects in Cristin Api and we are only taking into account the ones with parent institution = NTNU
    #response = json.loads(requests.get("https://api.cristin.no/v2/projects?parent_unit_id=194.0.0.0&page=" +str(counter) +"&per_page=1000").text)
    #projects.append(response)
    
    while counter<= num_pages:
        
        response = json.loads(requests.get("https://api.cristin.no/v2/projects?parent_unit_id=194.0.0.0&page=" +str(counter) +"&per_page=1000").text)
        projects.append(response)
        counter +=1
        
        
        
    return projects

        
a = get_projects_from_cristin()
print("----------------")

print(a[0][1]["cristin_project_id"])


print(len(a[0]))

id_list = []
for i in range(0,5):
   
    for j in range(len(a[i])):
         
         id_list.append(a[i][j]["cristin_project_id"])


print(id_list)


#Store data about the projects

#try function for the title ---> different languages
 
def tryness(mynewjson,label):
    
    
    try:
       
        return mynewjson[label]["nb"]
        
    except:
        try:
            return mynewjson[label]["no"] 
        except:
            try:
                return mynewjson[label]["en"] 

            except:
                return
        

def filter_institution_name(mynewjson):
        try:
            
            return mynewjson["coordinating_institution"]["institution"]["institution_name"]["nb"]
        
        except:
            try:
                
                return mynewjson["coordinating_institution"]["institution"]["institution_name"]["no"] 
            except:
                return mynewjson["coordinating_institution"]["institution"]["institution_name"]["en"] 
            

def filter_department_name(mynewjson):
    
        
        try:
            
            return mynewjson["coordinating_institution"]["unit"]["unit_name"]["nb"]
        
        except:
            try:
                
                return mynewjson["coordinating_institution"]["unit"]["unit_name"]["no"] 
            except:
                return mynewjson["coordinating_institution"]["unit"]["unit_name"]["en"] 
            
            
            
def check_participants(mynewjson,x):
    
    long = len(mynewjson["participants"])
    if (x> long):
        print(long)
        return "", "",""
    
    else:
        try:
            
            
            mynewjson["participants"][x]
            return mynewjson["participants"][x]["first_name"], mynewjson["participants"][x]["surname"], mynewjson["participants"][x]["cristin_person_id"]
        
        except:
            return "", "",""
        
        

def check_category(mynewjson,x):
    
    try:
        mynewjson["project_categories"]
        try:
            long = len(mynewjson["project_categories"])
            if (x> long):
                print(11223333)
                print(long)
                return ""
        
            else:
                try:
                    mynewjson["project_categories"][x-1]["name"]
                    
                    
                    ################333
                    
                    try:
        
                        return mynewjson["project_categories"][x]["name"]["nb"]
            
                    except:
                        try:
                            return mynewjson["project_categories"][x]["name"]["no"] 
                        except:
                            return mynewjson["project_categories"][x]["name"]["en"]
                    
                    
                    
                    
                    ######################33
                
                except:
                    return ""
        
        except:
            return ""
    
    except:
        return ""
    
    
def check_discipline(mynewjson,x):
    try:
        mynewjson["academic_disciplines"]
        
    
        try:
            long = len(mynewjson["academic_disciplines"])
            if (x> long):
                print(11223333)
                print(long)
                return ""
        
            else:
                try:
                    mynewjson["academic_disciplines"][x]["name"]
                    
                    
                    ################333
                    
                    try:
        
                        return mynewjson["academic_disciplines"][x]["name"]["nb"]
            
                    except:
                        try:
                            return mynewjson["academic_disciplines"][x]["name"]["no"] 
                        except:
                            return mynewjson["academic_disciplines"][x]["name"]["en"]
                    
                    
                    
                    
                    ######################33
                
                except:
                    return ""
        
        except:
            return ""
    except:
        return ""
    
    
    
def check_keyword(mynewjson,x):
    
    try:
        mynewjson["keywords"]
        try:
            long = len(mynewjson["keywords"])
            if (x> long):
                print(11223333)
                print(long)
                return ""
        
            else:
                try:
                    mynewjson["keywords"][x]["name"]
                
                
                ################333
                
                    try:
        
                        return mynewjson["keywords"][x]["name"]["nb"]
            
                    except:
                        try:
                            return mynewjson["keywords"][x]["name"]["no"] 
                        except:
                            return mynewjson["keywords"][x]["name"]["en"]
                
                
                
                
                ######################33
            
                except:
                    return ""
    
        except:
            return ""
    except:
        return ""
        
    
    
def check_summary(mynewjson):
    
    try:
        mynewjson["academic_summary"]
        try:
            return mynewjson["academic_summary"]["nb"]
        except:
            try:
                mynewjson["academic_summary"]["no"] 
            except:
                mynewjson["academic_summary"]["en"]
    except:
        return ""
        
    try:
        mynewjson["popular_scientific_summary"]
            
        try:
                return mynewjson["popular_scientific_summary"]["nb"]
        except:
            try:
                return mynewjson["popular_scientific_summary"]["no"]
            except:
                return mynewjson["popular_scientific_summary"]["en"]
    except:
        return ""
            
        
        

def check_funding(mynewjson,x):
    
    
    try:
        mynewjson["project_funding_sources"]
        try:
            long = len(mynewjson["project_funding_sources"])
            if (x> long):
                print(11223333)
                print(long)
                return ""
        
            else:
                try:
                    mynewjson["project_funding_sources"][x]["funding_source_name"]
                    
                    
                    ################333
                    
                    try:
        
                        return mynewjson["project_funding_sources"][x]["funding_source_name"]["nb"]
            
                    except:
                        try:
                            return mynewjson["project_funding_sources"][x]["funding_source_name"]["no"] 
                        except:
                            return mynewjson["project_funding_sources"][x]["funding_source_name"]["en"]
                    
                    
                    
                    
                    ######################33
                
                except:
                    return ""
        
        except:
            return ""
    except:
        return ""


def check_amount(mynewjson):
    try:
        return mynewjson["total_funding_amount"]["amount"]
    
    except:
        return "0"
    

def check_currency(mynewjson):
    try:
        return mynewjson["total_funding_amount"]["currency_code"]
    
    except:
        return "0"
    
    
def check_contact_name(mynewjson):
    try:
        return mynewjson["contact_info"]["contact_person"]
    
    except:
        return ""
    

def check_email(mynewjson):
    try:
        return mynewjson["contact_info"]["email"]
    
    except:
        return ""
    
    
def check_phone(mynewjson):
    try:
        return mynewjson["contact_info"]["phone"]
    
    except:
        return "0"
    
def check_last_modified(mynewjson):
    try:
        return mynewjson["last_modified"]["date"]
    except:
        return ""
        
        
        
data_base_with_projects = []

for i in id_list:
    
    mynewjson = json.loads(requests.get("https://api.cristin.no/v2/projects/"+str(i)).text)
    
    print(i)
    my_final_json = {}
    my_final_json = {"id": mynewjson["cristin_project_id"],
                    "publishable": mynewjson["publishable"],
                    "published": mynewjson["published"],
                    "title": tryness(mynewjson,"title"),
                    "main_language" : mynewjson["main_language"],
                    "start_date" : mynewjson["start_date"][0:10],
                    "end_date" : mynewjson["end_date"][0:10],
                    "status": mynewjson["status"],
                    "last_modified": check_last_modified(mynewjson)[0:10],
                    "coordinating_institution": filter_institution_name(mynewjson),
                    "department": filter_department_name(mynewjson),
                    "manager_id": mynewjson["participants"][0],
                    "manager_id": mynewjson["participants"][0]["cristin_person_id"],
                    "manager_name": mynewjson["participants"][0]["first_name"],
                    "manager_surname": mynewjson["participants"][0]["surname"],
                    
                    "participant1_name" : check_participants(mynewjson,1)[0],
                    "participant1_surname" : check_participants(mynewjson,1)[1],
                    "participant1_id": check_participants(mynewjson,1)[2],
                    
                    "participant2_name" : check_participants(mynewjson,2)[0],
                    "participant2_surname" : check_participants(mynewjson,2)[1],
                    "participant2_id": check_participants(mynewjson,2)[2],
                    
                    "participant3_name" : check_participants(mynewjson,3)[0],
                    "participant3_surname" : check_participants(mynewjson,3)[1],
                    "participant3_id" : check_participants(mynewjson,3)[2],
                    
                    
                    "participant4_name" : check_participants(mynewjson,4)[0],
                    "participant4_surname" : check_participants(mynewjson,4)[1],
                    "participant4_id" : check_participants(mynewjson,4)[2],
                    
                    
                    "participant5_name" : check_participants(mynewjson,5)[0],
                    "participant5_surname" : check_participants(mynewjson,5)[1],
                    "participant5_id" : check_participants(mynewjson,5)[2],
                    
                    
                    
                    "participant6_name" : check_participants(mynewjson,6)[0],
                    "participant6_surname" : check_participants(mynewjson,6)[1],
                    "participant6_id": check_participants(mynewjson,6)[2],
                    
                    "participant7_name" : check_participants(mynewjson,7)[0],
                    "participant7_surname" : check_participants(mynewjson,7)[1],
                    "participant7_id": check_participants(mynewjson,7)[2],
                    
                    "participant8_name" : check_participants(mynewjson,8)[0],
                    "participant8_surname" : check_participants(mynewjson,8)[1],
                    "participant8_id" : check_participants(mynewjson,8)[2],
                    
                    
                    "participant9_name" : check_participants(mynewjson,9)[0],
                    "participant9_surname" : check_participants(mynewjson,9)[1],
                    "participant9_id" : check_participants(mynewjson,9)[2],
                    
                    
                    "participant10_name" : check_participants(mynewjson,10)[0],
                    "participant10_surname" : check_participants(mynewjson,10)[1],
                    "participant10_id" : check_participants(mynewjson,10)[2],
                    
                    
                    "project_category1" : check_category(mynewjson,0),
                    "project_category2" : check_category(mynewjson,1),
                    "project_category3" : check_category(mynewjson,2),
                    "project_category4" : check_category(mynewjson,3),
                    "project_category5" : check_category(mynewjson,4),
                    
                    
                    "academic_discipline1" : check_discipline(mynewjson,0),
                    "academic_discipline2" : check_discipline(mynewjson,1),
                    "academic_discipline3" : check_discipline(mynewjson,2),
                    "academic_discipline4" : check_discipline(mynewjson,3),
                    "academic_discipline5" : check_discipline(mynewjson,4),
                    
                    "keyword1" : check_keyword(mynewjson,0),
                    "keyword2" : check_keyword(mynewjson,1),
                    "keyword3" : check_keyword(mynewjson,2),
                    "keyword4" : check_keyword(mynewjson,3),
                    "keyword5" : check_keyword(mynewjson,4),
                    
                    "summary": check_summary(mynewjson),
                    
                    
                    "funding1": check_funding(mynewjson,0),
                    "funding2": check_funding(mynewjson,1),
                    "funding3": check_funding(mynewjson,2),
                    "funding4": check_funding(mynewjson,3),
                    "funding5": check_funding(mynewjson,4),
                    
                    "amount": check_amount(mynewjson),
                    "currency": check_currency(mynewjson),
                    
                    "contact name": check_contact_name(mynewjson),
                    "contact_email": check_email(mynewjson),
                    
                    "contact_phone": check_phone(mynewjson)
                    
                    
                    
                    
                    


                    
                    
                    
                    
                    
            
                    
                    
                    

                    
                    }
    
    if my_final_json["coordinating_institution"] == "Norwegian University of Science and Technology":                 
        data_base_with_projects.append(my_final_json)



import json
print("holaaa")
with open('C:/Users/Marco/Documents/nuevacarp/myjson.json', 'w', encoding='utf-8') as f:
    json.dump(data_base_with_projects, f,ensure_ascii=False)
    