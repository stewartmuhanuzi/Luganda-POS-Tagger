import random

proper = ['Uganda', 'Nankya', 'Kabaka', 'Muhanuzi', 'Nyangoma', 'Masaka', 'Nansana', 'Mukono']
common = ['omuwala', 'omulenzi', 'omukyala', 'omusajja', 'emiti', 'embwa', 'kapira']
modifier = []
verb = ['bagenda','aduka', 'azanya', 'ayimba', 'atambula','asamba' ]
prep= []

#functions

#noun phrase takes argument to determine capitalization
def NounPhrase(case = 0):

	phrase = ""
#	print phrase
	#establish random boolean value
	rn = random.randint(0,1)
#	print rn
	#if statement to determine 
	if rn == 0: #this generates a proper noun phrase
		n = random.randint(0,(len(proper)-1))
	# 	print n
	#	print proper[n]
		phrase = proper[n] #initializes to noun phrase  plus space

	else: #this generates common noun phrase
		phrase = "" #initializes phrase with 'The'

		rn = random.randint(0,1)
		if rn = 1: #if random is 1, need to include modifier	
			n = random.randint(0,(len(modifier)-1)) #picks random index
			phrase += (modifier[n] + "") #appends modifier plus space

		n = random.randint(0,(len(common)-1))
		phrase += common[n]	#append common noun to end of string
		if case ==1:
			phrase = phrase.lower()

	return phrase


	def PrepPhrase():
		rn = random.randint(0,1)
		if rn ==0: #this generates no prepositional phrase
			return ""
		else:
			n = random.randint(0,(len(prep))	
			



