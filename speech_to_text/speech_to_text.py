import speech_recognition as sr 


r = sr.Recognizer()




# codigo para gravação de audio
# with sr.Microphone() as source:
#     r.adjust_for_ambient_noise(source)
#     print("Please say something")
#     audio = r.listen(source)
#     print("Recognizing Now .... ")
 
 
#     # recognize speech using google
 
#     try:
#         print("You have said \n" + r.recognize_google(audio,language='pt-BR'))
#         print("Audio Recorded Successfully \n ")
 
 
#     except Exception as e:
#         print("Error :  " + str(e))
 
#     # # write audio
#     # with open("recorded.wav", "wb") as f:
#     #     f.write(audio.get_wav_data())
 