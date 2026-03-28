import subprocess  #Run terminal commands from Python

def run_kubectl(command):

    """command.split - splits the command so it becomes kubectl get pods -> ["kubectl", "get", "pods"]
       capture_output=True - captures the output of the command, doesn't print it to the terminal
        text=True - returns the output as a string instead of bytes"""
    result = subprocess.run(["kubectl"] + command.split(), capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Error running kubectl command: {result.stderr}")
        return result.stderr or ""
    
    return result.stdout or ""