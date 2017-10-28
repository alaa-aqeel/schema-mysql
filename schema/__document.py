
_c_ = [
 
	"Update",
	"Select",
	"Drop",
	"sql",
	"Columns",
	"tables",
	"Add",
	"Create",
	"isConnect",
	"Error",
	"time",
	"datetime",
	"date",
	"configer"
]

configer = """
# * Configer  *

schema.configer = {
 		"host":"localhost",
		"user" :"root", 
		"password" :"", 
		"database" :""
}
schema.configer["database"] = "boy" *boy is database in my MySQLdatabase
"""

type_ = """

*-string(name,length=255,null=0,default="")
*-integer(name,length=50,null=0,auto=0,default="")
*-float(name,length=50,null=0,auto=0,default="")
*-double(name,length=50,null=0,auto=0,default="")
*-time(name,null=0,default="")
*-date(name,null=0,default="")
*-datetime(name,null=0,default="")
*-setPrimaryKey(name)

"""

update = """
# * Update *
## Update Table 
*-update = schema.Update("alaa")
*-update.up(name="mohommed",age=33).where(age=21)

## OR # 
*-update = schema.Update("alaa").up(name="mohommed",age=33)
*-update.where(age=21)

## OR #
*-schema.Update("alaa").up(name="mohommed",age=33).where(age=21) 
##
"""

select = """
# * Select  *
##
#table = Select("alaa")
#print(table.columns) #// return "columns name"
#print(table.name)    #// return alaa itme in col name
#tabl.all     #//  return dict(table::alaa)

#table = Select("alaa",index=-1) #// index=-1  "get last item in cols"
#print(table.name)    #// return last item in name
#tabl.all     #// return dict(table::alaa)

"""

add = """
# * Add = Insert  *
## Add Row to table::user 
*-schema.Add("user").row("abce",1230999)  * or *  schema.Add("user").row(name="abce",pass=1230999)
## OR # 
*-add_row = schema.Add("user")
*-add_row("name","password")

## Add Column to table::user 
*-a_col = schema.Add("user")
# type # 
*-a_col.string("nameCol",length=10,null=0)
# add #
*-col.col()
## 
"""




 
Create = """
# * Create  *


## Create Table 

*-c_table = schema.Create("name table")

	
type- " varchar " 
**-c_table.strin(name="name col",length=255,not_null=0)

type- integer == int 
**-c_table.integer(name="name col",length=50,not_null=0,auto=0)

type- float 
**-c_table.float(name="name col",length=50,not_null=0,auto=0)

**--> null = NOT NULL 
**--> auto = auto_increment

**-setPrimaryKey(name="col")

*-c_table.do()

##
"""

# * - - - - *
tables = """
# * tables  *

** Show the names of the tables in the database

*-schema.tables() return name table in database

"""


Columns = """
# * Columns *

# Show the names of the columns in the table
*-schema.Columns("name table").names()

# Show the info of the columns in the table
*-schema.Columns("name table").all()  
"""



Drop = """
# * drop  * 

# remove table 
*-schema.Drop("name table").table()            

# remove col from table  " columen::name "
*-schema.Drop("name table").col("name")        

# remove row from table " where name='alaa' "
*-schema.Drop("name table").row(name="alaa")  

## OR #
##
*-drop =  schema.Drop("user")

*-drop.table()
*-drop.col("password")
*-drop.row(passwrod=12345)
##

"""




sql = """
# * sql * 

*-schema.sql("command sql;show tables;select * from name_table;drop table name_table ") 
>>> return {
     "show tables" : {},
     "select * from name_table" :  {},
	 to other .... *
}
"""
