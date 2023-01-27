import json
employee = {
   "employee": [

      {
         "name": "kumaran",
         "DOB": "28-07-2022",
         "height": "7",
         "city":"banglore",
         "state":"kartnaka"
      },

      {
         "name": "rajesh",
         "DOB": "24-07-2022",
         "height": "10",
         "city":"chennai",
         "state":"tamilnadu"
      },
      
      {
        "name": "vicky",
        "DOB": "26-07-2022",
        "height": "10",
        "city":"surat",
        "state":"gujarat"
       },
      
      {
       "name": "ganesh",
       "DOB": "21-07-2022",
       "height": "12",
       "city":"hyderbad",
       "state":"telgana"
       },
       
       {
        "name": "selvan",
        "DOB": "23-07-2022",
        "height": "14",
        "city":"tirupathi",
        "state":"Andhra pradesh"
        }
       
     ]
   }
   
with open("employee.json","w") as f:
    json.dump(employee,f,indent=4)
    print("sucessfully")
    
    
#Write a python program that reads this information from the JSON file and save    
  import json
  with open("employee.json","r") as f:
   x=json.load(f)
   print(x)
   print("list of employee" )
   
   
# Create a dictionary of any 7 Indian states and their capitals. 
  
    
  import json 
  dictionary = { 
      "dictionary": [ 
    {
     "state": "andhra pradesh", 
     "capital":"amaravati"
     },
    
    {
     "state": "arunchala", 
     "capital":"itanagar"
     },
    
    {
     "state": "assam", 
     "capital":"dispur"
     },
    
    {
     "state": "bihar", 
     "capital":"patma"
     },
    
    {
     "state": "gujarat", 
     "capital":"gandhinagar"
     },
    
    {
     "state": "kartnaka", 
     "capital":"bengalaru"
     }
     
    
    ]  
  } 
    
  json_object = json.dumps(dictionary, indent = 4) 
  print(json_object)  