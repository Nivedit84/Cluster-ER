from utils.kubectl import run_kubectl
output = run_kubectl("get pods --all-namespaces")

failed_pods = []  #List to store names of failed pods
crashloop_pods = []  #List to store names of pods in CrashLoopBackOff
image_pull_error_pods = []  #List to store names of pods with ImagePullBackOff
pending_pods = []  #List to store names of pending pods

def check_pods():

    lines = output.splitlines()  #Split the output into lines
    for line in lines[1:]:
        parts = line.split()  #Split the line into parts (columns) like ["namespace", "pod_name", "status", "other", "columns"]
        namespace = parts[0]
        pod_name = parts[1]
        status = parts[3]

        if status in ["Error", "Failed"]:
            failed_pods.append(f"{namespace},{pod_name}")
        elif status == "CrashLoopBackOff":
            crashloop_pods.append(f"{namespace},{pod_name}")
        elif status in ["ImagePullBackOff", "ErrImagePull"]:
            image_pull_error_pods.append(f"{namespace},{pod_name}")
        elif status == "Pending":
            pending_pods.append(f"{namespace},{pod_name}")
    
    return failed_pods, crashloop_pods, image_pull_error_pods, pending_pods