# schema-mysql


__test.py__ <br>

	```
	from schema import * 
	
	```<br>
__document.py__<br>

	```
	Teach you how to use the library
	Like:
		pprint(docs.select)
		Seek examples of how to use the class
		pprint(docs._c_)
		*-[
		"Update","Select","Drop","sql",
		"Columns","tables","Add","Create","isConnect",
		"Error","time","datetime","date",configer
		*-]
		pprint(docs.drop)
		pprint(docs.sql)
		pprint(docs.configer)
		
	```

	```
	schema.configer["database"] = "boy"
	if schema.isConnect():

		pprint((schema.select("user").col("a")))

		pprint(schema.tables())

		pprint(schema.Columns("user").names())

		schema.Drop("user").col("now")

		n_col = schema.Add("user")
		n_col.string("now",20,1)
		n_col.col()

		pprint(schema.Columns("user").names())


		pprint(schema.select("user").col("name",password=12345))
		print("alaa."+str(",alaa.".join(("1","2","3"))))

		pprint(schema.Update("alaa").up(name="mohommed",age=33).where(age=21))

		pprint(schema.select("alaa").all())


	else:
	    print(schema.Error())
	```
