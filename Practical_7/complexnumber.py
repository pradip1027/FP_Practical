import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")


class ComplexNumber:
	def __init__(self, real, imag=3):
		self.real = float(real)
		self.imag = float(imag)

	def add(self, other):
		return ComplexNumber(self.real + other.real, self.imag + other.imag)

	def sub(self, other):
		return ComplexNumber(self.real - other.real, self.imag - other.imag)

	def mul(self, other):
		real_part = (self.real * other.real) - (self.imag * other.imag)
		imag_part = (self.real * other.imag) + (self.imag * other.real)

		if real_part == 0 and imag_part == 0:
			raise ValueError("Multiplication result cannot be 0.")

		return ComplexNumber(real_part, imag_part)

	def __str__(self):
		return f"{self.real:.1f} + {self.imag:.1f}i"


def read_float(prompt_text):
	while True:
		try:
			return float(input(prompt_text))
		except ValueError:
			print("Error: Please enter a valid number.")


def main():
	first_real = read_float("Enter the real part of the first complex number: ")
	first_imag_input = input(
		"Enter the imaginary part of the first complex number (default is 3): "
	).strip()

	if first_imag_input == "":
		first_imag = 3
	else:
		try:
			first_imag = float(first_imag_input)
		except ValueError:
			print("Invalid input for imaginary part. Using default value 3.")
			first_imag = 3

	second_real = read_float("Enter the real part of the second complex number: ")

	c1 = ComplexNumber(first_real, first_imag)
	c2 = ComplexNumber(second_real)

	print(f"C1 = {c1}")
	print(f"C2 = {c2}")

	addition = c1.add(c2)
	subtraction = c1.sub(c2)

	print(f"Addition: {addition}")
	print(f"Subtraction: {subtraction}")

	try:
		multiplication = c1.mul(c2)
		print(f"Multiplication: {multiplication}")
	except ValueError as err:
		print(f"Error: {err}")


if __name__ == "__main__":
	main()
