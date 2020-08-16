import speech_recognition as sr

def speech_to_text(*words):

	microphone=sr.Microphone()
	r=sr.Recognizer()
	with microphone as source:
		for i in words:
			for j in i:
				print(f"Please say:{j}")
				r.adjust_for_ambient_noise(source)
				audio=r.listen(source)
				spoken=r.recognize_google(audio)
				spoken=spoken.lower()
				if spoken==j:
					print("That was correct")
				else:
					print(f"You said, {spoken}. That was incorrect")

            
def audio_to_text(audiofile):
	sound_file=sr.AudioFile(audiofile)
	r=sr.Recognizer()

	with sound_file as source:
		audio=r.record(source)
		recognized=r.recognize_google(audio)
		print(recognized)
		




if __name__=="__main__":


	words = ['apple', 'banana', 'grape', 'orange', 'mango', 'lemon']
	#speech_to_text(words)
	