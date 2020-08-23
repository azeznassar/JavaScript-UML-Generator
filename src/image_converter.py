
from plantuml import PlantUML

class ImageConverter():

    def __init__(self):
        self.plant = PlantUML(url='http://www.plantuml.com/plantuml/img/')


    def produce_image_a(self):
        #self.plant.processes_file("dot.txt")
        pass

    def produce_image_b(self):
        self.plant.processes_file("dot.txt")

