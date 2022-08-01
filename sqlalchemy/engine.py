from sqlalchemy import MetaData, create_engine, text, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session, registry
metadata_obj = MetaData()

engine = create_engine("sqlite+pysqlite:///:memory:",echo=True, future=True)

# with engine.begin() as conn:
#     result = conn.execute(text("CREATE TABLE some_table (x int, y int)"))
#     conn.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),[{"x": 1, "y": 1}, {"x": 2, "y": 4}])
#     conn.commit()

# with engine.connect() as conn:
#     result = conn.execute(text('SELECT x,y from some_table'))
#     print(type(result))                         # try to print the attributes and its values in the above created table
    # for row in result:
    #     print(f"x:{row.x}   y:{row.y}")
    # for x,y in result:                        # printing by tuple assignment 
    #     print(f"x:{x}   y:{y}")
    # for row in result:                        # printing by integer index
    #     x = row[0]
    #     y = row[1]
    #     print(x,y)
    # for row in result:                          # printing by attribute name              
    #     y = row.y
    #     print(y)
    # for dict_row in result.mappings():          # mapping access
    #     x = dict_row['x']
    #     y = dict_row['y']
    # with engine.connect() as conn:              #sending parameters using where condition
    #     result = conn.execute(
    #     text("SELECT x, y FROM some_table WHERE y > :y"),{"y": 2})
    # for row in result:
    #    print(f"x: {row.x}  y: {row.y}")
# with engine.connect() as conn:              #sending multiple parameters
#         conn.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),[{"x": 11, "y": 12}, {"x": 13, "y": 14}])
#         conn.commit()
# stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=6)
# with engine.connect() as conn:
#         result = conn.execute(stmt)
#         for row in result:
#             print(f"x: {row.x}  y: {row.y}")


#------------------------------executing an orm session

# stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=6)
# with Session(engine) as session:
#     result = session.execute(stmt)
#     for row in result:
#        print(f"x: {row.x}  y: {row.y}")


# with Session(engine) as session:
    # result = session.execute(
    #     text("UPDATE some_table SET y=:y WHERE x=:x"),
    #     [{"x": 9, "y":11}, {"x": 13, "y": 15}]
    # )
    # session.commit()



#--------------------------------------CREATING TABLE

user_table = Table(
    "user_account",
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('fullname', String)
)

address_table = Table(
    "address",
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('user_id', ForeignKey('user_account.id'), nullable=False),
    Column('email_address', String, nullable=False)
)

metadata_obj.create_all(engine)

# print(user_table.c.keys())
# print(user_table.primary_key)


# mapper_registry = registry()
# print(mapper_registry.metadata)