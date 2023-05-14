#!/usr/bin/env python
# coding:utf-8
"""
file:Management.py
date:9/9/179:57 PM
author:hx
desc:管理系统雏形
"""
##添加模块
import sys
import json


##学校类定义
class School(object):
    ##初始化函数
    def __init__(self, SchoolName, SchoolPlace, SchoolMotto):
        self.SchoolName = SchoolName
        self.SchoolPlace = SchoolPlace
        self.SchoolMotto = SchoolMotto

    ##招生函数
    def RecruitStu(self):
        NewStuName = raw_input("StuName:")
        NewStuAge = raw_input("StuAge:")
        NewStuSex = raw_input("StuSex:")
        NewStuSchool = raw_input("StuSchool:")
        CourseNo = raw_input("CourseNo:")
        NewStuID = raw_input("StuID:")
        CoursePrice = raw_input("CoursePrice:")
        NewStu = Stu(NewStuName, NewStuAge, NewStuSex, NewStuSchool, CourseNo, NewStuID, CoursePrice)  ##实例化学员对象
        stus_dict = {"StuName": NewStuName, "StuAge": NewStuAge, "StuSex": NewStuSex, "StuSchool": NewStuSchool,
                     "CourseNo": CourseNo, "StuID": NewStuID, "CoursePrice": CoursePrice}  # 用字典来存放讲师信息
        self.method_name(NewStuName, stus_dict)
        NewStu.StuInfo()

    def method_name(self, NewStuName, stus_dict):
        if not dic:
            dic[NewStuName] = stus_dict
            json.dump(dic, open("student_db", "w"), encoding='utf-8', ensure_ascii=False, indent=2)
        else:
            if dic.get(NewStuName):
                print("%s学生已存在,不能注册名字相同的学生" % NewStuName)
            else:
                dic[NewStuName] = stus_dict
                json.dump(dic, open("student_db", "w"), encoding='utf-8', ensure_ascii=False, indent=2)
        print("The student has already added successfully".center(50, '-'))

    ##聘请讲师
    def HireTch(self):
        print(
        "Welcome to hire teacher from here~")
        NewTeacherName = raw_input("Please input the teacher's name:")
        NewTeacherAge = raw_input("Please input the teacher's age:")
        NewTeacherSex = raw_input("Please input the teacher's sex:")
        NewCourseNo = raw_input("Please input the teacher's course number:")
        NewSalary = raw_input("Please input the teacher's salary:")
        NewTeacher = Teacher(NewTeacherName, NewTeacherAge, NewTeacherSex, NewCourseNo, NewSalary)  # 实例化讲师对象
        teachers_dict = {"TeacherName": NewTeacherName, "TeacherAge": NewTeacherAge, "TeacherSex": NewTeacherSex,
                         "CourseNo": NewCourseNo, "Salary": NewSalary}  # 用字典来存放讲师信息
        # 通过json将讲师的字典反序列化到dic字典中
        if not dic:  # 字典如果为空
            dic[NewTeacherName] = teachers_dict  # 将讲师名与讲师对象相关联
            # 通过json将讲师的字典序列化到teacher_db文件中
            json.dump(dic, open("teacher_db", "w"), encoding='utf-8', ensure_ascii=False, indent=2)
        else:  # 如果文件中已有讲师信息
            if dic.get(NewTeacherName):  # 字典中不存在key，则返回none,不报错
                print("%s讲师已存在,不能创建名字相同的讲师" % NewTeacherName)
            else:
                dic[NewTeacherName] = teachers_dict
                json.dump(dic, open("teacher_db", "w"), encoding='utf-8', ensure_ascii=False, indent=2)
        NewTeacher.TeacherInfo()  ##将新老师的信息打印在屏幕上

    ##新增课程
    def CreateCourse(self):
        print
        "Welcome to create course!"
        NewCourseNo = raw_input("CourseNo:")
        NewCourseName = raw_input("CourseName:")
        NewCoursePrice = raw_input("CoursePrice:")
        NewCourse = Course(NewCourseNo, NewCourseName, NewCoursePrice)  ##新创建的对象直接实例化
        courses_dict = {"CourseNo": NewCourseNo, "CourseName": NewCourseName,
                        "CoursePrice": NewCoursePrice}  # 用字典来存放讲师信息
        if not dic:
            dic[NewCourseNo] = courses_dict
            json.dump(dic, open("course_db", "w"), encoding='utf-8', ensure_ascii=False, indent=2)
        else:
            if dic.get(NewCourseNo):
                print("%s课程已存在,不能注册课程号相同的课程" % NewCourseNo)
            else:
                dic[NewCourseNo] = courses_dict
                json.dump(dic, open("course_db", "w"), encoding='utf-8', ensure_ascii=False, indent=2)
        print("Course has already created successfully".center(50, '-'))
        print("""
        CourseNo:%s
        CourseName:%s
        CoursePrice:%s""" % (NewCourseNo, NewCourseName, NewCoursePrice))


class Teacher(object):
    def __init__(self, TeacherName, TeacherAge, TeacherSex, CourseNo, Salary):
        self.TeacherName = TeacherName
        self.TeacherAge = TeacherAge
        self.TeacherSex = TeacherSex
        self.CourseNo = CourseNo
        self.Salary = Salary

    def TeachKnowledge(self):
        print
        "Teach Knowlege~"

    def TeacherInfo(self):
        print("""
        -------------讲师信息-------------
        Name:%s
        Age:%s
        Sex:%s
        CourseNo:%s
        Salary:%s
        """ % (self.TeacherName, self.TeacherAge, self.TeacherSex, self.CourseNo, self.Salary))


##课程类定义
#TODO:doing now ,to do next
class Course(object):
    def __init__(self, CourseNo, CourseName, CoursePrice):
        self.CourseNo = CourseNo
        self.CourseName = CourseName
        self.CoursePrice = CoursePrice

    def ShowCourseInfo(self):
        print("""
        CourseNO:%s
        CourseName:%s
        CoursePrice:%s""" % (self.CourseNo, self.CourseName, self.CoursePrice))


##学员类定义
#TODO(danms):Remove me after icehouse
class Stu(object):
    def __init__(self, StuName, StuAge, StuSex, StuSchool, CourseNo, StuID, CoursePrice):
        self.StuName = StuName
        self.StuAge = StuAge
        self.StuSex = StuSex
        self.StuSchool = StuSchool
        self.CourseNo = CourseNo
        self.StuID = StuID
        self.CoursePrice = CoursePrice

    def Study(self):
        print
        "study"

    def PayMoney(self):
        print
        "Paying for money~"

    def StuInfo(self):
        print("""
                ---------------学生信息--------------
                Name:%s
                Age:%s
                Sex:%s
                School:%s
                CourseNo:%s
                ID:%s
                CoursePrice:%s
                """ % (
        self.StuName, self.StuAge, self.StuSex, self.StuSchool, self.CourseNo, self.StuID, self.CoursePrice))


def students_view():  # 学员视图
    while True:
        pro = """
        1.欢迎注册
        2.返回
        3.退出
        请选择:
        """
        num = raw_input(pro)
        if num == '1':
            choice_school_obj.RecruitStu()  # 调用学生注册方法并生成学生对象
        elif num == '2':
            break
        elif num == '3':
            sys.exit()
        else:
            continue


def teacher_view():  # 讲师视图
    name = raw_input("请输入讲师姓名:")
    while True:
        if dic.get(name) or teachers_dict.get(name):
            print("欢迎%s讲师".center(50, '-') % name)
        elif not dic.get(name) and not teachers_dict.get(name):
            print("%s讲师不存在" % name)
            break
        pro = """
        1.查看学员信息
        2.返回
        3.退出
        请输入你的选择:
        """
        num = raw_input(pro)
        if num == '1':
            if teachers_dict.get(name):
                teachers_dict[name].show_student()  # 查看学生信息
            else:
                print("功能未完善,只能输入lvah,cheng")
        elif num == '2':
            break
        elif num == '3':
            sys.exit()
        else:
            continue


def school_view():  # 学校视图
    while True:
        pro = """
        1.创建课程
        2.招生注册
        3.聘用讲师
        4.返回
        5.退出
        请输入你的选择:
        """
        num = raw_input(pro)
        if num == '1':
            choice_school_obj.CreateCourse()
        elif num == '2':
            choice_school_obj.RecruitStu()
        elif num == '3':
            choice_school_obj.HireTch()
        elif num == '4':
            break
        elif num == '5':
            sys.exit()
        else:
            continue


def main():
    global dic  # 全局变量
    global choice_school_obj
    dic = {}

    while True:
        print("请选择学校".center(50, '*'))
        pro1 = """
    1. %s
    2. %s
    3. 返回
    4. 退出
    请输入你的选择:
""" % (school1.SchoolName, school2.SchoolName)
        choice_school = input(pro1)
        if choice_school == '1':
            choice_school_obj = school1  # 将对象引用传给choice_school
        elif choice_school == '2':
            choice_school_obj = school2
        elif choice_school == '3':
            break
        elif choice_school == '4':
            sys.exit()
        else:
            continue
        while True:
            print("请选择视图".center(50, '*'))
            pro2 = """
        1.学员视图
        2.讲师视图
        3.学校管理视图
        4.返回
        5.退出
        请选择视图:
        """

            num = raw_input(pro2)

            if num == '1':
                print("欢迎进入学员视图".center(50, '*'))
                students_view()
            elif num == '2':
                print("欢迎进入讲师视图".center(50, '*'))
                teacher_view()
            elif num == '3':
                print("欢迎进入学校管理视图".center(50, '*'))
                school_view()
            elif num == '4':
                break
            elif num == '5':
                sys.exit()
            else:
                continue


if __name__ == '__main__':
    teachers_dict = {}
    courses_dict = {}
    stus_dict = {}

    school1 = School("A大学", "曲江校区", "祖国、荣誉、责任")  # 实例化两个学校
    school2 = School("B大学", "长安区", "爱国、求是、奋进")

    t1 = Teacher("leo", "28", "male", "01", "10000")
    t2 = Teacher("harry", "26", "female", "02", "9000")  # 实例化两个讲师
    teachers_dict["leo"] = t1
    teachers_dict["harry"] = t2
    teacher_dict = {"TeacherName": "leo", "TeacherAge": "28", "TeacherSex": "male", "CourseNo": "01", "Salary": "10000"}
    teacher_dict = {"TeacherName": "harry", "TeacherAge": "26", "TeacherSex": "female", "CourseNo": "02",
                    "Salary": "9000"}

    course1 = Course("01", "Linux云自动化运维", "12800")  # 实例化两个课程
    course2 = Course("02", "c/c++开发", "9800")
    courses_dict["01"] = course1
    courses_dict["02"] = course2
    courses_dict = {"CourseNo": "01", "CourseName": "Linux云自动化运维", "CoursePrice": "12800"}
    courses_dict = {"CourseNo": "02", "CourseName": "c/c++开发", "CoursePrice": "9800"}

    stu1 = Stu("Katy", "18", "female", "A大学", "01", "3150911026", "12800")  ##实例化两个学员
    stu2 = Stu("Betty", "18", "male", "B大学", "02", "3150911022", "12000")
    stus_dict["Katy"] = stu1
    stus_dict["Betty"] = stu2
    stu_dict = {"StuName": "Katy", "StuAge": "18", "StuSex": "female", "StuSchool": "A大学", "CourseNo": "01",
                "StuID": "3150911026", "CoursePrice": "12800"}
    stu_dict = {"StuName": "Betty", "StuAge": "18", "StuSex": "male", "StuSchool": "B大学", "CourseNo": "02",
                "StuID": "3150911022", "CoursePrice": "12000"}
    print(school1, school2)
    main()