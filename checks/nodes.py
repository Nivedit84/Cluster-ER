from utils.kubectl import run_kubectl

def check_nodes():
    output = run_kubectl("get nodes")
    
    not_ready_nodes = []
    lines = output.splitlines()
    for line in lines[1:]:  # Skip the header line
        parts = line.split()
        name = parts[0]
        status = parts[1]

        if status != "Ready":
            not_ready_nodes.append(name)
    return not_ready_nodes