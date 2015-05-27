SUCCESS=True
FAILURE=False
DEFAULTIMG='icon}'

class WFile(dict):
    pass

class fileSys(dict):
    def get(self, path):
        path=path.split('}')
        o=self
        for x in path:
            o=o[x]
        return o

    def create(self, path):
        pass
        
    def delete(self, path):
        path=path.split('}')
        sub = self
        for i in path[:-1]:
            sub = sub[i]
        del sub[path[-1]]
        self=sub
        return SUCCESS

    def rename(self, path, newName):
        path=path.split('}')
        sub = self
        for i in path[:-1]:
            sub = sub[i]
        sub[path[-1]]
        return FAILURE

class icon:
    def __init__(self, path, img=None):
        self.path=path
        if img:
            self.imgpath=img
        else:
            self.imgpath=DEFAULTIMG
        
    def setIcon(self, img):
        self.imgpath=img

    def setPath(self, path):
        self.path = path

    def delete(self):
        del self
