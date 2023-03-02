import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import pandas as pd

cnn = snowflake.connector.connect(
    user='kkism07',
    password = 'Xanthis@07',
    account = 'mkacjod-xr06564',
    warehouse = 'project_warehouse',
    database = 'project_database',
    schema = 'project_schema'
    )
print('opening csv..')
df = pd.read_csv('C:\\Users\\KislayS\\Pictures\\customers-100.csv', sep =',',header=0,index_col=False)
df.reset_index(drop=True, inplace=True)
print(df.head(10))
#cs = cnn.cursor()
success, nchunks, nrows, _ = write_pandas(cnn,df,"project_tasks",quote_identifiers=False)
print(str(success)+'/'+str(nchunks)+'/'+str(nrows))
