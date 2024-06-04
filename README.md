# lockenv - encrypt and decrypt env files easily

A Helper pip package for encrypting env's to be stored safely in code repositories


### Assumptions:

+ Assuming python3 is installed on your system.
+ Nano is installed on your system
+ If you have VScode installed, better !


Install `lockenv` on your system using : 

```
pip install lockenv
```

## Encryption Options

```
lockenv
```

+ Running the command will check for any 'fkey' files in the current path, if found will read the key, if not it will prompt to generate a new key:




+ environment specific

```
ferncrypter -e production
```


+ Pass key manually

```
ferncrypter -e production -k keyfile or key-string
```

## Decryption Options

+ Decrypt env

```
ferncrypter -d
```

+ Environment specific

```
ferncrypter -d -e production
```

+ Pass key manually
+ Recomended option if using inside pipelines or scripts

```
ferncrypter -d -e production -k keyfile or key-string
```
