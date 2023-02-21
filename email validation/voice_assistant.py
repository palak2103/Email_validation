import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():#speech to text
    recognizer =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data =recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand") 
def speechtx(x): #text to speech
    engine = pyttsx3.init()  
    voices= engine.getProperty('voices')   
    engine.setProperty('voice', voices[1].id) #male=[0], female=[1]
    rate= engine.getProperty('rate')   
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ =='__main__':

    # if sptext().lower() == "name":

        data1=sptext().lower()
        if "your name" in data1:
            name = "my name is peter"
            speechtx(name)

        elif "old are you"  in data1:
            age ="i am just 21 year old" 
            speechtx(age)  

        elif "time" in data1:
            time =datetime.datetime.now().strftime("%I%M%p")#hpur %I
            speechtx(time)

        elif "youtube" in data1:
            webbrowser.open("https://youtu.be/MSr8DoNbQgc") 

        elif "website" in data1:
            webbrowser.open("https://www.w3schools.com/html/default.asp") 

        elif"joke"  in data1:
            joke_1= pyjokes.get_joke(language="en", category="neutral") 
            print(joke_1) 
            speechtx(joke_1)       

        elif "shiv"  in data1:
             webbrowser.open("https://youtu.be/HC3-gSNbx00")             
    # else:
    #     print("thanks")

# speechtx("tu man meri jaan tujhe jane na")    
# sptext()     



