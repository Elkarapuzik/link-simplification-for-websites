# Link Shortener
- This is a program that shortens links and finds out how many people clicked on your shortened link.

## How to install
- Download the repository from the git hub:

```
https://github.com/Elkarapuzik/link-simplification-for-websites
```

- Python3 should already be installed. Then use pip(or pip3 if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
``` 
## Preparing to run
- Go to bitly website, register, open settings -> API -> generate token
- Create `.env` file in the program folder.
- The `.env` file should have the following form:
```
TOKEN=token from bitly site
```

## How to run the program
- To run the program you need to type in the command line:
```
python3 main.py
```