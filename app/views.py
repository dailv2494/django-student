from django.shortcuts import render,redirect
from . import  db

# students = [
#     {"id": 1, "name": "Student 1", "studentNo": "1001"},
#     {"id": 2, "name": "Student 2", "studentNo": "1002"}
# ]
def index(request):
    context = {'students' : db.getAllStudents()}
    return render(request, 'index.html', context)
def createStudent(request):
    if request.method=='POST':
        studentNo=request.POST['studentNo']
        name=request.POST['name']
        db.createStudent(studentNo, name)
        return redirect('home')

    return render(request,'student_form.html')#sau khi update tra ve form
def updateStudent(request,id):
    st=db.getStudentById(id)
    studentNo=st.studentNo
    name=st.name
    if request.method=='POST':
        studentNo=request.POST['studentNo']
        name=request.POST['name']
        db.updateStudent(id,studentNo,name)
        return redirect('home')

    return render(request,'student_form.html',
                  {'studentNo':studentNo,'name':name})#sau khi update tra ve form html
def deleteStudent(request,id):
    db.deleteStudent(id)
    return redirect('home')#