import os
import shutil

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
        self.vaspPath = None

    # Functions
    def runAll(self):
        pass


    def notify(self):
        """
        This will be some function such that it will be called after a job is finished and you're in runAll mode. Pretty much notify will check if the necessary jobs have reached completed status.
        If they have, it will call the next step (either topO or vacancies)
        """
    def updateStatus(self, status):
        """
        The status of all jobs will start as None. Other statuses include submitted, begun, completed, failed.
        """
        pass

    def setup(self):
        """
        This will pretty much initialize values, put vasp.slurms in the right place, establish which jobs will be run. That sort of thing
        
        """

        # Check if the directory already exists. If it does, ask if it should be removed. 
        if os.path.exists(self.objectDir):
            print("It looks as though this directory has been used before. Are you sure you want to restart?")
            response = input("Enter your response (y is yes and anything else is no): ")
            if response != "y":
                raise Exception("Directory has been used before. Not overwriting")
            else:
                shutil.rmtree(self.objectDir)
                os.makedirs(self.objectDir)

        else:
            os.makedirs(self.objectDir)

        #TODO This needs to deal with modifying vasp.slurm when necessary
        

    def pristine(self):
        self.setup()
        self.jobs["pristine"] = {"1CUSO": "Not submitted", "2CUSnoO": "Not submitted", "3subCUS": "Not submitted", "4Bridge": "Not submitted", "5subBridge": "Not submitted"}
        for job in self.jobs["pristine"]:
            

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
