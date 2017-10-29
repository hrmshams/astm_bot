class FileImplementer:

    @staticmethod
    def rewrite_file(address, string):
        file = open(address, "w")
        file.write(string)
        file.close()

    @staticmethod
    def read_file(address):
        file = open(address, "r")
        string = file.read()
        file.close()

        return string
