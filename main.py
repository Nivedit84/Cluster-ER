from checks.pods import check_pods
from checks.incidents import capture_incident

def main():
    print ("Running kubectl commands...\n")
    failed_pods, crashloop_pods, image_pull_error_pods, pending_pods = check_pods()  #Check the status of pods in the cluster
    if failed_pods or crashloop_pods or image_pull_error_pods or pending_pods:
        print("Found pods with issues:")
        if failed_pods:
            print(f" - Failed pods: {len(failed_pods)}")
        if crashloop_pods:
            print(f" - CrashLoopBackOff pods: {len(crashloop_pods)}")
        if image_pull_error_pods:
            print(f" - ImagePullBackOff pods: {len(image_pull_error_pods)}")
        if pending_pods:
            print(f" - Pending pods: {len(pending_pods)}")
    else:
        print("All pods are functioning correctly.")
    
    capture_incident()  #Capture the current state of the cluster for incident analysis

if __name__ == "__main__":
    main()