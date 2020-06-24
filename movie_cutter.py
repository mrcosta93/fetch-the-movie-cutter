# -*- coding: utf-8 -*-
import os

comeco = input("Digite a hora de começo: ")
fim = input("Digite a hora de fim: ")
nome = input("Entre com o nome do arquivo: ")

def main():
    cmd = "ffmpeg -i " + nome + " -ss " + comeco + " -to " + fim + " -c:v copy -c:a copy ~/Downloads/output-fetch.mp4"
    returned_value = os.system(cmd)  # returns the exit code in unix
    print('returned value:', returned_value)
    return returned_value

main()