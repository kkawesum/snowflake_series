import snowflake.connector

cnn = snowflake.connector.connect(
    user='kkism07',
    password = 'Xanthis@07',
    account = 'mkacjod-xr06564'
    )

cs = cnn.cursor()
try:
    cs.execute('select current_version()')
    row = cs.fetchone()
    print('connector version',row[0])
    print('creating objects')
    sql = 'CREATE WAREHOUSE IF NOT EXISTS project_warehouse'
    cs.execute(sql)
    sql = 'CREATE DATABASE IF NOT EXISTS project_database'
    cs.execute(sql)
    sql= 'USE DATABASE project_database'
    cs.execute(sql)
    sql = 'CREATE SCHEMA IF NOT EXISTS project_schema'
           
    print('DDL done..')
    cs.execute(sql)
    print('start DML')
    
    sql = 'CREATE OR REPLACE TABLE project_database.project_schema.project_comments ( ID integer, comments string)'
    cs.execute(sql)
    sql = "Insert Into project_database.project_schema.project_comments (ID, comments) Values (777,'MYCOMMENTS')"

    cs.execute(sql)
    cs.execute("SELECT * FROM project_database.project_schema.project_comments")
    row=cs.fetchone()
    print('Row 1 :',row)
    print('done')

    
    
finally:
    cs.close()
cnn.close()
