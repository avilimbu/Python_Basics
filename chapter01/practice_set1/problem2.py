#Install an external module and perform some operation



#pyttsx3 module is used to change text into voice
import pyttsx3 
engine = pyttsx3.init()
engine.say("I am learning the python with dedication")
engine.runAndWait()