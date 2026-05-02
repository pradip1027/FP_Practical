import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")



import time

class StopWatch:
	def __init__(self):
		self.__startTime = time.time()
		self.__endTime = self.__startTime

	def getStartTime(self):
		return self.__startTime

	def getEndTime(self):
		return self.__endTime

	def start(self):
		self.__startTime = time.time()

	def stop(self):
		self.__endTime = time.time()

	def getElapsedTime(self):
		return int((self.__endTime - self.__startTime) * 1000)


def main():
	watch = StopWatch()
	watch.start()

	total = 0
	for i in range(1, 10000000):
		total += i

	watch.stop()

	print("Elapsed time:", watch.getElapsedTime(), "milliseconds")


if __name__ == "__main__":
	main()
