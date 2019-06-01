import base64

class Printdict(dict):
    def print(self):
        print()
        for k in self.keys():
                self.decorate(k)

    def decorate():
        pass

class Urlclass(Printdict):
    def decorate(self, k):
        print("-" * 30)
        print(k + "  :   " + str(self[k]))

class Numclass(Printdict):
    def decorate(self, k):
        print("{:5}".format(k) + "  :  " + str(self[k]))

def main():
    urldict = Urlclass()
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
            if num in numdict:
                numdict[num] = numdict[num] + 1
            else:
                numdict[num] = 1

    urldict.print()
    numdict.print()

def printlist(list_data):
    for l in list_data:
        print(l, end=" ")


if __name__ == "__main__":
    main()
