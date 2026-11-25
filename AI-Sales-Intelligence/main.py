company=" ABC Company"
industry=" Landescaping"
location="Texas"
employees= 25
website="www.google.com"
company_size= "small"
has_website= True


def display_company_info():
    
    print("Company name is=", company)
    print("Industry is=",industry)
    print("Location is=",location)
    print("employees are",employees)
    print("website is ",website)
    
display_company_info()

if employees >=20:
    print("Lead is potentially :HIGHT")
else:
    print("Lead potentially is : Low")
    
def calculate_lead_score(employees,industrym,location,has_website):
    score = 0

    if employees >=20:
        score += 50
    
    if industry==" Landescaping":
        score +=50
    if location== "Texas":
        score +=20
    if has_website:
        score+=30
        
    return score

lead_score = calculate_lead_score(employees,industry,location,has_website)
print("Lead score",lead_score)








   
    
    
    