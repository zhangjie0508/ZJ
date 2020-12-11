# -*- coding: utf-8 -*-
#第三次修改
#不能判断宿舍是否住满四人
#交换宿舍功能单人交换不能判断输入宿舍是否在该性别中存在并没住满四人；双人交换不能判断性别是否相同并相互交换宿舍。
import json
import random

filename = 'student.json'
students_all = {}
dorm = {"man":[100,101,102],"woman":[200,201,202]}


def main():
    global students_all
    # 将文件内容读入一个变量中
    fd = open(filename, 'r', encoding='utf-8')
    file_data = fd.read()
    # 将内容转为json对象，保存到students_all中
    try:
        students_all = json.loads(file_data)
        print(students_all)
    except:
        print("无学生信息")
    while True:
        menum()
        try:
          choice = int(input('请选择：'))
        except:
          continue
        if not choice in [0, 1, 2, 3, 4, 5,6]:
            print("输入错误，请重新输入")
            continue
        if choice == 0:
            answer = input('你确定要退出系统吗？y/n')
            if answer.upper() == 'Y':
                print('谢谢你的使用！')
                break  # 结束循环，退出系统
            else:
                continue
        elif choice == 1:
            insert()  # 录入学生信息
        elif choice == 2:
            search()  # 查找学生信息
        elif choice == 3:
            delete()  # 删除学生信息
        elif choice == 4:
            modify()  # 修改学生信息
        elif choice == 5:
            show()  # 显示学生信息
        elif choice == 6:
             adjdorm() #交换宿舍

# 主菜单
def menum():
    print("----------宿舍管理系统----------")
    print("----------功能菜单-------------")
    print("         1.录入学生信息         ")
    print("         2.查找学生信息         ")
    print("         3.删除学生信息         ")
    print("         4.修改学生信息         ")
    print("         5.显示学生信息         ")
    print("         6.更换宿舍            ")
    print("         0.退出系统            ")
    print("-----------------------------")
def keyboard_input(t,_prompt):
    while True:
        v = input(_prompt)
        if type(t)== type(1):
          try:
              v =int(v)
          except:
              print('输入无效，不是整数类型，请重新输入')
              continue
        break
    return v
# 录入学生信息功能
def insert():
    global  students_all
    while True:
        id = keyboard_input(1,"请输入学号（如1001）：")
        if str(id) in students_all:
            print('该学号已存在，请重新输入！')
            continue
        age =keyboard_input(1,'请输入年龄：')
        name = keyboard_input("",'请输入姓名：')
        while True:
              sex = keyboard_input("",'请输入性别：')
              if sex not in ('男', '女'):
                  print('输入无效，请重新输入男/女')
                  continue
              break
        q= input('输入1自动分配，手动分配回车：')
        if q == '1':
            dorm=dorm_self(sex)
        else:
            dorm=dorm_manual(sex)
        stu = {'学号': str(id), '姓名': name, '性别': sex, '年龄': age, '宿舍号': dorm}  # 将录入的学生信息保存到字典
        students_all[str(id)] = stu  # 将学生信息字典添加到列表中
        answer = input('是否继续添加？Y/n\n')
        if answer.upper() == 'Y':
            continue
        break  # 结束循环
    save()  # 调用save方法存储学生信息
    print('学生信息录入完毕')

#判断宿舍是否住满
def qs(dorm):
    count = 0
    for id in students_all:
        if students_all[id]['宿舍号'] == dorm:
            count +=1
    if count >=4:
        return True
    return False
#自动分配宿舍
def dorm_self(sex):
    while True:
        count=0
        if sex == '男':
            dorm=str(random.randint(100,102))
        if sex =='女':
            dorm = str(random.randint(200, 202))
        for id in students_all:
            if students_all[id]['宿舍号'] == dorm:
                count = count + 1
        if count >= 4:
            continue
        return dorm
#宿舍手动分配
def dorm_manual(sex):
    while True:
        count = 0
        dorm = int(input('请输入宿舍号：'))
        if sex == '男':
            if dorm not in range(100,103):
                print('输入有误，请重新输入：')
                continue
        if sex == '女':
            if dorm not in range(200, 203):
                print('输入有误，请重新输入：')
                continue
        return dorm
#保存信息
def save():
    stu_txt = open(filename, 'w', encoding='utf-8')  # 打开文件，w写入模式
    stu_txt.write(json.dumps(students_all, ensure_ascii=False))
    stu_txt.close()  # 关闭文件


# 查找学生信息
def search():
    global students_all
    stu={}
    while True:
        students_lst = []
        mode = int(input('按学号查找请输入1，按宿舍号查找请输入2：'))
        if mode == 1:
            id = int(input('请输入学号：'))
            if str(id) in students_all:
                stu = students_all[str(id)]
                students_lst.append(stu)
        elif mode == 2:
            dorm = int(input('请输入宿舍号：'))
            for id in students_all:
                stu = students_all[id]
                if stu["宿舍号"] == dorm:
                    students_lst.append(stu)
        else:
            print('你的输入有误，请重新输入！')
            continue
        show_student(students_lst)
        anser = input('是否要继续查询？y/N\n')
        if anser.upper() == 'Y':
            continue
        else:
            break

def show_student(lst):
    format_title = '{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}'
    print(format_title.format('学号', '姓名', '性别', "年龄", '宿舍号'))
    # 定义内容的显示格式
    format_date = '{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}'
    for item in lst:
        print(format_date.format(item.get('学号'),
                                 item.get('姓名'),
                                 item.get('性别'),
                                 item.get('年龄'),
                                 item.get('宿舍号')))

# 删除学生信息
def delete():
    while True:
        id = input('请输入要删除的学生的学号:')
        try:
            if id != '': # 如果输入的学号不为空
              students_all.pop(id)
              print('该学生信息已删除')
              save()
        except:
            print('无该学生信息，请重新输入学号')
            continue
        answer = input('是否继续删除？y/N\n')
        if answer.upper() == 'Y':
            continue  # 继续删除信息
        else:
            break  # 退出循环

# 修改学生信息
def modify():
    global students_all
    stu={}
    while True:
        students_lst = []
        id = input('请输入要修改的学生学号：')
        if str(id) not in students_all:
            print("查无此人，请重新输入")
        else:
            stu = students_all[id]
            try:
                v = input('请输入姓名：')
                if v != '':
                    stu["姓名"] = v
                v = input('请输入性别：')
                if v not in ('男', '女'):
                    print('输入无效，请重新输入男/女')
                    continue
                if v != '':
                    stu['性别'] = v
                v = input('请输入年龄：')
                if v != '':
                    stu['年龄'] = int(v)
                v = input('请输入宿舍号：')
                if v != '':
                    stu['宿舍号'] = int(v)
                students_all[id]=stu
                save()
            except:
                print('你的输入有错误，请重新输入！')
                continue
        print('修改成功！')
        break
    answer = input('是否继续修改其他学生信息？y/N')
    if answer.upper() == 'Y':
        modify()
# 显示学生信息
def show():
    global students_all
    fd = open(filename, 'r', encoding='utf-8')
    file_data = fd.read()
    try:
        students_all = json.loads(file_data)
    except:
        print("无学生信息")
    # print(students_all)
    list = []
    for key in students_all:
        list.append(students_all[key])
    show_student(list)

#交换宿舍
def adjdorm():
    mod = int(input('单人调换宿舍请输入1，双人调换宿舍请输入2：'))
    if mod == 1:
        # id = args[0]
        # dorm = args[1]
        while True:
            id=input('请输入学号：')
            if str(id) not in students_all:
                print("查无此人，请重新输入")
                continue
            dorm=input('请输入要调换的宿舍号：')
            try:
                qs = students_all[id]['宿舍号']

                if dorm != qs:
                    print('修改成功！')
                    students_all[id]['宿舍号'] = dorm
                    save()
                    return
            except:
                print("信息有误")
                return
    elif mod == 2:
        while True:
            ida=input('请输入第一个学生学号')
            if str(ida) not in students_all:
                print("查无此人，请重新输入")
                continue
            idb=input('请输入第二个学生学号')
            if str(idb) not in students_all:
                print("查无此人，请重新输入")
                continue
    else:
        print('输入错误，请重新输入')


if __name__ == '__main__':  # 以主函数方式运行
    main()  # 调用main
