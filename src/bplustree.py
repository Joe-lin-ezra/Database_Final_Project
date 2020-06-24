import copy

class BplusTree():
    def __init__(self, D):
        self.root = ExternalNode()
        self.leaf = None
        self.D = D

    def insert(self, data):
        # data = int(data[2:])
        while True:
            if self.root:
                if type(self.root) == InternalNode:
                    if len(self.root.leaf) > 1:
                        if self.root.leaf[0] < data < self.root.leaf[len(self.root.leaf) - 1]:
                            for d in range(len(self.root.leaf)-1):
                                if data > self.root.leaf[d] and data > self.root.leaf[d+1]:
                                    continue
                                elif self.root.leaf[d] < data < self.root.leaf[d + 1]:
                                    d+1
                        elif data > self.root.leaf[len(self.root.leaf)-1]:
                            self.root.ptr[len(self.root.leaf)].data.append(data)
                            if len(self.root.ptr[len(self.root.leaf)].data) > 1:
                                self.root.ptr[len(self.root.leaf)].data.sort()
                            if len(self.root.ptr[len(self.root.leaf)].data) == self.D:
                                data = copy.copy(self.root.ptr[len(self.root.leaf)].data)
                                self.splite(data)

                    else:
                        if type(self.root.ptr[0]) == ExternalNode:
                            if data > self.root.leaf[0]:
                                self.root.ptr[1].data.append(data)
                                if len(self.root.ptr[1].data) > 1:
                                    self.root.ptr[1].data.sort()
                                if len(self.root.ptr[1].data) == self.D:
                                    data = copy.copy(self.root.ptr[1].data)
                                    self.splite(data)
                            else:
                                self.root.ptr[0].data.append(data)
                                if len(self.root.ptr[0].data) > 1:
                                    self.root.ptr[0].data.sort()
                                if len(self.root.ptr[0].data) == self.D:
                                    data = copy.copy(self.root.ptr[0].data)
                                    self.splite(data)
                        else:
                            if data < self.root.leaf[0]:
                                pass
                            else:
                                if len(self.root.ptr[1].leaf) > 1:
                                    pass
                                else:
                                    if data > self.root.ptr[1].leaf[0]:
                                        self.root.ptr[1].ptr[1].data.append(data)
                                        if len(self.root.ptr[1].ptr[1].data) > 1:
                                            self.root.ptr[1].ptr[1].data.sort()
                                        if len(self.root.ptr[1].ptr[1].data) == self.D:
                                            data = copy.copy(self.root.ptr[1].ptr[1].data)
                                            self.splite(data)
                                    else:
                                        self.root.ptr[0].data.append(data)
                                        if len(self.root.ptr[0].data) > 1:
                                            self.root.ptr[0].data.sort()
                                        if len(self.root.ptr[0].data) == self.D:
                                            data = copy.copy(self.root.ptr[0].data)
                                            self.splite(data)

                    break
                else:
                    self.root.data.append(data)
                    if len(self.root.data) > 1:
                        self.root.data.sort()
                    if len(self.root.data) == self.D:
                        data = copy.copy(self.root.data)
                        self.splite(data)
                    break
            self.root.data.append(data)
            break

    def print(self):
        print(self.root.leaf)
        for d in range(len(self.root.ptr)):
            print(self.root.ptr[d].leaf,"leaf")
            for y in range(len(self.root.ptr[d].ptr)):
                print(self.root.ptr[d].ptr[y].data,"data")


    def delete(self):
        pass

    def splite(self, data):
        if (self.D % 2) != 0:
            if type(self.root) == ExternalNode:
                self.root = InternalNode()
                self.root.leaf.append(data[int((self.D / 2))])
                self.root.ptr.append(ExternalNode())
                for d in range(self.D):
                    if d == int((self.D / 2)):
                        break
                    self.root.ptr[0].data.append(data[d])
                self.root.ptr.append(ExternalNode())
                for d in range(self.D):
                    if d < int((self.D / 2)):
                        continue
                    self.root.ptr[1].data.append(data[d])
                self.root.ptr[0].ptr=self.root.ptr[1]
                self.leaf = self.root.ptr[0]
            else:
                if type(self.root.ptr[0]) == ExternalNode:
                    for d in range(len(self.root.ptr)):
                        if len(self.root.ptr[d].data) == self.D:
                            if len(self.root.ptr) != 3:
                                self.root.leaf.append(data[int((self.D / 2))])
                                self.root.ptr.append(ExternalNode())
                                self.root.ptr[d+1].data = copy.copy(self.root.ptr[1].data)
                                self.root.ptr[d].data.clear()
                                self.root.ptr[d].data.append(data[int((self.D / 2))-1])
                                self.root.ptr[d+1].data.remove(data[int((self.D / 2))-1])
                                self.root.ptr[d].ptr = self.root.ptr[d+1]
                            else:
                                self.root.leaf.append(data[int((self.D / 2))])
                                self.root.ptr[d].data.remove(data[int((self.D / 2)) - 1])
                                if len(self.root.leaf) == self.D:
                                    tmp = InternalNode()
                                    tmp.leaf.append(data[int((self.D / 2))-1])
                                    tmp.ptr.append(InternalNode())
                                    for d in range(self.D):
                                        if d == int((self.D / 2)):
                                            break
                                        tmp.ptr[0].leaf.append(self.root.leaf[d])
                                    tmp.ptr[0].ptr.append(self.root.ptr[0])
                                    tmp.ptr[0].ptr.append(self.root.ptr[1])
                                    tmp.ptr.append(InternalNode())
                                    for d in range(self.D):
                                        if d != int((self.D / 2)):
                                            continue
                                        tmp.ptr[1].leaf.append(self.root.leaf[d]+1)
                                    tmp.ptr[1].ptr.append(ExternalNode())
                                    tmp.ptr[1].ptr[0].data.append(data[int((self.D / 2))-1])
                                    tmp.ptr[1].ptr.append(self.root.ptr[2])
                                    self.root = tmp
                else:
                    print(data)
        else:
            if type(self.root) == ExternalNode:
                self.root = InternalNode()
                self.root.leaf.append(data[int((self.D / 2))])
                self.root.ptr.append(ExternalNode())
                for d in range(self.D):
                    if d == int((self.D / 2)):
                        break
                    self.root.ptr[0].data.append(data[d])
                self.root.ptr.append(ExternalNode())
                for d in range(self.D):
                    if d < int((self.D / 2)):
                        continue
                    self.root.ptr[1].data.append(data[d])

            else:
                pass

    def search(self):
        pass


class InternalNode():
    def __init__(self):
        self.leaf = []
        self.ptr = []


class ExternalNode():
    def __init__(self):
        self.data = []
        self.ptr = None
