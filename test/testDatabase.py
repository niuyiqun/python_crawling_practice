# -*- codeing = utf-8 -*-
# @Time : 2020/10/18 14:45
# @Author : niu
# @File : testDatabase.py
# @Software: PyCharm

import pymysql

# sql1='''
    #     create table if not exists person
    #     (
    #     id int,
    #     name varchar(30),
    #     age int,
    #     sex char(2)
    #     );
    # '''    #创建新的数据表
    #
    # # c.execute(sql1)
    # # c.execute("insert into person (id,name,age,sex) values (1,'小明',15,'男')")
    # # db.commit()
    #
    # sql='''
    #     select * from person ;
    # '''
    # c.execute(sql)
    # print(c.rowcount)     #查看拿到的数据的行数
    #
    # row=c.fetchone()
    #
    # while row:
    #     print(row)
    #     row=c.fetchone()

def insert(c,id,name,age,sex):
    sql='''
        insert into person (id,name,age,sex) values ({id},{name},{age},{sex})
    '''.format(id=id,name=name,age=age,sex=sex)
    c.execute(sql)
if __name__ == '__main__':
    db = pymysql.connect(host='localhost', user='root', password='nyq20010324', db='test000', port=3306)

    cursor=db.cursor()
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print("版本号",data)
    c=db.cursor()



    db.close()