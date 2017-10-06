
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

#{ Select col from table Where 1=1 }#

*-schema.select("name table").col("name col","age","work",age=21)
## OR #
*- select = schema.select("name table")
*- select.col("name col","age","work",age=21)

#**--> get age,work  where age=21

## OR #
#{ Select col,col from table }#
*- select = schema.select("name table")
*- select.col("name col","age","work")

**--> Not Where 
##
#{ Select * from table where 1=1 }#

*-schema.select("name tables").all(age=21)

## OR #
*-select = schema.select("name tables")
*-select.all(age=21) 

#**--> all where age = 21 get 
## OR #
*-schema.select("name tables").all()

##
#{ Select table1.col,table1.col from table1,tabl2 where table1.col3 = table2.col3 }#
          
*-schema.select("tb1","tb2").joins("col  name from tb1","col name from tb1",join_col="name col") 

## AND #

#{ Select table2.col1,table2.col2 from tabl2,table1 where table2.col3 = table1.col3 }#

*-schema.select("tb2","tb1").joins("col name from tb2","col name from tb2",join_col="name col") 

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
