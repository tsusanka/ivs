# -*- coding: utf-8 -*-

from config import *
from enums import *

if is_production():
    from naoqi import ALProxy

def getISeeSentence(shape, color, count):
    count = int(count)
    if count == 0:
        return "Nic nevidím"
    sentence = "Vidím "
    if count == 1:
        sentence += "jeden"
    elif count == 2:
        sentence += "dva"
    else:
        sentence += str(count)
    sentence += " "

    if color == "blue":
        if count > 4:
            sentence += "modrých"
        elif count > 1:
            sentence += "modré"
        elif count == 1:
            sentence += "modrý"
    if color == "yellow":
        if count > 4:
            sentence += "žlutých"
        elif count > 1:
            sentence += "žluté"
        elif count == 1:
            sentence += "žlutý"
    if color == "red":
        if count > 4:
            sentence += "červených"
        elif count == 1:
            sentence += "červený"
        elif count > 1:
            sentence += "červené"

    sentence += " "

    if shape == Shape.TRIANGLE:
        sentence += "trojúhelník"
    if shape == Shape.HEXAGON:
        sentence += "hexagon"
    if shape == Shape.RECTANGLE:
        sentence += "obdelník"
    if shape == Shape.CIRCLE:
        sentence += "kruh"

    if count > 4:
        sentence += "ů"
    elif count > 1:
        sentence += "y"
    return sentence


def sayISee(shape, color, count):
    sentence = getISeeSentence(shape, color, count)
    if is_production():
        tts = ALProxy("ALTextToSpeech", ROBOT_IP, ROBOT_PORT)
        tts.setLanguage("Czech")
        tts.say(sentence);
    else:
        print("Saying: '" + sentence + "'")
