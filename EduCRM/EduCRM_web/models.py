from django.db import models

# Create your models here.


# 抽象类表
class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# 成绩类
class Results(BaseModel):
    student_name = models.CharField(max_length=30,null=False)
    classes_name = models.CharField(max_length=30,null=False)
    mid_term_written = models.CharField(max_length=30,null=True)
    mid_term_machine = models.CharField(max_length=30,null=True)
    mid_term_mean = models.CharField(max_length=30,null=True)
    end_written = models.CharField(max_length=30,null=True)
    end_machine = models.CharField(max_length=30,null=True)
    end_mean = models.CharField(max_length=30,null=True)
    student_id = models.CharField(max_length=30,null=False)

# 学生考勤
class AttendanceStudent(BaseModel):
    student_name = models.CharField(max_length=30)
    professional_name = models.CharField(max_length=30)
    classes_name = models.CharField(max_length=30)
    discipline_name = models.CharField(max_length=30,null=True)
    discipline_date = models.CharField(max_length=30,null=True)
    note = models.CharField(max_length=255,null=True)
    should_day = models.CharField(max_length=30)
    actual_day = models.CharField(max_length=30)


# 老师考勤
class AttendanceTeacher(BaseModel):
    teacher_name = models.CharField(max_length=30)
    professional_name = models.CharField(max_length=30)
    classes_name = models.CharField(max_length=30)
    discipline_name = models.CharField(max_length=30,null=True)
    discipline_date = models.CharField(max_length=30,null=True)
    note = models.CharField(max_length=255,null=True)
    should_day = models.CharField(max_length=30)
    actual_day = models.CharField(max_length=30)

# 积分商城
class IntegralMall(BaseModel):
    shop = models.CharField(max_length=30)
    score = models.IntegerField()
    inventory = models.IntegerField()
    price = models.DecimalField(max_digits=7,decimal_places=2,)
    image_url = models.CharField(max_length=255)
    is_activation = models.CharField(max_length=30)


# 信息通知
class MessageNotice(BaseModel):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255,null=True)
    is_activation = models.CharField(max_length=2,default=1)  #0=否 1=是；默认1

# 缴费项目
class PaymentProject(BaseModel):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    note = models.CharField(max_length=255)
    is_activation = models.CharField(max_length=2,default=1) #0=否 1=是；默认1


# 方向表
class Professional(BaseModel):
    professional_name = models.CharField(max_length=30)

# 老师表
class Teacher(BaseModel):
    teacher_name = models.CharField(max_length=30)
    id_card = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    work_number = models.IntegerField(auto_created=100000)  #从100000开始自增 试
    password = models.CharField(max_length=255,default='')
    email = models.CharField(max_length=30,null=True)
    phone = models.CharField(max_length=30,null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=30,null=True)
    is_activation = models.CharField(max_length=5,default=1) #0=否 1=是；默认1
    professional = models.ForeignKey(Professional,on_delete=models.SET_NULL,null=True,blank=True)

# 通讯录表
class AddressBook(BaseModel):
    contact = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    note = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, null=True)
    qq = models.CharField(max_length=20, null=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True,blank=True)

# 班级表
class Classes(BaseModel):
    classes_Name = models.CharField(max_length=30)
    class_number = models.CharField(max_length=30)
    professional = models.ForeignKey(Professional,on_delete=models.SET_NULL,null=True,blank=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True,blank=True)

# 课程表
class Course(BaseModel):
    course_name = models.CharField(max_length=30)
    professional = models.ForeignKey(Professional,on_delete=models.SET_NULL,null=True,blank=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True,blank=True)

# 家长表
class Parents(BaseModel):
    parents_name  = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=255)
    id_card = models.CharField(max_length=30)
    integral_score = models.IntegerField(default=0)
    is_activation = models.CharField(max_length=5,default=1) #0=否 1=是；默认1

# 学生表
class Student(BaseModel):
    student_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    id_card = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    is_activation = models.CharField(max_length=30,default=1) #0=否 1=是；默认1
    parents = models.ForeignKey(Parents,on_delete=models.SET_NULL,null=True,blank=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True,blank=True)
    classes = models.ForeignKey(Classes,on_delete=models.SET_NULL,null=True,blank=True)
    Professional = models.ForeignKey(Professional,on_delete=models.SET_NULL,null=True,blank=True)


# 缴费记录
class PaymentRecords(BaseModel):
    payment_project_id = models.CharField(max_length=30)
    detail = models.CharField(max_length=255)
    parents = models.ForeignKey(Parents,on_delete=models.SET_NULL,null=True,blank=True)


# 积分兑换记录表
class IntegralRecord(BaseModel):
    mall_id = models.CharField(max_length=30)
    parents = models.ForeignKey(Parents,on_delete=models.SET_NULL,null=True,blank=True)


# 家长留言
class ParentsMessage(BaseModel):
    parents_name = models.CharField(max_length=30)
    content = models.CharField(max_length=255)
    anonymous = models.CharField(max_length=30,default=0) #0=否 1=是；默认0
    parents = models.ForeignKey(Parents,on_delete=models.SET_NULL,null=True,blank=True)


