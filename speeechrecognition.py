import speech_recognition as sr
def main():
    r= sr.Recognizer()  #recognize the voice what we speak
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) #clear noise 
    
        print("Please speak something")
    
        audio = r.listen(source)
    
        print("Recognizing now....")
    
        #recognize speech using google
    
        try:
            print("You have said: \n" + r.recognize_google(audio))
            print("Audio Recorded Successfully \n")
        
        except Exception as e:
            print("Error: " + str(e))
        
        
        #write audio
        
        with open("recorded.wav", "wb") as f:    #wb---> write binary
            f.write(audio.get_wav_data())    #save the audio in the file

if __name__ == "__main__":
    main()

#commit  git
#commit 2