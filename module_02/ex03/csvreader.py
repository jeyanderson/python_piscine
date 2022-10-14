from unittest import skip


class CsvReader():
    def __init__(self,filename=None,sep=',',header=False,skip_top=0,skip_bottom=0):
        self.missing=False
        self.corrupted=False
        self.data=[]
        try:
            self.file=open(filename)
        except:
            self.missing=True
        else:
            ncolumns=None
            if header:
                self.header=self.file.readline().rstrip().split(sep)
                ncolumns=len(self.header)
            for i in range(skip_top):
                self.file.readline()
            while True:
                line=self.file.readline().rstrip()
                if not line:
                    break
                sline=line.split(sep)
                if '' in sline:
                    self.corrupted=True
                    break
                length=len(sline)
                if ncolumns and ncolumns!=length:
                    self.corrupted=True
                    break
                ncolumns=length
                self.data.append(sline)
                if skip_bottom:
                    self.data=self.data[:-skip_bottom]




    def __enter__(self):
        if self.missing or self.corrupted:
            return None
        return self

    
    def __exit__(self,exc_type,exc_value,tb):
        if not self.missing:
            self.file.close


    def getdata(self):
        return self.data

    
    def getheader(self):
        return self.header if self.header else None

with CsvReader('bad.csv',header=True)as file:
    if not file:
        print('File is corrupted.')