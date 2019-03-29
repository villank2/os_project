
class File():
    def __init__(self,size,ctime,mtime,maxlen):
        self.size = size
        self.ctime = ctime
        self.mtime = mtime
        self.maxlen = maxlen

    def __str__(self):
        return ("{:{}} {:>10} {:<20} {:<20}".format(filename,maxlen,self.size,self.ctime,self.mtime))
