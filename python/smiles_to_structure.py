## Written by Ye Kyaw Thu, LU Lab., Myanmar
## SMILES to molecule figure generation

import sys
import argparse
from rdkit import Chem
from rdkit.Chem import Draw

def generate_structure(smiles):
    molecule = Chem.MolFromSmiles(smiles)
    if molecule is None:
        raise ValueError("Could not parse SMILES string.")
    return molecule

def main():
    parser = argparse.ArgumentParser(description="Generate a molecule structure from a SMILES string.")
    parser.add_argument("smiles", help="SMILES string of the molecule")
    parser.add_argument("--output", help="Output image file name", default="molecule.png")
    args = parser.parse_args()

    smiles = args.smiles
    output_file = args.output

    try:
        molecule = generate_structure(smiles)
        img = Draw.MolToImage(molecule)
        img.save(output_file)
        print(f"Molecule image saved as {output_file}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
