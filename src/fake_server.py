import subprocess
import time

adding = subprocess.run(shell=True, args=['git', 'add', '.'], capture_output=True,cwd='..\saves')
commits = subprocess.run(shell=True, args=['git', 'commit',  '-m' , f'"the time of this commit is {time.time()} (this is the initial commit before starting)"'], capture_output=True, cwd='..\saves')
pushing = subprocess.run(shell=True, args=['git', 'push', '-u', 'origin', 'main'], capture_output=True, cwd='..\saves')


while True: 
    pulling = subprocess.run(shell=True, args=['git', 'pull'], capture_output=True, cwd='..\saves')
    adding = subprocess.run(shell=True, args=['git', 'add', '.'], capture_output=True,cwd='..\saves')
    commits = subprocess.run(shell=True, args=['git', 'commit',  '-m' , f'"the time of this commit is {time.time()}"'], capture_output=True, cwd='..\saves')
    pushing = subprocess.run(shell=True, args=['git', 'push', '-u', 'origin', 'main'], capture_output=True, cwd='..\saves')
    time.sleep(60)
