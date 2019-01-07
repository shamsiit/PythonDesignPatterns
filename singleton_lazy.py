class Singleton(object):
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print(" __init__ method called..")
        else:
            print("Instance already created : ", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()

        return cls.__instance

if __name__ == "__main__":
    s = Singleton() ## initialized but not object created
    print("object created : ", Singleton.getInstance()) # object created here

    s1 = Singleton() # object already created
