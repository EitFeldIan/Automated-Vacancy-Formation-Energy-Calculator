#!/usr/bin/env python3

import sys

def runCalcs(dopantName, storageDir, uCorr, pseudo):
    dopant = dope(dopantName, storageDir, uCorr, pseudo)
    dopant.runAll()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./script.py dopeElem storageDir uCorr pseudo")
        sys.exit(1)
    runCalcs(*sys.argv[1:])
