X = {    "apiKey": "AIzaSyDpyGIbJXOHc53qTMGdG9XS8tnFeREcxNY",
    "authDomain": "anaglyph-letter-game.firebaseapp.com",
    "projectId": "anaglyph-letter-game",
    "storageBucket": "anaglyph-letter-game.appspot.com",
    "messagingSenderId": "370658729206",
    "appId": "1:370658729206:web:93a8b30502aaa30ab2a0d7",}

for k, v in X.items():
	print(f'NEXT_PUBLIC_FIREBASE_{k.upper()}={v}')


for k, v in X.items():
	print(f'{k}:process.env.NEXT_PUBLIC_FIREBASE_{k.upper()},')	