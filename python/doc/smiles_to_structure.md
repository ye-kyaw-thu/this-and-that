# SMILES to Molecule Structure Generation

## Basic Concepts of SMILES

 SMILES (Simplified Molecular Input Line Entry System) is a notation that allows a user to represent a chemical structure in a text format. It's widely used in cheminformatics and is valuable for storing and transferring data about molecular structures.
 
- Atoms: In SMILES, atoms are represented by their elemental symbols from the periodic table. For example, carbon is represented as 'C', hydrogen as 'H', oxygen as 'O', etc.
- Bonds: Single bonds are not explicitly represented. For double, triple, and aromatic bonds, '=', '#', and ':' are used, respectively.
- Branching: Parentheses are used to indicate branch points. For example, in ethane ('CC'), adding a methyl group on the first carbon is written as 'C(C)C'.

## rdkit Library Installation

```
(base) yekyaw.thu@gpu:~/exp/code$ pip install rdkit
Keyring is skipped due to an exception: 'keyring.backends'
Defaulting to user installation because normal site-packages is not writeable
Collecting rdkit
  Downloading rdkit-2023.3.2-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (29.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 29.5/29.5 MB 1.5 MB/s eta 0:00:00
Requirement already satisfied: numpy in /opt/anaconda/anaconda3/lib/python3.7/site-packages (from rdkit) (1.18.1)
Requirement already satisfied: Pillow in /opt/anaconda/anaconda3/lib/python3.7/site-packages (from rdkit) (7.0.0)
Installing collected packages: rdkit
Successfully installed rdkit-2023.3.2

[notice] A new release of pip available: 22.3 -> 23.3.1
[notice] To update, run: pip install --upgrade pip
(base) yekyaw.thu@gpu:~/exp/code$
```

## Example Runnings

```
python ./smiles_to_structure.py N1CC2CCCCC2CC1
```

```

```

```

```

```

```

```

```

## References

[1]. https://opensmiles.org/opensmiles.html  
