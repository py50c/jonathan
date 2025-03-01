import time
import pyfiglet
import os
import art
while True:
	try:
		study_min = int(input("How many minutes do you want to study : "))
		study_hour = study_min // 60
		study_min = study_min % 60
		study_sec = 0
		while study_sec >= 0:
			os.system("clear")
			hour_str = str(study_hour)
			min_str = str(study_min)
			sec_str = str(study_sec)
			art_hour = art.text2art(hour_str,font = "small")
			art_min = art.text2art(min_str,font = "small")
			art_sec = art.text2art(sec_str,font ="small")
			print(f"{art_hour}:{art_min}:{art_sec}")
			study_sec -= 1
			time.sleep(1)
			if study_sec < 0:
				study_min -= 1
				study_sec = 59
			if study_min < 0:
				study_hour -=1
				study_min = 59
			if study_min <= 0 and study_hour <= 0 and study_sec == 0:
				break
		os.system("clear")
		end_message = pyfiglet.figlet_format("TIME IS UP")
		print(end_message)
		cont = input("would you like to time yourself again \n if yes press any key if no press 'q' : ")
		if cont == "q":
			print("....\nDONE")
			break
		else:
			True
			print("....\n....\n")
	except ValueError:
		print("Enter an integer ")
	
