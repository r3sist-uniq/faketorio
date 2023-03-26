
# Faketorio

Want to play co-op with your friends but don't want to rent servers?

Here is a small (dumb) python script which acts like a fake server. All it does it pushes and pulls from a remote git repository. 

Basically, you host, play together with your friend, save your world, and your friend will automatically find the newly saved world on their computer. How? See below

You can run it through the python script OR even build this as an .exe (through pyinstaller) , and run it as a background process. Meaning, it will keep running in the background without you knowing. 

## Supported Games

Basically everywhere you need computers to sync a folder automatically (not just games, ofcourse). 

Factorio 

Minecraft

more?

## How to make it work?

* One of your friend creates a common github/gitlab repo where you guys want your files to be saved (you guys can do it come on) and pushes his saved files if he wants to.  
* All of you initialize a git repo where your game (example: Factorio) saves are saved. Add the common github remote. 

Then:
```python
git init
git commit -a -m "your commit message"
git pull --allow-unrelated-histories
```
* Change the save_directory variable in the python script, to where your files are saved. (note: this is the relative location of your file from where you are executing the script or the .exe)
* Make all your friends run this script (or .exe). And you guys are good to go :)
(optional but good) Build a .exe and run it :) 
* To build an .exe file , install pyinstaller, And:
```python
pyinstaller --onefile fake_server.py   
```

You can even create this as a background process which boots automatically on startup. Magic. 

## NOTE

This is made to sync a folder between different computers. If your friend goes rogue and deletes your main file, it WILL get deleted in your computer too. 

But, since we are using git, JUST go back to a previous commit, and resurrect your world :) 

## Contributing

sure man

## License

[MIT](https://choosealicense.com/licenses/mit/)


