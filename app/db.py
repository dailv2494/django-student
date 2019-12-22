from app.models import Student
def getAllStudents():
	return Student.objects.all()

def createStudent(studentNo,name):
	return Student.objects.create(
		studentNo=studentNo,
		name=name
	)

def getStudentById(id):
	return  Student.objects.get(id=id)


def updateStudent(id,studentNo,name):
	st=getStudentById(id)
	st.studentNo=studentNo
	st.name=name
	st.save()
	return st
def deleteStudent(id):
	st=getStudentById()
	if st:
		st.delete()
#python manage.py shell
#st1=createStudent('1001','Student 1')
#st2=createStudent('1002','Student 2')
#st3=createStudent('1003','Student 3')

#students = getAllStudents()
#st1 = getStudentById(1)
#st1.name
#updateStudent(1,'1001','student 1 new1')
#st1=getStudentById(1)
