from pack1 import karthik
questions=[
        "Q1.What is the capital of india \n a.Delhi\n b.Mumbai\n c.kolkata",
        "Q2.What is the national bird of india \n a.Peackock\n b.Butterfly\n c.None",
        "Q3.Where is statue of liberty located \n a.India\n b.Europe\n c.United states"
    ]
sol=[
     karthik(questions[0],"a"),
     karthik(questions[1],"a"),
     karthik(questions[2],"c"),
]
count=0
score=0
for x in sol:
    print(questions[count])
    ans=input("Enter the answer : ")
    if ans==x.answer:
       score=score+1
    count=count+1
print("Your score is ",score,"/3")
print("Thank U For taking test")