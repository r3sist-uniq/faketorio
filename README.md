
# Faketorio

Want to play co-op with your friends but don't want to rent servers?

Here is a small (dumb) python script which acts like a fake server. All it does it pushes and pulls from a remote git repository. 

Basically, you host, play together with your friend, save your world, your friend will automatically find it on their computer. 

You can use this an .exe , and run it as a background process. Meaning, it will keep running in the background without you knowing. 

## Supported Games

Factorio 


Minecraft

more?

Basically everywhere you need computers to sync a folder automatically. 

## How to make it work?

Create a common github/gitlab repo where you want your fake server to be. One of your friends pushes the already saved game files into it. 

Your second friend will now go to the location where his factorio files are saved. 

Then:
```python
git init
git commit -a -m "your commit message"
git pull --allow-unrelated-histories
```

To build an .exe file , install pyinstaller

Then:
```python
pyinstaller --onefile fake_server.py   
```

Now you can start the python program from both of your computers. Magic. You can even create this as a background process which boots automatically on startup. Magic. 

## NOTE

This is made to sync a folder between different computers. If your friend goes rogue and deletes your main file, it WILL get deleted in your computer too. 

But, since we are using git, JUST go back to a previous commit, and resurrect your world :) 

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)


