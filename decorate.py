import base64

class Printdict(dict):
    def print(self):
        print()
        for k in self.keys():
                self.decorate(k)

    def decorate():
        pass

class Requestclass(Printdict):
    def decorate(self, k):
        print("-" * 30)
        print(k + "  :   " + str(self[k]))

class Numclass(Printdict):
    def decorate(self, k):
        print("{:5}".format(k) + "  :  " + str(self[k]))

def main():
    requestdict = Requestclass()
    numdict = Numclass()
    path = "/var/log/wowhoneypot/access_log"
    
    with open(path) as file:
        for f in file:
            s = f.split(" ")
            print(printlist(s[:-1]))
            print("-" * 40)
            print(base64.b64decode(s[-1]))
            print("=" * 60)
            num = s[-2]
            req = s[0] + " " + s[1]
            
            if num in numdict:
                numdict[num] = numdict[num] + 1
            else:
                numdict[num] = 1
            
            if req in requestdict:
                requestdict[req] = requestdict[req] + 1
            else:
                requestdict[req] = 1

    requestdict.print()
    numdict.print()

def printlist(list_data):
    for l in list_data:
        print(l, end=" ")


if __name__ == "__main__":
    main()
