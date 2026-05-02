import random
import time
import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")

num_questions = 5
score = 0

print("Welcome to Quiz\n")

start_time = time.time()  

for i in range(num_questions):
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    op = random.choice(['+', '-'])

    if op == '+':
        correct_answer = a + b
    else:
        correct_answer = a - b

    given_answer = int(input(f"What is {a} {op} {b}? : "))

    if given_answer == correct_answer:
        print("Correct Answer\n")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {correct_answer}\n")

end_time = time.time()  
time_taken = round(end_time - start_time, 2)

print(f"Score : {score} out of {num_questions}")
print(f"Time Taken : {time_taken} Seconds")
