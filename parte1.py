# -*- coding: utf-8 -*-
import os

comeco = input("Digite a hora de começo: ")
fim = input("Digite a hora de fim: ")

def main():
    cmd = "ffmpeg -i /home/marcos/Downloads/input.mp4 -ss " + comeco + " -to " + fim + " -c:v copy -c:a copy /home/marcos/Downloads/output.mp4"
    returned_value = os.system(cmd)  # returns the exit code in unix
    print('returned value:', returned_value)
    return returned_value

main()
