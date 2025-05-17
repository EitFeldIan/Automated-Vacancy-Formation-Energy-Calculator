import os
import shutil
import sys
sys.path.append('/home/ef35/Automated-Vacancy-Formation-Energy-Calculator')
from cpFile import cpFile
from modPoscar import modPOSCAR
import subprocess
import pdb


class Dope:
    def __init__(self, dopeName, objectDir, uCorr, pseudo):
        self.dopeName = dopeName
        self.uCorr = uCorr

        # This is either "_pv", "_sv", or ""
        self.pseudo = pseudo
        self.objectDir = os.path.abspath(objectDir)
        self.pristineDir = ""
        self.topODir = ""
        self.vacanciesDir = ""
        self.jobs = {}
        self.functionPath = "/home/ef35/Automated-Vacancy-Formation-Energy-Calculator"
        self.isContinuous = False


    # Functions
    def runAll(self):
        self.isContinuous = True
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

    def __setup(self):
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

        os.chdir(self.objectDir)

        pbePath = "~/work/tsenftle/software/vasp/potpaw_pbe/"

        #TODO: Add something here if they try to use a pseudo that doesn't exist in the folder
        command = "cat " + pbePath + "O/POTCAR " + pbePath + "Ru/POTCAR " + pbePath + self.dopeName + self.pseudo + "/POTCAR> POTCAR"
        subprocess.run(command, shell=True, text=True)

        cpFile("INCAR", self.objectDir)

        subprocess.run(["sed", "-i", f"/^LDAUU/s/ u / {self.uCorr} /", "INCAR"], check=True)

        #TODO: I need different version of vasp.slurm
        

    def pristine(self):

        self.__setup()

        os.makedirs("pristine")
        os.chdir("pristine")
        self.pristineDir = os.path.join(self.objectDir, "pristine")


        #TODO: Check whether all of these are working as intended
        self.jobs["pristine"] = {"1CUSO": "Not submitted", "2CUSnoO": "Not submitted", "3subCUS": "Not submitted", "4Bridge": "Not submitted", "5subBridge": "Not submitted"}
        dopeAtomInd = {"1CUSO": 196, "2CUSnoO": 196, "3subCUS": 173, "4Bridge": 189, "5subBridge": 180}
        removeAtomsInd = {"1CUSO": None, "2CUSnoO": 132, "3subCUS": None, "4Bridge": None, "5subBridge": None}

        for job in self.jobs["pristine"]:
            os.makedirs(job)
            jobPath = os.path.join(self.pristineDir, job)
            os.chdir(jobPath)

            cpFile(["POSCAR", "KPOINTS"], jobPath)
            modPOSCAR(os.path.join(jobPath, "POSCAR"), self.dopeName, dopeAtomInd[job], removeAtomsInd[job])

            #TODO: Have different vasp.slurm behavior depending on isContinuous
            #TODO change vasp.slurm so the job name is different for every run

            if not self.isContinuous:
                cpFile(["vasp.slurm"], jobPath)
                pdb.set_trace()
                subprocess.run(["sed", "-i", f's/^#SBATCH --job-name=.*/#SBATCH --job-name={job}/', "vasp.slurm"], check=True)

            shutil.copy2(os.path.join(self.objectDir, "POTCAR"),os.path.join(jobPath, "POTCAR"))
            shutil.copy2(os.path.join(self.objectDir, "INCAR"),os.path.join(jobPath, "INCAR"))


            #TODO: Run sbatch

            os.chdir(self.pristineDir)


    def topO(self):
        pass

    def vacancies(self):
        pass

    # Getters
    def get_dopeName(self):
        return self.dopeName

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
