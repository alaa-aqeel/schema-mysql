
class type_():
	def __init__(self,sql):
		self.sql = sql
	def string(self,name,length=255,null=0,default=""):
		not_null = " NOT NULL" if null else ""
		default_  = " DEFAULT %s"%default if default != "" else ""
		self.sql[0] += "%s VARCHAR(%d)%s%s,"%(name,length,not_null,default_)

	def integer(self,name,length=50,null=0,auto=0,default=""):
		not_null = " NOT NULL" if null else ""
		auto_increment = " auto_increment" if auto else ""
		default_  = " DEFAULT %s"%default if default != "" else ""
		self.sql[0] += "%s int(%d)%s%s%s,"%(name,length,not_null,auto_increment,default_)

	def float(self,name,length=50,null=0,auto=0,default=""):
		not_null = " NOT NULL" if null else ""
		auto_increment = " auto_increment" if auto else ""
		default_  = " DEFAULT %s"%default if default != "" else ""
		self.sql[0] += "%s float(%d)%s%s%s,"%(name,length,not_null,auto_increment,default_)

	def double(self,name,length=50,null=0,auto=0,default=""):
		not_null = " NOT NULL" if null else ""
		auto_increment = " auto_increment" if auto else ""
		default_  = " DEFAULT %s"%default if default != "" else ""
		self.sql[0] += "%s DOUBLE(%d)%s%s%s,"%(name,length,not_null,auto_increment,default_)

	def time(self,name,null=0,default=""):
		not_null = " NOT NULL" if null else ""
		default_  = " DEFAULT %s"%default if default != "" else ""
		self.sql[0] += "%s time%s%s,"%(name,not_null,default_)

	def date(self,name,null=0,default=""):
		not_null = " NOT NULL" if null else ""
		default_  = " DEFAULT %s"%default if default != "" else ""
		self.sql[0] += "%s date%s%s,"%(name,not_null,default_)

	def datetime(self,name,null=0,default=""):
		not_null = " NOT NULL" if null else ""
		default_  = " DEFAULT %s"%default if default != "" else ""
		self.sql[0] += "%s datetime%s%s,"%(name,not_null,default_)

	def setPrimaryKey(self,name):
		self.sql[0] += "PRIMARY KEY (%s),"%name

