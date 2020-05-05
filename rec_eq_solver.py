import numpy



class CharacteristicEquetion:

	def __init__(self, poly):
		self.equetion = numpy.poly1d(poly)


	def __repr__(self):
		return numpy.poly1d(self.equetion)


	def __str__(self):
		return self.__repr__()



class RecurrenceEquetion:

	def __init__(self, equetion):
		self.__equetion_str	= equetion
		self.__coefs		= self.__parse(equetion)
		self.__charact_eq 	= CharacteristicEquetion(self.__coefs)


	def __repr__(self):
		return self.__equetion_str


	def __str__(self):
		return self.__repr__()


	def get_charact_eq(self):
		return self.__charact_eq


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
			elements[elem] = int(value) if value != "" else 0

		coefs = [0] * (max(elements.keys()) + 1)
		for key in elements.keys():
			coefs[key] = elements[key]

		return coefs




#test = CharacteristicEquetion(['q', 'w','z'])

# example 1 
#
# a(n) = a(n-1) + a(n-2)


example_1 = "a(n) = 2a(n-1) + 5a(n-2) - 3a(n-3)"
example_2 = "a(n) = 2a(n-1) + 5a(n-2) - 3a(n-5)"

equetion1 = RecurrenceEquetion(example_1)