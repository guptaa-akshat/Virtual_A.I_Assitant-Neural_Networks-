import speech_recognition as sr      #pip install speech_recognition

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,0,5)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-US")
        print(f"You Said : {query}")
    except:
        return ""

    query = str(query)
    return query.lower()

Listen()