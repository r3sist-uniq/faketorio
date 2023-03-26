import subprocess
import time

save_directory = ".\saves"

while True: 
    pulling = subprocess.run(shell=True, args=['git', 'pull'], capture_output=True, cwd=save_directory)
    print(pulling, 'pulled')
    adding = subprocess.run(shell=True, args=['git', 'add', '.'], capture_output=True,cwd=save_directory)
    print(adding, 'added')
    commits = subprocess.run(shell=True, args=['git', 'commit',  '-m' , f'"the time of this commit is {time.time()}"'], capture_output=True, cwd=save_directory)
    print(commits, 'committed')
    pushing = subprocess.run(shell=True, args=['git', 'push', '-u', 'origin', 'master'], capture_output=True, cwd=save_directory)
    print(pushing, 'pushed') 
    print('goin to sleep now')
    time.sleep(60)
