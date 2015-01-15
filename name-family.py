class Student(object):

	courseMarks={}
	name=""
	family=""

	def __init__(self, name, family):
		self.name = name
		self.family = family

	def addCourseMark(self, course, mark):
		self.courseMarks[course] = mark

	def average(self):
		allMarks = self.courseMarks.values()
		return sum(allMarks)/len(allMarks) if len(allMarks) > 0 else 0

if __name__ == "__main__":
	stu1 = Student("Jim","Wan")
	stu1.addCourseMark("Math", 0)
	stu1.addCourseMark("Calc", 100)
	print("Stu1 avg",stu1.average())