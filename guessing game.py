print('guess the hidden number')
secret_number= 3
guess_count = 0
guess_limit =3
while guess_count < guess_limit :
	guess= int ( input('Guess no. ') )
	guess_count +=1
	if guess == secret_number :
		print( 'well done !  , yow won.')
		break
else :
  	print('sorry ! , you failed.')