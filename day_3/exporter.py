people = [
	('Joe', 78),
	('Janet', 90),
	('Brain', 67)
	]

def super_sum(*args):
	return sum(args)

def hello_again(name, age):
	return "I am {}  and {} years old".format(name, age)

def max_min(A):
	max_, min_ = A[0], A[0]
	for i in A:
		if i > max_:
			max_ = i
		if i < min_:
			min_ = i
	return max_ - min_
