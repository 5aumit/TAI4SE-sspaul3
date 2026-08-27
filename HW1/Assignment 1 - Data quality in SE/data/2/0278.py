import sys
import time
import pymorphy2
import pyglet
import pyttsx3
import threading
import warnings
import pytils

warnings.filterwarnings("ignore")

""" Количество раундов, вдохов в раунде, задержка дыхания на вдохе"""
rounds, breaths, hold = 4, 31, 14


def play_wav_v2(src):
    wav = pyglet.media.load(sys.path[0] + '\\src\\wav\\' + src + '.wav')
    wav.play()
    time.sleep(wav.duration)


def play_wav_inline(src):
    wav = pyglet.media.load(sys.path[0] + '\\src\\wav\\' + src + '.wav')
    wav.play()


def correct_numerals(phrase, morph=pymorphy2.MorphAnalyzer()):
    new_phrase = []
    py_gen = 1
    phrase = phrase.split(' ')
    while phrase:
        word = phrase.pop(-1)
        if 'NUMB' in morph.parse(word)[0].tag:
            new_phrase.append(pytils.numeral.sum_string(int(word), py_gen))
        else:
            new_phrase.append(word)
        py_gen = pytils.numeral.FEMALE if 'femn' in morph.parse(word)[0].tag else pytils.numeral.MALE
    return ' '.join(new_phrase[::-1])


def nums(phrase, morph=pymorphy2.MorphAnalyzer()):
    """ согласование существительных с числительными, стоящими перед ними """
    phrase = phrase.replace('  ', ' ').replace(',', ' ,')
    numeral = ''
    new_phrase = []
    for word in phrase.split(' '):
        if 'NUMB' in morph.parse(word)[0].tag:
            numeral = word
        if numeral:
            word = str(morph.parse(word)[0].make_agree_with_number(abs(int(numeral))).word)
        new_phrase.append(word)

    return ' '.join(new_phrase).replace(' ,', ',')


def speak(what):
    speech_voice = 3  # голосовой движок
    rate = 120
    tts = pyttsx3.init()
    voices = tts.getProperty("voices")
    tts.setProperty('rate', rate)
    tts.setProperty("voice_v2", voices[speech_voice].id)
    print('🔊', what)
    what = correct_numerals(what)
    tts.say(what)
    tts.runAndWait()


class Workout:

    def __init__(self, rounds=3, breaths=30, hold=15):
        self.rounds = rounds
        self.breaths = breaths
        self.hold = hold
        self.round_times = []
        self.lock = threading.Lock()  # взаимоблокировка отдельных голосовых потоков

    def __str__(self):
        return '\n♻{} 🗣{} ⏱{}'.format(self.rounds, self.breaths, self.hold)

    def __hold_breath(self):
        start_time = time.time()
        input()
        seconds = int(time.time() - start_time)
        mins = seconds // 60
        secs = seconds % 60
        self.round_times.append('{:02}:{:02}'.format(mins, secs))
        play_wav_inline('inhale')
        self.say('Глубокий вдох. ' + nums("{} минута {} секунда".format(mins, secs)))

    def __clock_tick(self):
        for i in range(self.hold):
            if i < hold - 3:
                time.sleep(1)
            else:
                play_wav_v2('clock')
        play_wav_inline('gong2')

    def __breathe_round(self, round):
        self.say('Раунд ' + str(round))
        for i in range(self.breaths):
            if i % 10 == 0:
                play_wav_inline('gong')
            play_wav_v2('inhale')
            print(i + 1, end=' ')
            play_wav_v2('exhale')
        print()
        self.say('Задерживаем дыхание на выдохе')
        self.__hold_breath()
        self.__clock_tick()
        play_wav_inline('exhale')
        self.say('Выдох')
        time.sleep(1)

    def breathe(self):
        self.say('Выполняем ' + nums(str(self.rounds) + ' раунд'))
        self.say('Каждый раунд это ' + nums(str(self.breaths) + ' глубокий вдох - и спокойный выдох'))
        self.say('Приготовились...')
        for i in range(self.rounds):
            self.__breathe_round(i + 1)
        self.say('Восстанавливаем дыхание.')

    def statistics(self):
        print('=============')
        for i in range(len(self.round_times)):
            print('Раунд', i, self.round_times[i])
        print('=============')

    def say(self, what):
        self.lock.acquire()
        thread = threading.Thread(target=speak, kwargs={'what': what})
        thread.start()
        thread.join()
        self.lock.release()


workout = Workout(rounds, breaths, hold)
workout.breathe()

workout.statistics()
