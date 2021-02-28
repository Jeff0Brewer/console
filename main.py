import time
from speechrecog import text_stream, start_listen, stop_listen
from commands import commands

KEYWORD = 'console'

def main():
	global text_stream
	start_listen()

	while True:
		while KEYWORD not in text_stream[0]:
			time.sleep(.25)
		print(text_stream[0])
		text = text_stream[0].split(KEYWORD + ' ')[1]
		text_stream[0] = ''

		for command, callback in commands.items():
			if command in text:
				callback()

if __name__ == '__main__':
	main()