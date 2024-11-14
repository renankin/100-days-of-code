bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi))  # flooring a number

print(round(bmi, 2))  # rounding

# assignment operators
score = 9

# Users scores a point
score += 1  # sum up
score -= 1  # reduce
score *= 1  # multiply
score /= 3  # divide

print(score)

# f-strings
print("Your score is " + str(score))

score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")
