print("art.py by Jonnelafin")
import time

def fetch():
	red = ""
	full = []
	with open("presets/base.jfFont", 'r') as f:
		last = ""
		for x in f.read():
			if x == "~":
				full.append(red)
				red = ""
			elif x == "\n" and last == "~":
				1/1
			else:
				red = red + x
			last = x
	return full
def jfprint(font = [], text = "", delay = 0.1):
	whitesp = 1	
	
	chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "?", "!", ":", ".", ",", "'", "-", "|"]
	if text == "":
		text = input("Text: ")
	text = text.upper()
	rows = ["", "", "", "", ""]
	for letter in text:
		if letter == " ":
			art = "    \n"*len(rows)
		else:
			try:
				art = font[chars.index(letter)]
			except Exception as e:
				art = "  █   \n  █   \n  ██  \n  █   \n██████\n"
				print(e)
		artRows = []
		red = ""
		for i in art:
			if i == "\n":
				artRows.append(red + (" "*whitesp))
				red = ""
			else:
				red = red + i
		for i in range(len(rows)):
			rows[i] = rows[i] + artRows[i]
	for i in rows:
		time.sleep(delay)
		print(i)
if __name__ == '__main__':
	font = fetch()
	jfprint(font)
