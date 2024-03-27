import speech_recognition as sr

# Создаем объект Recognizer
recognizer = sr.Recognizer()

# Записываем аудио с микрофона
with sr.Microphone() as source:
    print("Скажите что-нибудь:")
    audio = recognizer.listen(source)

# Распознаем речь с использованием Google Web Speech API
try:
    text = recognizer.recognize_google(audio, language="ru-Ru")
    print("Вы сказали: " + text)
except sr.UnknownValueError:
    print("Извините, не удалось распознать речь")
except sr.RequestError as e:
    print("Ошибка при запросе к сервису Google Web Speech API; {0}".format(e))
