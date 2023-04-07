#Dictionaries are the one which are used to store data through keywords and these can be of integers characters and strings...!
Rollno={
   "A2112651001":"Balu Karthik",
   "A2112651002":"Sai Kiran",
   "A2112651014":"Bobby",
   "A2112651015":"Ravi varma",
   "A2112651024":"Easwer",
   "A2112651027":"Karthik",
   "A2112651054":"Komal",
   33:"hello"
}
print(Rollno)
print(Rollno["A2112651001"])
print(Rollno.get(33,"INVALID"))#Returns the string if not found
print(Rollno.get("A21126510019","Invalid key"))
"""{'A2112651001': 'Balu Karthik', 'A2112651002': 'Sai Kiran', 'A2112651014': 'Bobby', 'A2112651015': 'Ravi varma', 'A2112651024': 'Easwer', 'A2112651027': 'Karthik', 'A2112651054': 'Komal', 33: 'hello'}
Balu Karthik
hello
Invalid key"""