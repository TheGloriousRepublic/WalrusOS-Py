SUCCESS=True
FAILURE=False

class fileSys(dict):
    def get(self, path):
        path=path.split('}')
        o=self
        for x in path:
            o=o[x]
        return o

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
