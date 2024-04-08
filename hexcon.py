#!/usr/bin/python3

# by AlissoftCodes
# Github: https://github.com/AlissoftCodes/
# Instagram: https://instagram.com/AlissonFaoli

import os, sys, re

if sys.platform == 'linux':
	pro_tip = f'''\n\033[36mPro tip:
	It works smoother if you add \033[35mhexcon\033[39m \033[36mto your aliases file.
	Command: \033[33msudo echo "alias hexcon='python3 {os.path.abspath(__file__)}'" >> {os.getenv('HOME')}/.{os.getenv('SHELL').split(os.sep)[-1].lower()}_aliases\033[39m\n'''
else:
	pro_tip = ''

HELP = f'''
\033[35mhexcon\033[39m \033[32mby AlissoftCodes\033[39m
\033[34mGithub\033[39m: \033[32mhttps://github.com/AlissoftCodes/hexcon\033[39m

Usage:
	python3 {sys.argv[0]} [options]
		-h, --help		Show this help message and exit
		-e, --encode		Text to hex (encode mode)
		-d, --decode		Hex to text (decode mode)
		-i, --intelligent	Intelligent mode (decode/encode) - Default if no option is provided
		-ue, --url-encode	URL encode
		-ud, --url-decode	URL decode

If you run the script without any content, it will run in interactive mode.

Examples:
	Encoding:
		python3 {sys.argv[0]} -e "Hello World"
	Decoding:
		python3 {sys.argv[0]} -d "48656c6c6f20576f726c64"
	Intelligent mode:
		python3 {sys.argv[0]} -i "Hello World"
		python3 {sys.argv[0]} -i '48656c6c6f20576f726c64'
	URL encoding:
		python3 {sys.argv[0]} -ue "Hello World"
	URL decoding:
		python3 {sys.argv[0]} -ud "Hello%20World"
	Interactive mode:
		python3 {sys.argv[0]}

Note:
	If you want to echo a string into the script, you can use the following syntax:
		echo "Hello World" | python3 {sys.argv[0]} -e
{pro_tip}
'''

def intelligence(text):
	if re.match(r'^[0-9a-fA-F]+$', text):
		return fh(text)
	else:
		return th(text)


def url_encode(text):
	return ''.join(map(lambda x: x if (x.isalnum() or x in '-._~') else '%' + format(ord(x), 'x').upper(), text))


def url_decode(text):
	d = ''
	i = 0
	while i < len(text):
		if text[i] == '%':
			d += chr(int(text[i + 1:i + 3], 16))
			i += 3
		else:
			d += text[i]
			i += 1
	return d


def th(text):
	return ''.join(list(map(lambda x: format(ord(x), 'x'), text)))


def fh(hexa):
	results = []
	for text in hexa.split():
		result = []
		for i in range(0, len(text), 2):
			result.append(chr(int(text[i:i+2], 16)))
		results.append(''.join(result))
	return '\n'.join(results)


def interactive():
	while True:
		try:
			match input('[1] Text to hex\n[2] Hex to text\n[3] URL encode\n[4] URL decode\n[5] Exit\n> '):
				case '1':
					print('\033[32m[+]\033[39m Result: '+th(input('Text to hex: ')))
				case '2':
					print('\033[32m[+]\033[39m Result: '+fh(input('Hex to text: ')))
				case '3':
					print('\033[32m[+]\033[39m Result: '+url_encode(input('Text to URL encode: ')))
				case '4':
					print('\033[32m[+]\033[39m Result: '+url_decode(input('URL encoded text: ')))
				case '5':
					break
				case _:
					print('\033[31m[!]\033[39m Invalid option!')
		except KeyboardInterrupt:
			break
		except ValueError:
			print('\033[31m[!]\033[39m Bad format!')
		except Exception:
			print('\033[31m[!]\033[39m Fatal error...')
	sys.exit(0)


def get_input():
	if not os.isatty(0):
		return sys.stdin.read().strip()
	elif len(sys.argv) > 1:
		return sys.argv[-1]
	else:
		return interactive()


def get_mode():
	if len(sys.argv) > 1:
		mode = sys.argv[1]
		mode = re.sub(r'^--help', '-h', mode)
		mode = re.sub(r'^--encode', '-e', mode)
		mode = re.sub(r'^--decode', '-d', mode)
		mode = re.sub(r'^--url.?encode', '-ue', mode)
		mode = re.sub(r'^--url.?decode', '-ud', mode)
		mode = re.sub(r'^--intelligent', '-i', mode)
		return mode
	else:
		return 'i'


def main():
	try:
		text = get_input()
		match get_mode():
			case '-e':
				print(th(text))
			case '-d':
				print(fh(text))
			case '-i':
				print(intelligence(text))
			case '-ue':
				print(url_encode(text))
			case '-ud':
				print(url_decode(text))
			case '-h':
				print(HELP)
			case _:
				if len(sys.argv) > 2:
					print('\033[31m[!]\033[39m Invalid option!')
				else:
					print(intelligence(text))
	except KeyboardInterrupt:
		sys.exit(0)
	except ValueError:
		print('\033[31m[!]\033[39m Bad format!')
	except Exception:
		print('\033[31m[!]\033[39m Fatal error...')



if __name__ == '__main__':
	main()
