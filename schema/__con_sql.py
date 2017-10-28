from schema.__type  import type_
from schema.__connect import Connect,db,__msg__

configer = {
	"host"     :"localhost",
	"user"     :"root",
	"password" :"",
	"database" :"",
}


class Create(type_):
	def __init__(self,name):
		if name.strip() != "":
			self.__self__ = Connect(configer)
			
			self.sql_ = [""];self.name = name
			super().__init__(self.sql_)
		else:
			exit()

	def do(self):
		sql = "CREATE TABLE %s (%s);"%(self.name,self.sql_[0].strip(","))
		try:
			self.__self__.cur.execute(sql)
			return 1
		except db.Error as er:
			return str(er)
		except:
			return __msg__[0]

class Add(type_):
	def __init__(self,name):

		if name.strip() != "":
			super().__init__([""])
			self.__self__ = Connect(configer)
			self.name = name;
		else:
			exit()

	def row(self,*t_values,**d_values):
		if d_values != {}:
			sql = "INSERT INTO %s %s VALUES %s ;"%(self.name,str(tuple(d_values.keys())),str(tuple(d_values.values())))
		elif t_values != tuple():
			sql = "INSERT INTO %s  VALUES %s ;"%(self.name,str(tuple(t_values)))
		else:
			return "*t_values and **d_values 'forget' \n help: print(schema.docs.add)"
		try:
			self.__self__.cur.execute(sql)
			self.__self__.connect_.commit()
			return 1
		except db.Error as er:
		
			return str(er)
		except:
			return __msg__[0]

	def col(self):

		sql = "ALTER TABLE %s ADD %s;"%(self.name,self.sql[0].strip(","))
		print(sql)
		try:
			self.__self__.cur.execute(sql.strip())
			self.__self__.connect_.commit()
			return 1
		except db.Error as er:
			return str(er)
		except:
			return __msg__[0]



class Select(Connect):
	_all  = {}
	def __init__(self,*col,index=""):
		if str(col).strip() != "": 
			super().__init__(configer)
			self.index = index
			sql = "SELECT * FROM %s;"%str(",".join(col))
			try:
				self.cur.execute(sql)
				Select.cols =self.cur.column_names
				for i in self.cur.column_names:
					self._all.update({i:[]})

				for v in self.cur.fetchall():
					for k in self.cols:
						if self._all.get(k) != None:
							self._all[k].append(v[self.cols.index(k)])

				for k,v in self._all.items():
					self._all[k] = tuple(self._all.get(k))

			except db.Error as er:
				print(er)
				self._all.update({"Error":str(er)})
			except Exception as ers :
				print(ers)

		else:
			self._all.update({"Error":"Error: select(Name Table) !!"})

	def __getattr__(self,name):
		if self._all.get("Error"):
			return self._all.get("Error")

		if name == "all":
			return self._all
		if self.index != "" and self.index:
			return self._all.get(name)[self.index]
		return self._all.get(name)
		

class Columns(Connect):
	def __init__(self,name):
		if name.strip() != "": 
			super().__init__(configer)
			self.command = "SHOW COLUMNS FROM %s"%name
		else:
			exit()

	def names(self):
		try:
			self.cur.execute(self.command)
			row = [] # Field
			for i in self.cur.fetchall():
				row.append(i[0])
			return row 
		except db.Error as er:
			return str(er)
		except:
			return __msg__[0]

	def all(self):
		try:
			self.cur.execute(self.command)
			return self.cur.fetchall()
		except db.Error as er:
			return str(er)
		except:
			return __msg__[0]			


class Update(Connect):
	def __init__(self,name):
		if name.strip() != "":
			self.name = name
			super().__init__(configer)
		else:
			exit()

	def up(self,**col_update):
		if col_update != {}:
			cols   = "" if self.reg(col_update) == "" else self.reg(col_update).strip(",")
			self.sql = "UPDATE %s SET %s"%(self.name,cols)
			return self 
		else:
			return " **cols_update = 'forget' \n help: print(schema.docs.update)"

	def where(self,**where):
		if where != {}:
			wheres = "" if self.reg(where) == "" else self.reg(where).strip(",")
			self.sql +=" WHERE %s;"%wheres
			try:
				self.cur.execute(self.sql)
				self.connect_.commit()
				return 1
			except db.Error as er:
				return str(er)
			except:
				return __msg__[0]
		else:
			return " **where = 'forget' \n help: print(schema.docs.update)"

	def reg(self,where):
		where_s = ""
		for k,v in where.items():
			if type(v) in (int,float,bool):
				where_s += str(k)+"="+str(v)
			else:
				where_s += str(k)+"='"+str(v)+"'"
			where_s += ","
		return where_s


		
		
class Drop(Connect):
	def __init__(self,name):
		if name.strip() != "": 
			super().__init__(configer)
			self.name = name
		else:
			exit()


	def table(self):
		try:
			self.cur.execute("drop table %s"%self.name)
			self.connect_.commit()
			return 1
		except db.Error as er:
			return str(er)
		except:
			return __msg__[0]

	def col(self,name):
		if name.strip() != "":
			sql = "ALTER TABLE %s DROP %s;"%(self.name,name)
			try:
				self.cur.execute(sql)
				self.connect_.commit()
				return 1
			except db.Error as er:
				return str(er)
			except:
				return __msg__[0]
		else:
			return " name = '' \n help: print(schema.docs.drop)"

	def row(self,**where):
		if where != {}:
			where_s = ""
			for k,v in where.items():
				if type(v) in (int,float,bool):
					where_s += str(k)+"="+str(v)
				else:
					where_s += str(k)+"='"+str(v)+"'"
				where_s += ","
			sql = "DELETE FROM %s WHERE %s;"%(self.name,where_s.strip(","))
			try:
				self.cur.execute(sql)
				self.connect_.commit()
				return 1
			except db.Error as er:
				return str(er)
			except:
				return __msg__[0]
		else:
			return " **where = {} \n help: print(schema.docs.drop)"


def tables():
	command = "SHOW TABLES"
	__self__ = Connect(configer)
	cur = __self__.cur.execute(command)
	row = []
	for i in __self__.cur.fetchall():
		row.append(i[0])
	return row
	

def isConnect():
	__self__ = Connect(configer)
	return __self__.con
def Error():
	return __msg__[0]


def sql(command):
	""" SQL command """
	if command.strip() != "":
		try:
			dic_t = {}
			__self__ = Connect(configer)
			for i in __self__.cur.execute("%s"%command,multi=True):
				if i.with_rows:
					rows = i.fetchall()
					dic_t.update({str(i).split(":")[1]:rows})
			__self__.connect_.commit()
			return dic_t
		except db.Error as er:
			return str(er)
		except:
			return __msg__[0]
	else:
		return None
		
