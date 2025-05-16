#!/usr/bin/env python3

import sys
from Dope import Dope
def runCalcs(dopeName, objectDir, uCorr, pseudo):
    dopant= Dope(dopeName, objectDir, uCorr, pseudo)
    dopant.pristine()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./script.py dopeName storageDir uCorr pseudo")
        sys.exit(1)
    runCalcs(*sys.argv[1:])
