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
    ddl_sql = 'CREATE WAREHOUSE IF NOT EXISTS project_warehouse'
    'CREATE DATABASE IF NOT EXISTS project_database'
    'USE DATABASE project_database'
    'CREATE SCHEMA IF NOT EXISTS project_schema'
    print('done')
    
finally:
    cs.close()
cnn.close()
