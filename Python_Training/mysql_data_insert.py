try:
    import mysql.connector
    from datetime import *

    time=datetime.now()
    mycustom = time.strftime("%Y-%m-%d %H:%M:%S")


    mydb= mysql.connector.connect(host="192.168.0.150",user="mysql_user",password="test123",database="alnafi")
    ###mysql connection object create
    cur = mydb.cursor()

    '''
    ###Fetching data
    #sql = """ select * from trainer_details """
    ###Executing
    cur.execute(sql)
    result = cur.fetchall()
    #result = cur.fetchone()
    for row in result:
        print(row)
    '''

    '''
    ###Fetching data
    sql = """ insert into trainer_details (fname,lname,desig,username,password,salary,datetime) values ('Yousuf','Ali','Businessman','Yousuf','ramzan123',900000,'2022-10-02') """
    ###Executing
    cur.execute(sql)
    mydb.commit()
    print("Data has been inserted")
    '''

    '''
    ###Fetching data
    sql = """ insert into trainer_details (fname,lname,desig,username,password,salary,datetime) values (%s,%s,%s,%s,%s,%s,%s) """
    data = ('rehan','pathan','POS','rehan','rehan123','75000',mycustom)
    ###Executing
    cur.execute(sql,data)
    ###For Inserting
    mydb.commit()
    print("Data has been inserted")
    '''

    '''
    data="'zoya@855'"
    sql= " update trainer_details set password="+data+" where t_id=11 "
    ###Executing
    cur.execute(sql)
    ###For Inserting
    mydb.commit()
    print("Data has been inserted")
    '''

    mydata= input("Enter the fname which you want to remove from mysql: ")
    sql= "delete from trainer_details where fname = '"+mydata+"'"
    ###Executing
    cur.execute(sql)

    ###For Inserting
    mydb.commit()
    print("Your command was Successful")

    #Fetching mysql Data
    select_sql="""select * from trainer_details """
    cur.execute(select_sql)
    result = cur.fetchall()
    for row in result:
        print(row)

    mydb.close()

except Exception as e:
    print("Something issue please check your input",e )
