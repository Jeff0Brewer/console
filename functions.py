import webbrowser, subprocess, os, random
from appscript import app, mactypes
from speechrecog import stop_listen


webbrowser.get('open -a /Applications/Google\ Chrome.app %s')
urls = {
	'youtube': 'https://www.youtube.com/', 
	'pandora': 'https://www.pandora.com/',
	'canvas': 'https://canvas.northwestern.edu/',
	'github': 'https://github.com/Jeff0Brewer',
	'visualizer': 'https://jeff0brewer.github.io/mat_vis/mat_vis.html',
	'email': 'https://mail.google.com/mail/ca/u/2/#inbox'
}

paths = {
	'school': '/Users/jeff/Documents/0_school',
	'music': '/Users/jeff/Documents/music',
	'documents': '/Users/jeff/Documents'
}

background_dir = '/Users/jeff/backgrounds/'
black_bg = 'black.jpg'
curr_bg = str(app('Finder').desktop_picture.get()).split('\'')
curr_bg = curr_bg[len(curr_bg) - 2]
backgrounds = os.listdir(background_dir)
backgrounds.remove(black_bg)

def chrome_youtube():
	webbrowser.open(urls['youtube'])

def chrome_pandora():
	webbrowser.open(urls['pandora'])

def chrome_canvas():
	webbrowser.open(urls['canvas'])

def chrome_visualizer():
	webbrowser.open(urls['visualizer'])

def chrome_email():
	webbrowser.open(urls['email'])

def chrome_github():
	webbrowser.open(urls['github'])

def finder_school():
	subprocess.Popen(['open', paths['school']])

def finder_music():
	subprocess.Popen(['open', paths['music']])

def finder_documents():
	subprocess.Popen(['open', paths['documents']])

def terminal_new():
	os.system('open -a Terminal .')

def desktop_black():
	app('Finder').desktop_picture.set(mactypes.File(background_dir + black_bg))

def desktop_random():
	global curr_bg
	
	bg = random.choice(backgrounds)
	while bg == curr_bg:
		bg = random.choice(backgrounds)
	curr_bg = bg
	app('Finder').desktop_picture.set(mactypes.File(background_dir + bg))

def clear_terminal():
	os.system('clear')

def stop_app():
	stop_listen()
	exit()