#!/usr/bin/env python3

import argparse
from pymatgen.io.vasp import Poscar

def removeAtom(atom_indices, poscar_path="POSCAR"):
    """
    Purpose:
        Remove specified atoms from a POSCAR file and save a backup.

    Inputs:
        atom_indices (list of int): List of atom indices (1-based) to remove.
        poscar_path (str): Path to the POSCAR file. Defaults to "POSCAR".

    Outputs:
        None. Overwrites the POSCAR file and saves the original as POSCAR_old.
    """
    poscar = Poscar.from_file(poscar_path)
    structure = poscar.structure
    selective_dynamics = poscar.selective_dynamics or [[True, True, True] for _ in structure]
    poscar.write_file(f"{poscar_path}_old")
    indices = sorted([i - 1 for i in atom_indices], reverse=True)

    for idx in indices:
        if idx < 0 or idx >= len(structure):
            raise ValueError(f"Invalid atom index: {idx + 1}")
        del structure[idx]
        if len(selective_dynamics) > idx:
            del selective_dynamics[idx]

    poscar.structure = structure
    if selective_dynamics:
        poscar.selective_dynamics = selective_dynamics
    poscar.write_file(poscar_path)


def replaceAtom(atom_index, new_element, poscar_path="POSCAR"):
    """
    Purpose:
        Replace a specific atom in the POSCAR file with a new element.

    Inputs:
        atom_index (int): 1-based index of the atom to replace.
        new_element (str): Chemical symbol of the new element.
        poscar_path (str): Path to the POSCAR file. Defaults to "POSCAR".

    Outputs:
        None. Overwrites the POSCAR file and saves the original as POSCAR_old.
    """
    poscar = Poscar.from_file(poscar_path)
    structure = poscar.structure
    index = atom_index - 1
    if index < 0 or index >= len(structure):
        raise ValueError(f"Invalid atom index: {atom_index}")
    poscar.write_file(f"{poscar_path}_old")
    structure[index].specie = new_element
    poscar.structure = structure
    poscar.write_file(poscar_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Modify a POSCAR file.")
    subparsers = parser.add_subparsers(dest="command")

    rm_parser = subparsers.add_parser("remove", help="Remove atoms by index (1-based)")
    rm_parser.add_argument("indices", nargs="+", type=int, help="Atom indices to remove")
    rm_parser.add_argument("--poscar", default="POSCAR", help="Path to POSCAR file")

    repl_parser = subparsers.add_parser("replace", help="Replace an atom with a new element")
    repl_parser.add_argument("index", type=int, help="Atom index to replace (1-based)")
    repl_parser.add_argument("element", type=str, help="New element symbol")
    repl_parser.add_argument("--poscar", default="POSCAR", help="Path to POSCAR file")

    args = parser.parse_args()

    if args.command == "remove":
        removeAtom(args.indices, args.poscar)
    elif args.command == "replace":
        replaceAtom(args.index, args.element, args.poscar)
    else:
        parser.print_help()

