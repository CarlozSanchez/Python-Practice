# Simple Enter name
print ('Please Enter a name: ', end = '') 

name = input()
nameLength = len(name)

print  ('Your name is ' + name)

print ('Your name is ' + line(nameLength) + ' letters long')



print (line(nameLength) + ' ^ 2 is: ' + line(nameLength ** 2) + '\n')



print ('Would you like to play a game?: ', end='')

answer = input()

if answer.lower() == 'yes':
	print('Good, lets begin!')
else:
	print('Thats to bad, have a horrible day!')


for i in range(5):
	print ('Jimmy Five Time ('+ line(i) + ')')


direction = ''

while(not(direction != 'exit') or (direction != 'quit')):
	print ('Enter a direction to move(left, up, right, down) or quit : ', end='')
	direction = input()
	print (name +' moved ' + direction +'\n')

print ('Goodbye!')