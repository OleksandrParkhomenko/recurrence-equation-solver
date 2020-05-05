import numpy



class CharacteristicEquetion:

	def __init__(self, poly):
		self.equetion = numpy.poly1d(poly)


	def __repr__(self):
		return self.equetion


	def __str__(self):
		return self.__repr__()


	def solve(self):
		return numpy.roots(self.equetion)



class RecurrenceEquetion:

	def __init__(self, equetion, init_conditions):
		self.__equetion_str	 	= equetion
		self.__coefs		 	= self.__parse(equetion)
		self.__charact_eq		= CharacteristicEquetion(self.__coefs)
		self.__init_conditions	= init_conditions
		self.__solution 		= None


	def __repr__(self):
		return self.__equetion_str


	def __str__(self):
		return self.__repr__()


	def get_charact_eq(self):
		return self.__charact_eq.equetion


	def get_solution(self):
		if self.__solution is None:
			return "Equetion hasn't been solved jet or doesn't have a solution"

		solution = "a(n) = "
		for i, _ in enumerate(self.__solution):
			if self.__solution[i] >= 0 and i > 0:
				solution += "+"
			solution += "{0:,.2f}({0:,.2f})^n".format(self.__solution[i], self.__coefs[i])
			#"{0:,.2f}".format(2083525.34561)
			#solution += str(self.__solution[i]) + "(" + str(self.__coefs[i]) + ")^n "

		return solution


	def solve(self):
		solutions = self.__charact_eq.solve()
		a = list()
		b = list()
		for i, elem in enumerate(self.__init_conditions):
			a_i = list()
			for value in solutions:
				a_i.append(value**i)
			a.append(a_i)
			b.append(elem)
		a = numpy.array(a)
		b = numpy.array(b)
		self.__solution = numpy.linalg.solve(a,b)

		return self.__solution


	def __parse(self, equetion_str):
		equetion_str = equetion_str.replace("n","")
		equetion_str = equetion_str.replace("=","")
		equetion_str = equetion_str.replace("+","")
		equetion_str = equetion_str.replace(" ","")
		elements	 = dict()

		while equetion_str:	
			a_index = equetion_str.find("a")
			open_p 	= equetion_str.find("(")
			close_p = equetion_str.find(")")
			elem 	= equetion_str[open_p + 1:close_p]
			elem 	=-int(elem) if elem != "" else 0
			value 	= equetion_str[:a_index]
			equetion_str   = equetion_str[close_p + 1:]

			if value != "" and value != "-":
				elements[elem] = int(value)
			elif value == "-":
				elements[elem] = -1
			else:
				elements[elem] = 1

		coefs = [0] * (max(elements.keys()) + 1)
		for key in elements.keys():
			if key > 0:
				coefs[key] = elements[key] * -1
			else:
				coefs[key] = elements[key] 

		return coefs



### few examples
example_1 			= "a(n) = a(n-1) + 6a(n-2)"
example_1_solutions = [1,2]
example_2 			= "a(n) = -a(n-1) + 4a(n-2) + 4a(n-3)"
example_2_solutions = [8,6,26]

eq1 = RecurrenceEquetion(example_1, example_1_solutions)
eq2 = RecurrenceEquetion(example_2, example_2_solutions)

print("Example #1:")
print("\nEquetion: ", eq1)
eq1.solve()
print("Solution: ", eq1.get_solution())


print("\n\nExample #2:")
print("\nEquetion: ", eq2)
eq2.solve()
print("Solution: ",eq2.get_solution())