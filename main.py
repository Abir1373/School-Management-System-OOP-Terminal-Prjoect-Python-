from school import School 
from person import Student , Teacher 
from subject import Subject 
from classroom import ClassRoom 

school = School('ABC' , "Dhaka")

# Adding classroom

eight = ClassRoom('Eight')
nine = ClassRoom('Nine')
ten = ClassRoom('Ten')

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

#Adding student

abir = Student('Abir',eight)
tajwar = Student('Tajwar',nine)
sami = Student('sami',ten)
tamim = Student('Tamim',ten)


school.student_admission(abir)
school.student_admission(tajwar)
school.student_admission(sami)
school.student_admission(tamim)

# Adding teachers 

moni = Teacher('Moni')
jahid = Teacher('Jahid')
ebrahim = Teacher('Ebrahim')

# Adding Subjects

bangla = Subject('Bangla',moni)
physics = Subject('Physics',jahid)
chemistry = Subject('Chemistry',ebrahim)
biology = Subject('Biology',ebrahim)


eight.add_subject(bangla)
nine.add_subject(bangla)
ten.add_subject(bangla)

nine.add_subject(physics)
ten.add_subject(physics)

nine.add_subject(chemistry)
ten.add_subject(chemistry)

nine.add_subject(biology)
ten.add_subject(biology)

eight.take_semester_final_exam()
nine.take_semester_final_exam()   
ten.take_semester_final_exam()
print(school)