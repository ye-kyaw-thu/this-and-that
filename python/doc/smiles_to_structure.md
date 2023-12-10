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

Output png file:  
![N1CC2CCCCC2CC1](https://github.com/ye-kyaw-thu/this-and-that/blob/main/python/fig/smiles/N1CC2CCCCC2CC1.png)  

```
python ./smiles_to_structure.py C1=CC=C1
```
Output png file:  
![C1=CC=C1](https://github.com/ye-kyaw-thu/this-and-that/blob/main/python/fig/smiles/C1%3DCC%3DC1.png)  

```
python ./smiles_to_structure.py C1=CC=CC=C1
```
Output png file:  
![C1=CC=CC=C1](https://github.com/ye-kyaw-thu/this-and-that/blob/main/python/fig/smiles/C1%3DCC%3DCC%3DC1.png)

```
python ./smiles_to_structure.py C1OC=CC=1
```
Output png file:  
![C1OC=CC=1](https://github.com/ye-kyaw-thu/this-and-that/blob/main/python/fig/smiles/C1OC%3DCC%3D1.png)

```
python ./smiles_to_structure.py "F/C=C/F"
```
Output png file:  
![F/C=C/F](https://github.com/ye-kyaw-thu/this-and-that/blob/main/python/fig/smiles/FslashC%3DCslashF.png)

```
python ./smiles_to_structure.py 
```
Output png file:  
![[NH4+].[NH4+].[O-]S(=O)(=O)[S-]](https://github.com/ye-kyaw-thu/this-and-that/blob/main/python/fig/smiles/%5BNH4%2B%5D.%5BNH4%2B%5D.%5BO-%5DS(%3DO)(%3DO)%5BS-%5D.png)

```
python ./smiles_to_structure.py c1ccccc1-c2ccccc2
```
Output png file:  
![c1ccccc1-c2ccccc2](https://github.com/ye-kyaw-thu/this-and-that/blob/main/python/fig/smiles/c1ccccc1-c2ccccc2.png)


## References

[1]. https://opensmiles.org/opensmiles.html  
