# How to Run

```
>python hash-and-salt-eg.py
Enter your username: user1
Enter your password:
Login successful!
```

```
>python hash-and-salt-eg.py
Enter your username: user2
Enter your password:
Incorrect password.
Enter your password:
Incorrect password.
Enter your password:
Incorrect password.
Too many failed attempts. Try again later.
```

```
>type user_data.json
{"user1": {"salt": "acc697ad1a2b4eae460243505532ae76", "hash": "2d415fadb8aa1af70fd8e1b2a12517338ae1850f72da7a7f27d2be1e46a9cfec"}, "user2": {"salt": "6621ee17c38aac3f800c73424d82250a", "hash": "85814273a0b2384be19777f243075582741de0813bc4792ccc15b93829bbae88"}, "user3": {"salt": "556882c9469f659bb58c752ff7913cd5", "hash": "5740ed384b3cf692e20b115e92ef9a193854b1dd3bf3936bbd393ca929c118dc"}}
```
