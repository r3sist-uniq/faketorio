import subprocess
import time


save_directory = "..\saves"

adding = subprocess.run(shell=True, args=['git', 'add', '.'], capture_output=True,cwd=save_directory)
commits = subprocess.run(shell=True, args=['git', 'commit',  '-m' , f'"the time of this commit is {time.time()} (this is the initial commit before starting)"'], capture_output=True, cwd=save_directory)
pushing = subprocess.run(shell=True, args=['git', 'push', '-u', 'origin', 'main'], capture_output=True, cwd=save_directory)


while True: 
    pulling = subprocess.run(shell=True, args=['git', 'pull'], capture_output=True, cwd=save_directory)
    adding = subprocess.run(shell=True, args=['git', 'add', '.'], capture_output=True,cwd=save_directory)
    commits = subprocess.run(shell=True, args=['git', 'commit',  '-m' , f'"the time of this commit is {time.time()}"'], capture_output=True, cwd=save_directory)
    pushing = subprocess.run(shell=True, args=['git', 'push', '-u', 'origin', 'main'], capture_output=True, cwd=save_directory)
    time.sleep(60)
