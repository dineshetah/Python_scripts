import pandas as pd 
from sqlalchemy import create_engine

db_connection_str = 'mysql+pymysql://user:Dinesh@123@localhost/amabhoomi'

engine = create_engine(db_connection_str)  # create a SQLAlchemy engine

file_path = 'D:\amabhoomi\multiple_xlsx_in_dbtable.py'
xlsx_File =pd.ExcelFile(file_path)
print(xlsx_File)

