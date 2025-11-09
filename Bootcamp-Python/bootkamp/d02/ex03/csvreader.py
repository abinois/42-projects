class CsvReader():
    def __init__(self, file, sep=',', header=False, skip_top=0, skip_bottom=0):
        if type(file) is not str:
            exit('Invalid path.')
        self.file = file
        if type(sep) is not str:
            exit('Invalid separator.')
        self.sep = sep
        if type(header) is not bool:
            exit('Expected bool for argument header.')
        self.header = header
        if type(skip_top) is not int or type(skip_bottom) is not int:
            exit('Expected int for arguments skip_top and skip_bottom.')
        self.s_top = skip_top
        self.s_bot = skip_bottom

    def __enter__(self):
        try:
            self.fd = open(self.file, 'r')
            self.content = self.fd.readlines()
            if self.header:
                self.header = self.content[0].replace('\n', '').split(self.sep)
            if self.s_top > 0 and self.s_top < len(self.content):
                self.content = [line for line in self.content[self.s_top::]]
            if self.s_bot > 0 and self.s_bot < len(self.content):
                self.content = [line for line in self.content[:len(self.content) - self.s_bot:]]
            self.content = [line.replace('\n', '').split(self.sep) for line in self.content]
            return self
        except FileNotFoundError:
            exit('File not found.')

    def __exit__(self, exception_type, exception_value, traceback):
        if exception_type:
            exit(exception_value)
        try:
            self.fd.close()
        except:
            exit('Problem closing the file.')
    
    def getdata(self):
        return self.content
    
    def getheader(self):
        if self.header:
            return self.header


if __name__ == "__main__":

    with CsvReader('file.txt', header=True, skip_bottom=1, skip_top=1) as file:
        data = file.getdata()
        print(data)
        header = file.getheader()
        print(header)
    
    with CsvReader('not_a_file.txt', sep=' ') as file:
        file.getdata()
