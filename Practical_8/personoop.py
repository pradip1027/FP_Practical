import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def display(self):
		print(f"Name: {self.name}")
		print(f"Age: {self.age}")


class Student(Person):
	def __init__(self, name, age, section):
		super().__init__(name, age)
		self.section = section

	def displayStudent(self):
		print("\nStudent details:")
		self.display()
		print(f"Section: {self.section}")


def main():
	name = input("Enter name: ")
	age = input("Enter age: ")
	section = input("Enter section: ")

	student_obj = Student(name, age, section)
	student_obj.displayStudent()


if __name__ == "__main__":
	main()
