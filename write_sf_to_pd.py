import snowflake.connector
import pandas as pd

cnn = snowflake.connector.connect(
    user='kkism07',
    password = 'Xanthis@07',
    account = 'mkacjod-xr06564',
    warehouse = 'project_warehouse',
    database = 'project_database',
    schema = 'project_schema'
    )

cs = cnn.cursor()
sql = 'select * from project_tasks'
cs.execute(sql)
df = cs.fetch_pandas_all()
cs.close()
cnn.close()
print(df.head(10))
