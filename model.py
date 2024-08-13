class Ball:

    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.clicked = False

    def move(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]

    def set_clicked(self):
        self.clicked = True

    def set_unclicked(self):
        self.clicked = False

