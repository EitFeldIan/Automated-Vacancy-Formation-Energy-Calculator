#! /home/ef35/miniconda3/bin/python
from pymatgen.io.vasp import Poscar
from pymatgen.core import Element
import sys
import argparse


def modPOSCAR(POSCARpath, elemName, replaceAtomInd, removeAtomsInd):
    if replaceAtomInd !=None:
        replaceAtom(POSCARpath, replaceAtomInd, elemName)
        
    if removeAtomsInd !=None:
        removeAtoms(POSCARpath, removeAtomsInd)

def removeAtoms(POSCARpath, atoms, test=False):
    # Load POSCAR
    poscar = Poscar.from_file(POSCARpath)
    structure = poscar.structure
    if test:
        poscar.write_file(POSCARpath + "_old")

    # Atoms should be 0 indexed and sort in reverse so that there is no index shifting
    atomInds = [atom - 1 for atom in atoms]  
    atomInds.sort(reverse=True)  

    for atomInd in atomInds:
        if atomInd < 0 or atomInd >= len(structure):
            print(f"Invalid atom index: {atomInd + 1}")
            sys.exit(1)
        del structure[atomInd]

    poscar.write_file(POSCARpath)

    if test:
        print("Success!")

def replaceAtom(POSCARpath, atomInd, elemName, test=False):
    # Load POSCAR
    poscar = Poscar.from_file(POSCARpath)
    structure = poscar.structure

    if test: 
        poscar.write_file(POSCARpath + "_old")
    
    # Zero index
    atomInd -= 1

    if atomInd < 0 or atomInd >= len(structure):
        print(f"Invalid atom index: {atomInd + 1}")
        sys.exit(1)

    elem = Element(elemName)  
    elemCoords = structure[atomInd].frac_coords

    sd = None
    if "selective_dynamics" in structure[atomInd].properties:
        sd = structure[atomInd].properties["selective_dynamics"]

    if sd is not None:
        structure.append(elem, elemCoords, properties={"selective_dynamics": sd})
    else:
        structure.append(elem, elemCoords)

    del structure[atomInd]

    poscar.write_file(POSCARpath)

    if test:
        print("Success!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Modify atoms in a POSCAR file.")
    parser.add_argument("poscar_path", type=str, help="Path to the POSCAR file")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Remove atoms subcommand
    parser_remove = subparsers.add_parser("remove", help="Remove atoms from POSCAR")
    parser_remove.add_argument("indices", type=int, nargs='+', help="Indices of atoms to remove (1-based)")
    parser_remove.add_argument("--test", action="store_true", help="If set, create backup and print success message")

    # Replace atom subcommand
    parser_replace = subparsers.add_parser("replace", help="Replace an atom in POSCAR")
    parser_replace.add_argument("index", type=int, help="Index of atom to replace (1-based)")
    parser_replace.add_argument("element", type=str, help="New element symbol")
    parser_replace.add_argument("--test", action="store_true", help="If set, create backup and print success message")

    args = parser.parse_args()

    if args.command == "remove":
        removeAtoms(args.poscar_path, args.indices, args.test)
    elif args.command == "replace":
        replaceAtom(args.poscar_path, args.index, args.element, args.test)


