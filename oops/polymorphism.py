class birds:

    def sound(self):
        print("birds sounds like 'chirp', 'chirp' ")

class crow(birds): #------ inheritance
    def sound(self):
      print("crow sounds'caw' , 'caw' ")
    

parrot = birds()
bird1 = crow()

parrot.sound()
bird1.sound()


