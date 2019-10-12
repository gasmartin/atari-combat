from os import system


def play_shoot():
    system("aplay assets/shoot.wav")


def play_explosion():
    system("aplay assets/explosion.wav")
