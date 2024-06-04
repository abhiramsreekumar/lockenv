# lockenv - encrypt and decrypt env files easily

A Helper pip package for encrypting env's to be stored safely in code repositories


#### Assumptions:

+ Assuming python3 is installed on your system.
+ Nano is installed on your system
+ If you have VScode installed, better !


Install `lockenv` on your system using : 

```
pip install lockenv
```

### Encryption Options

```
lockenv
```

+ The command will check for any 'fkey' files in the current path, if found will read the key, if not it will prompt to generate a new key

+ Secondly it will look for an env file in the current path, if found will read env, if nit will prompt to generate a new env

+ It will automatically open the decrypted version of env in Visual Studio Code, if it is not installed, it will open nano editor

+ After editing the env file save it and close the file, it will be encrypted automatically


```
lockenv -e production
```
+ You can specify an environment, and it will open the environment specific key and env file, if not exist will create

```
lockenv -e production -k keyfile or key-string
```

+ You can also specify keys manually
+ the key can be either the keyfile name or the key as a string

```
lockenv -e production -f envfile
```
+ The env file can also be manually specified

#### Examples
```
lockenv -k key-string N_Wctg1YY7uyUmD8Cs4bq3VY6IsOHVbbeElpC-tpvE4= -f test.env
```
+ encrypting specifying key and env file manually


### Decryption Options

```
lockenv -d
```
+ It will decypt the env file, if multiple env or keys are found it will prompt to choose one

```
lockenv -d -e production
```
+ You can specify an environment 
+ Recomended option if using inside pipelines or scripts


#### Examples
```
lockenv -d -k key-string N_Wctg1YY7uyUmD8Cs4bq3VY6IsOHVbbeElpC-tpvE4= -f test.env
```
+ Decrypting specifying key and env file manually
