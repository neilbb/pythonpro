



from peewee import *


db = SqliteDatabase('students.db')


class Student(Model):
	username = CharField(max_length=255, unique=True)
	points = IntegerField(default=0)

	class Meta:
		#tell model what database it belongs to
		database = db


s = [
	{'user':'johndoe',
	'lvl':3000
	},{'user':'jaydoe',
	'lvl':321999
	},
	{'user':'ramdoe',
	'lvl':30434
	},
	{'user':'chaitoedoe',
	'lvl':5555
	},
	{'user':'laladoe',
	'lvl':302
	},

]


def add_students():

	for i in s:
		try:
			Student.create(username=i['user'],
						points=i['lvl'])
		except IntegrityError:
			student_record = Student.get(username=i['user'])
			student_record.points = i['lvl']
			student_record.save()


def top_student():
	#student = Student.select() # get all student records in the database
	student = Student.select().order_by(Student.points.desc()).get() # there is a ascending too and get() will get the first one record
	return student


if __name__ == '__main__':
	db.connect()
	db.create_tables([Student],safe=True)
	add_students()
	a = top_student()
	print("the top student",a.username,a.points)




