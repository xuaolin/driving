country = input('where do you come from?')
age = input('how old are you?')
age = int (age)
if country == '中国':
	if age >= 18:
		print ('you can drive')
	else:
		print ('you cant drive')
elif country == '美国':
	if age >= 16:
		print ('you can drive')
	else:
		print ('you cant drive')