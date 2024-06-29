class Make_File:
    def __init__(self, filename):
        self.fn = open(filename, "w")

    def write_to_file(self, text, file):
        self.file = self.fn
        self.text = text
        self.file.write(str(self.text))

    def close(self, file):
        self.file = self.fn.close()
        
    def print_file(self, file):
        self.file = open(file, "r").read()
        print(self.file)




class Open_File:
    def __init__(self, file):
        self.fn = open(file, "a")
        
    def write_to_file(self, text, file):
       self.file = self.fn
       self.text = text
       self.file.write(str(self.text))

    def close(self, file):
        self.file = self.fn.close()

    def clear(self, file):
        self.file = self.fn.truncate(0)
        
    def print_file(self, file):
        self.file = open(file, "r").read()
        print(self.file)
