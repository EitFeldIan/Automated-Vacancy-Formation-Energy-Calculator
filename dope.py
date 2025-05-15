class dope:
    def __init__(self, dopantName, objectDir, uCorr, pseudo):
        self.dopantName = dopantName
        self.uCorr = uCorr
        self.pseudo = pseudo
        self.objectDir = objectDir
        self.pristineDir = None
        self.topODir = None
        self.vacanciesDir = None
        self.jobs = None

    # Functions
    def calculate(self):
        pass

    def notify(self):
        pass

    def pristine(self):
        pass

    def topO(self):
        pass

    def vacancies(self):
        pass

    # Getters
    def get_dopantName(self):
        return self.dopantName

    def get_uCorr(self):
        return self.uCorr

    def get_pseudo(self):
        return self.pseudo

    def get_objectDir(self):
        return self.objectDir

    def get_pristineDir(self):
        return self.pristineDir

    def get_topODir(self):
        return self.topODir

    def get_vacanciesDir(self):
        return self.vacanciesDir

    def get_jobs(self):
        return self.jobs
