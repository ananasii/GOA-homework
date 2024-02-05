name = "ana"
#name არის ცვლადი
# = არის ცვლადისთვის მნიშ
# "ana" არის ცვლადისთვის მნიშვნელობა

surname = "tkemaladze"

# print(name)
#პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიქტი

name = "ana" #ეს არის str (string) ტიპის ცვლადი
age = "13" # ეს არის int ( integer ) მთელი რიცხვი
height = "153" #ეს არის float ტიპის ცვლადი ( ათწილადი )
#boolean (bool) ტიპის ცვლადი

knows_programming = False #True ან False
is_ugly = False 

isUgly = False # ჯავასკრიპტული camelcase

print(name + " " + surname)


#სტრინგი არის ბრჭრალებში მოქცეული
# print(name + age)

# print(type(age))
# print(type(name))
# print(type(surname))
# print(type(height))
# print(type(knows_programming))

print(name + str(age))
      

print(("hello, I am") + " " + str(name) + " " + str(surname) + (". I am") + " " + str(age) + " " + ("years old.") + " " + ("Do I know programming? The answer is :") + " " + str(knows_programming))