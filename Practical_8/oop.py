import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")


class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if self.is_empty():
			return None
		return self.items.pop()

	def peek(self):
		if self.is_empty():
			return None
		return self.items[-1]

	def display(self):
		return self.items

	def is_empty(self):
		return len(self.items) == 0


def main():
	stack = Stack()

	while True:
		print("\nStack Operations:")
		print("1. Push")
		print("2. Pop")
		print("3. Peek")
		print("4. Display")
		print("5. Exit")

		choice = input("Enter your choice: ")

		if choice == "1":
			item = input("Enter item to push: ")
			stack.push(item)
		elif choice == "2":
			popped_item = stack.pop()
			if popped_item is None:
				print("Stack is empty.")
			else:
				print(f"Popped item: {popped_item}")
		elif choice == "3":
			top_item = stack.peek()
			if top_item is None:
				print("Stack is empty.")
			else:
				print(f"Top item: {top_item}")
		elif choice == "4":
			print(f"Stack: {stack.display()}")
		elif choice == "5":
			break
		else:
			print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
	main()
