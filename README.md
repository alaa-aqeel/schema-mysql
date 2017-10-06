# schema-mysql

__You need to install mysql-connector__<br>
__Window__<br>
https://dev.mysql.com/downloads/connector/python/2.1.html<br>
		
__linux__<br>
	
	Installed by the use of pip  :
		sudo pip3 install --allow-external mysql-connector-python mysql-connector-python


__test.py__ <br>

	
	from schema import * 
	
	
	#Teach you how to use the library
	#Like{
		pprint(docs.select)
		Seek examples of how to use the class
		pprint(docs._c_)
	#	*-[
	#	"Update","Select","Drop","sql",
	#	"Columns","tables","Add","Create","isConnect",
	#	"Error","time","datetime","date",configer
	#	*-]
		pprint(docs.drop)
		pprint(docs.sql)
		pprint(docs.configer)
	#}
	
	# Only one database can be connected
	schema.configer["database"] = "boy"
	
	## OR
	# 
	config = {
	
 		"host":"localhost","user" :"root",
		"password" :"", "database" :"test"
	}
	
	schema.configer = config
	
	# 
	if schema.isConnect():
		

		
		# Show the names of the tables in the database
		pprint(schema.tables())
		
		# table::user  column::name
		pprint((schema.select("user").col("name")))
		# where 'password=12345' *select*
		pprint(schema.select("user").col("name",password=12345))
		# all table 
		pprint(schema.select("alaa").all())
		pprint(schema.select("alaa").all(password=12345))

		# Show the names of the columns in the table
		pprint(schema.Columns("user").names())
		
		# Show the info of the columns in the table
		pprint(schema.Columns("user").all())

		schema.Drop("user").col("now")
		
		#  add column to table::user
		n_col = schema.Add("user")
		n_col.string("now",20,1)
		n_col.col()
		
		# update table::alaa .up Update the following columns .where column::age = 21 
		pprint(schema.Update("alaa").up(name="mohommed", age=33).where(age=21))

		


	else:
	    print(schema.Error())
	
