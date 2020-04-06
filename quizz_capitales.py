import json
import random
import time
import sys
import unicodedata
import os.path

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

toto = '''{
	"quizzData" : [
		{
"country": "Afghanistan",
"city": "Kaboul"
},
{
"country": "Albanie",
"city": "Tirana"
},
{
"country": "Algerie",
"city": "Alger"
},
{
"country": "Andorre",
"city": "Andorre-la-Vieille"
},
{
"country": "Angola",
"city": "Luanda"
},
{
"country": "Antigua-et-Barbuda",
"city": "Saint John's"
},
{
"country": "Argentine",
"city": "Buenos Aires"
},
{
"country": "Arménie",
"city": "Erevan"
},
{
"country": "Australie",
"city": "Canberra"
},
{
"country": "Autriche",
"city": "Vienne"
},
{
"country": "Azerbaïdjan",
"city": "Bakou"
},
{
"country": "Bahamas",
"city": "Nassau"
},
{
"country": "Bahreïn",
"city": "Manama"
},
{
"country": "Bangladesh",
"city": "Dacca"
},
{
"country": "Barbade",
"city": "Bridgetown"
},
{
"country": "Biélorussie",
"city": "Minsk"
},
{
"country": "Belgique",
"city": "Bruxelles"
},
{
"country": "Belize",
"city": "Belmopan"
},
{
"country": "Bénin",
"city": "Porto-Novo"
},
{
"country": "Bermudes",
"city": "Hamilton"
},
{
"country": "Bhoutan",
"city": "Thimphou"
},
{
"country": "Bolivie",
"city": "La Paz"
},
{
"country": "Bosnie-Herzégovine",
"city": "Sarajevo"
},
{
"country": "Botswana",
"city": "Gaborone"
},
{
"country": "Brésil",
"city": "Brasilia"
},
{
"country": "Brunei",
"city": "Bandar Seri Begawan"
},
{
"country": "Bulgarie",
"city": "Sofia"
},
{
"country": "Burkina Faso",
"city": "Ouagadougou"
},
{
"country": "Burundi",
"city": "Bujumbura"
},
{
"country": "Cambodge",
"city": "Phnom Penh"
},
{
"country": "Cameroun",
"city": "Yaoundé"
},
{
"country": "Canada",
"city": "Ottawa"
},
{
"country": "Cap-Vert",
"city": "Praia"
},
{
"country": "République centrafricaine",
"city": "Bangui"
},
{
"country": "Tchad",
"city": "N'Djaména"
},
{
"country": "Chili",
"city": "Santiago"
},
{
"country": "Chine",
"city": "Pékin"
},
{
"country": "Colombie",
"city": "Bogota"
},
{
"country": "Comores",
"city": "Moroni"
},
{
"country": "République du Congo",
"city": "Brazzaville"
},
{
"country": "Îles Cook",
"city": "Avarua"
},
{
"country": "Costa Rica",
"city": "San José"
},
{
"country": "Croatie",
"city": "Zagreb"
},
{
"country": "Cuba",
"city": "La Havane"
},
{
"country": "Chypre",
"city": "Nicosie"
},
{
"country": "République tchèque",
"city": "Prague"
},
{
"country": "Danemark",
"city": "Copenhague"
},
{
"country": "Djibouti",
"city": "Djibouti"
},
{
"country": "Dominique",
"city": "Roseau"
},
{
"country": "République dominicaine",
"city": "Saint-Domingue"
},
{
"country": "Timor oriental",
"city": "Dili"
},
{
"country": "Équateur",
"city": "Quito"
},
{
"country": "Egypte",
"city": "Le Caire"
},
{
"country": "Salvador",
"city": "San Salvador"
},
{
"country": "Guinée équatoriale",
"city": "Malabo"
},
{
"country": "Érythrée",
"city": "Asmara"
},
{
"country": "Estonie",
"city": "Tallinn"
},
{
"country": "Éthiopie",
"city": "Addis-Abeba"
},
{
"country": "Fidji",
"city": "Suva"
},
{
"country": "Finlande",
"city": "Helsinki"
},
{
"country": "France",
"city": "Paris"
},
{
"country": "Gabon",
"city": "Libreville"
},
{
"country": "Gambie",
"city": "Banjul"
},
{
"country": "Géorgie",
"city": "Tbilisi"
},
{
"country": "Allemagne",
"city": "Berlin"
},
{
"country": "Ghana",
"city": "Accra"
},
{
"country": "Gibraltar",
"city": "Gibraltar"
},
{
"country": "Grèce",
"city": "Athènes"
},
{
"country": "Groenland",
"city": "Nuuk"
},
{
"country": "Grenade",
"city": "Saint-Georges"
},
{
"country": "Guatemala",
"city": "Guatemala"
},
{
"country": "Guinée",
"city": "Conakry"
},
{
"country": "Guinée-Bissau",
"city": "Bissau"
},
{
"country": "Guyana",
"city": "Georgetown"
},
{
"country": "Haiti",
"city": "Port-au-Prince"
},
{
"country": "Vatican",
"city": "Cité du Vatican"
},
{
"country": "Honduras",
"city": "Tegucigalpa"
},
{
"country": "Hongrie",
"city": "Budapest"
},
{
"country": "Islande",
"city": "Reykjavik"
},
{
"country": "Inde",
"city": "New Delhi"
},
{
"country": "Indonésie",
"city": "Jakarta"
},
{
"country": "Iran",
"city": "Téhéran"
},
{
"country": "Irak",
"city": "Bagdad"
},
{
"country": "Irlande",
"city": "Dublin"
},
{
"country": "Israël",
"city": "Tel-aviv"
},
{
"country": "Italie",
"city": "Rome"
},
{
"country": "Côte d'Ivoire",
"city": "Yamoussoukro"
},
{
"country": "Jamaïque",
"city": "Kingston"
},
{
"country": "Japon",
"city": "Tokyo"
},
{
"country": "Jordanie",
"city": "Amman"
},
{
"country": "Kazakhstan",
"city": "Astana"
},
{
"country": "Kenya",
"city": "Nairobi"
},
{
"country": "Kiribati",
"city": "Tarawa-Sud"
},
{
"country": "Koweït",
"city": "Koweït"
},
{
"country": "Kirghizistan",
"city": "Bichkek"
},
{
"country": "Laos",
"city": "Vientiane"
},
{
"country": "Lettonie",
"city": "Riga"
},
{
"country": "Liban",
"city": "Beyrouth"
},
{
"country": "Lesotho",
"city": "Maseru"
},
{
"country": "Liberia",
"city": "Monrovia"
},
{
"country": "Libye",
"city": "Tripoli"
},
{
"country": "Liechtenstein",
"city": "Vaduz"
},
{
"country": "Lituanie",
"city": "Vilnius"
},
{
"country": "Luxembourg",
"city": "Luxembourg"
},
{
"country": "Macédoine du Nord",
"city": "Skopje"
},
{
"country": "Madagascar",
"city": "Antananarivo"
},
{
"country": "Malawi",
"city": "Lilongwe"
},
{
"country": "Malaisie",
"city": "Kuala Lumpur"
},
{
"country": "Maldives",
"city": "Malé"
},
{
"country": "Mali",
"city": "Bamako"
},
{
"country": "Malte",
"city": "La Valette"
},
{
"country": "Îles Marshall",
"city": "Majuro"
},
{
"country": "Martinique",
"city": "Fort-de-France"
},
{
"country": "Mauritanie",
"city": "Nouakchott"
},
{
"country": "Maurice",
"city": "Port-Louis"
},
{
"country": "Mexique",
"city": "Mexico"
},
{
"country": "Micronésie",
"city": "Palikir"
},
{
"country": "Moldavie",
"city": "Chisinau"
},
{
"country": "Monaco",
"city": "Monaco"
},
{
"country": "Mongolie",
"city": "Oulan-Bator"
},
{
"country": "Maroc",
"city": "Rabat"
},
{
"country": "Mozambique",
"city": "Maputo"
},
{
"country": "Myanmar",
"city": "Naypyidaw"
},
{
"country": "Namibie",
"city": "Windhoek"
},
{
"country": "Nauru",
"city": "Yaren"
},
{
"country": "Népal",
"city": "Katmandou"
},
{
"country": "Pays-Bas",
"city": "Amsterdam"
},
{
"country": "Nouvelle-Zélande",
"city": "Wellington"
},
{
"country": "Nicaragua",
"city": "Managua"
},
{
"country": "Niger",
"city": "Niamey"
},
{
"country": "Nigeria",
"city": "Abuja"
},
{
"country": "Niue",
"city": "Alofi"
},
{
"country": "Corée du Nord",
"city": "Pyongyang"
},
{
"country": "Irlande du Nord",
"city": "Belfast"
},
{
"country": "Norvège",
"city": "Oslo"
},
{
"country": "Oman",
"city": "Mascate"
},
{
"country": "Pakistan",
"city": "Islamabad"
},
{
"country": "Palaos",
"city": "Melekeok"
},
{
"country": "Palestine",
"city": "Ramallah"
},
{
"country": "Panama",
"city": "Panama"
},
{
"country": "Papouasie-Nouvelle-Guinée",
"city": "Port Moresby"
},
{
"country": "Paraguay",
"city": "Asuncion"
},
{
"country": "Pérou",
"city": "Lima"
},
{
"country": "Philippines",
"city": "Manille"
},
{
"country": "Pologne",
"city": "Varsovie"
},
{
"country": "Portugal",
"city": "Lisbonne"
},
{
"country": "Porto Rico",
"city": "San Juan"
},
{
"country": "Qatar",
"city": "Doha"
},
{
"country": "Reunion",
"city": "Saint-Denis"
},
{
"country": "Roumanie",
"city": "Bucarest"
},
{
"country": "Russie",
"city": "Moscou"
},
{
"country": "Rwanda",
"city": "Kigali"
},
{
"country": "Saint-Christophe-et-Niévès",
"city": "Basseterre"
},
{
"country": "Sainte-Lucie",
"city": "Castries"
},
{
"country": "Saint-Vincent-et-les-Grenadines",
"city": "Kingstown"
},
{
"country": "Samoa",
"city": "Apia"
},
{
"country": "Saint-Marin",
"city": "Saint-Marin"
},
{
"country": "Sao Tomé-et-Principe",
"city": "Sao Tomé"
},
{
"country": "Arabie saoudite",
"city": "Riyad"
},
{
"country": "Ecosse",
"city": "Édimbourg"
},
{
"country": "Sénégal",
"city": "Dakar"
},
{
"country": "Seychelles",
"city": "Victoria"
},
{
"country": "Sierra Leone",
"city": "Freetown"
},
{
"country": "Singapour",
"city": "Singapour"
},
{
"country": "Slovaquie",
"city": "Bratislava"
},
{
"country": "Slovénie",
"city": "Ljubljana"
},
{
"country": "Salomon",
"city": "Honiara"
},
{
"country": "Somalie",
"city": "Mogadiscio"
},
{
"country": "Afrique du Sud",
"city": "Pretoria"
},
{
"country": "Corée du Sud",
"city": "Séoul"
},
{
"country": "Soudan du Sud",
"city": "Djouba"
},
{
"country": "Espagne",
"city": "Madrid"
},
{
"country": "Sri Lanka",
"city": "Colombo"
},
{
"country": "Soudan",
"city": "Khartoum"
},
{
"country": "Suriname",
"city": "Paramaribo"
},
{
"country": "Swaziland",
"city": "Mbabane"
},
{
"country": "Suède",
"city": "Stockholm"
},
{
"country": "Suisse",
"city": "Berne"
},
{
"country": "Syrie",
"city": "Damas"
},
{
"country": "Tadjikistan",
"city": "Douchanbé"
},
{
"country": "Tanzanie",
"city": "Dodoma"
},
{
"country": "Thailande",
"city": "Bangkok"
},
{
"country": "République démocratique du Congo",
"city": "Kinshasa"
},
{
"country": "Togo",
"city": "Lomé"
},
{
"country": "Tonga",
"city": "Nuku'alofa"
},
{
"country": "Trinité-et-Tobago",
"city": "Port-d'Espagne"
},
{
"country": "Tunisie",
"city": "Tunis"
},
{
"country": "Turquie",
"city": "Ankara"
},
{
"country": "Turkménistan",
"city": "Achgabat"
},
{
"country": "Tuvalu",
"city": "Funafuti"
},
{
"country": "Ouganda",
"city": "Kampala"
},
{
"country": "Ukraine",
"city": "Kiev"
},
{
"country": "Émirats arabes unis",
"city": "Abou Dabi"
},
{
"country": "Angleterre",
"city": "Londres"
},
{
"country": "États-Unis",
"city": "Washington"
},
{
"country": "Uruguay",
"city": "Montevideo"
},
{
"country": "Ouzbékistan",
"city": "Tachkent"
},
{
"country": "Vanuatu",
"city": "Port-Vila"
},
{
"country": "Venezuela",
"city": "Caracas"
},
{
"country": "Vietnam",
"city": "Hanoi"
},
{
"country": "Pays de Galles",
"city": "Cardiff"
},
{
"country": "Yémen",
"city": "Sanaa"
},
{
"country": "Serbie",
"city": "Belgrade"
},
{
"country": "Zambie",
"city": "Lusaka"
},
{
"country": "Zimbabwe",
"city": "Harare"
}
	]
}
'''

data = json.loads(toto)


def removeAccents(inputString):
	nfkd_form = unicodedata.normalize('NFKD', inputString)
	only_ascii = nfkd_form.encode('ASCII', 'ignore')
	return only_ascii

def formatQuestion(inputString):
	vowels = ('a', 'e', 'i', 'o', 'u')
	if inputString[0].lower() in vowels:
		inputString = "l'" + inputString
	elif inputString[-1:] == "e":
		inputString = "la " + inputString
	return inputString

def getDifficulty():
	availableChoices = (1, 2, 3)
	print("Choisis un niveau de difficulte :\n")
	print("1 : Facile (3 erreurs possibles)\n")
	print("2 : Moyen (1 erreurs possibles)\n")
	print("3 : Difficile (0 erreurs possibles + Chronometre de 120 secondes)\n\n")
	difficulty = input("Fais un choix 1, 2 ou 3 :\n")
	if not difficulty.isdigit() or int(difficulty) not in availableChoices:
		print("\n\n\nJe n'ai pas compris")
		return getDifficulty()
	else:
		return int(difficulty)

def introduction():
	mode = str(input("Bienvenue au jeu des capitales, choisis un mode de jeu \"capitale\" ou \"pays\" : \n"))
	while mode != "capitale" and mode != "pays":
		mode = str(input("je n'ai pas compris, capitale ou pays ?\n"))
	else:
		print("Tu as choisis le mode de jeu " + mode + "\n")
	difficulty = getDifficulty()
	startQuizz(mode, difficulty)



def startScreen(mode, difficulty):
	difficultyMode = ("FACILE", "MOYEN", "DIFFICILE")
	highScore = setRecords(mode, difficulty, "0", "GET")
	print("------------------------------\n")
	print("|                            |\n")
	print("|                            |\n")
	print("|      MODE : "  + mode.upper(), end='')
	print("       |\n" if mode == "capitale" else "           |\n")
	print("|    DIFFICULTE : "  + difficultyMode[difficulty - 1].upper(), end='')
	if difficulty == 1 :
		print("     |\n")
	elif difficulty == 2 :
		print("      |\n")
	else :
		print("  |\n")
	print("|         RECORD : " + highScore + "         |\n")
	print("|                            |\n")
	print("|                            |\n")
	print("------------------------------\n")
	if difficulty == 3:
		time.sleep(1)
		print("ATTENTION LA PARTIE VA DEMARRER DANS \n")
		time.sleep(1)
		print("3\n")
		time.sleep(1)
		print("2\n")
		time.sleep(1)
		print("1\n")
		time.sleep(1)
		print("GOGOGO !\n\n")




def writeRecords(records, difficulty, score, mode):
	difficultyMode = ["FAC", "MOY", "DIF"]
	records.write("RECORD MODE " + mode.upper() + " DIFFICULTE " + difficultyMode[difficulty - 1] + " : " + str(score) + "\n")


def setRecords(mode, difficulty, score, getset = "SET"):
	if not os.path.exists("records_quizz_capitales.txt"):
		f = open("records_quizz_capitales.txt", "w")
	difficultyMode = ["FAC", "MOY", "DIF"]
	found = False
	fileData = ""
	highScore = score
	index = 34 if mode == "pays" else 38
	with open('records_quizz_capitales.txt', 'r+') as records:
		if len(records.read(1)) == 0:
			found = False
		else:
			records.seek(0)
			for line in records:
				if line.find(difficultyMode[difficulty - 1]) != -1 and line.find(mode.upper()) != -1:
					if int(line[index:]) < int(score):
						found = True
						fileData += line.replace(line[index:], score + "\n")
					else:
						highScore = int(line[index:])
				else:
					found = False
					fileData += line
		if not found and getset == "SET":
			writeRecords(records, difficulty, highScore, mode)
	if found and getset == "SET":
		with open('records_quizz_capitales.txt', 'w') as file:
			file.write(fileData)
	return str(highScore)

def verifyAnswer(answer, guess):
	answer = removeAccents(answer).decode('utf-8').lower().strip().replace("-", " ")
	guess = removeAccents(guess).decode('utf-8').lower().strip().replace("-", " ")
	if guess == answer:
		return True
	else:
		return False


def launchHardMode(mode, gameMode):
	timerStart = time.time()
	score = 0

	sec = 0
	while sec < 120:
		for country in data['quizzData']:
			sys.stdout.flush()
			if mode == "capitale":
				print("Quelle est la capitale de " + country[gameMode[0]] + "?\n")
			else:
				print("Quelle est le pays dont la capitale est " + country[gameMode[0]] + "?\n")
			guess = str(input())
			sec = int(time.time() - timerStart)
			if verifyAnswer(country[gameMode[1]], guess):
				score += 1
				print(bcolors.OKGREEN + "Bravo ! " + str(score) + " points !" +  bcolors.ENDC + "Question suivante : \n---------   \n")
				if sec > 90:
					print(bcolors.FAIL + str(120 - sec) + " secondes restantes" + bcolors.ENDC)
				else:
					print(bcolors.WARNING + str(120 - sec) + " secondes restantes" + bcolors.ENDC)
				continue
			else:
				print(bcolors.FAIL + "Faux ! " +  bcolors.ENDC)
				sec = 130
				break

	print(bcolors.OKGREEN + "FIN -- Votre score est : " + str(score) + bcolors.ENDC)

	return str(score)

def launchNormalMode(mode, gameMode, joker, difficulty):
	score = 0
	answers = {}
	
	for country in data['quizzData']:
		while joker >= 0:
			print("Question suivante : \n---------   \n")
			if mode == "capitale":
				print("Quelle est la capitale de " + formatQuestion(country[gameMode[0]]) + "?\n")
			else:
				print("Quelle est le pays dont la capitale est " + country[gameMode[0]] + "?\n")
			guess = str(input())
			if verifyAnswer(country[gameMode[1]], guess):
				score += 1
				print(bcolors.OKGREEN + "Bravo ! " + str(score) + " points !" + bcolors.ENDC + "\n")
				break
			else:
				print(bcolors.FAIL + "Faux ! " +  bcolors.ENDC)
				if difficulty == 1:
					print(bcolors.FAIL + "La reponse etait " + country[gameMode[1]] + bcolors.ENDC)
				elif difficulty == 2:
					answers[country[gameMode[0]]] = country[gameMode[1]]
				joker -= 1
				if joker > 0:
					print(bcolors.WARNING + str(joker) + " jokers restants" + bcolors.ENDC)
				elif joker == 0:
					print(bcolors.WARNING + str(joker) + " joker restant. ATTENTION ! VOUS N'AVEZ PLUS LE DROIT A l'ERREUR" + bcolors.ENDC)
				break

	print(bcolors.OKGREEN + "FIN -- Votre score est : " + str(score) + bcolors.ENDC)
	for a in answers:
		print(bcolors.WARNING + "Vous avez eu faux sur : " + a + ". La reponse etait : " + answers[a] + bcolors.ENDC)
	# print(answers)
	return str(score)




def startQuizz(mode, difficulty):
	random.shuffle(data['quizzData'])
	gameMode = ["country", "city"]
	score = 0
	if mode == "pays":
		gameMode[0], gameMode[1] = gameMode[1], gameMode[0]
	difficultyMode = (3, 1, 0)
	joker = difficultyMode[difficulty - 1]
	startScreen(mode, difficulty)
	if joker == 0:
		score = launchHardMode(mode, gameMode)
	else:
		score = launchNormalMode(mode, gameMode, joker, difficulty)
	highScore = setRecords(mode, difficulty, score)
	if (int(highScore) <= int(score) and int(highScore) > 0):
		print(bcolors.OKGREEN + "NOUVEAU RECORD POUR CE MODE" +  bcolors.ENDC + "\n")
	elif (score == "0"):
		print(bcolors.FAIL + "NUL ! 0 POINTS ! IL FAUT REESSAYER" +  bcolors.ENDC + "\n")
	else:
		print(bcolors.WARNING + "Pas mal ! Mais vous n'avez pas battu votre record de " + highScore + bcolors.ENDC + "\n")
	replay = input("Rejouer ? (oui/non)\n")
	while (replay != "oui" and replay != "non"):
		replay = input("Je n'ai pas compris, Rejouer ? (oui/non)\n")
	if replay == "oui":
		sameConfig = input("Relancer meme mode et meme difficulte ? (oui/non)\n")
		while (sameConfig != "oui" and sameConfig != "non"):
			sameConfig = input("Je n'ai pas compris. Relancer meme mode et meme difficulte ? (oui/non)\n")
		if sameConfig == "oui":
			startQuizz(mode, difficulty)
		else:
			introduction()



introduction()