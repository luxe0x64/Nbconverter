import os
from moviepy import *
from time import sleep

###################################################################################
#                           Made by: nobody3132 aka luxe0x64                      #
#                               Date: 14 February 2025                            #
#                               Happy Vilentine's day                             #
###################################################################################



class Convert:
    def __init__(self):
        os.system('clear')
        os.system('cat nbconverver_banner.txt')
        self.name_of_file_to_convert = None
        self.converted_file_name = None
        self.format = None
    pass


    def Formats(self):
        print("supported formats: mp3 mp4 m4a avi etc.")
        self.format = input("Enter file format TO convert: ")
        print(f"Format selected: {self.format}")
        sleep(3)
        os.system("clear")
        os.system('cat nbconverver_banner.txt')
        os.system('ls')
    pass
        
    def Converting(self):
        self.name_of_file_to_convert = input("Enter the name of file with extensions example: music.mp3\nEnter the name of file to convert: ")
        try:
            os.system('ls | grep ' + self.name_of_file_to_convert)
            print("Found. ")
            print("Name of the file to convert: " + self.name_of_file_to_convert)
            self.converted_file_name = input("Enter converted file name, example: music.m4a\nEnter converted file name: ")
            print("Converting... ")
            try:
                video = VideoFileClip(os.path.join(self.name_of_file_to_convert))
                video.audio.write_audiofile(os.path.join(self.converted_file_name))
                print("Converted. " + "File saved as: " + self.converted_file_name)
            except Exception as e:
                print("Something went wrong.... ")
                print(e)
        except Exception as e:
            print("File not found. ")
            print(e)
    pass


ConverProgram = Convert()
ConverProgram.Converting()
