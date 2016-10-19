from db_handler import DB_Handler
from random import randint


class test:
    def __init__(self):
        print ">>> {}".format("Talk to me!")

        self.DBH = DB_Handler()


    def example(self):
        # print(">>> Getting all the phrases")

        phrases = self.DBH.get_all_phrases()

        #-1 because len doesn't start counting from 0..
        print(phrases[randint(0,len(phrases)-1)][1])
