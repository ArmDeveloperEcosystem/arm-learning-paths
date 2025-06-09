"""
Utilities for interacting with Google Cloud Platform.
"""
import subprocess
import sys
from typing import List, Optional

def get_running_instances() -> List[str]:
    """
    Return a list of names of GCP VMs that are currently RUNNING.
    
    Returns:
        List of instance names
    """
    try:
        output = subprocess.check_output(
            ["gcloud", "compute", "instances", "list",
             "--filter=status=RUNNING",
             "--format=value(name)"],
            universal_newlines=True
        )
        instances = [line.strip() for line in output.splitlines() if line.strip()]
        return instances
    except subprocess.CalledProcessError as e:
        print(f"Error fetching running instances: {e}", file=sys.stderr)
        return []

def choose_instance(instances: List[str]) -> str:
    """
    Prompt user to choose an instance from the list.
    
    Args:
        instances: List of instance names
        
    Returns:
        Selected instance name
    """
    if not instances:
        print("No running instances found.", file=sys.stderr)
        sys.exit(1)
        
    print("Select an instance:")
    for idx, name in enumerate(instances, 1):
        print(f"{idx}. {name}")
        
    while True:
        choice = input(f"Enter number (1-{len(instances)}): ").strip()
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(instances):
                return instances[idx - 1]
        print("Invalid selection, try again.")

def get_instance_zone(name: str) -> str:
    """
    Return the zone of the given GCP VM instance.
    
    Args:
        name: Instance name
        
    Returns:
        Zone name
    """
    try:
        output = subprocess.check_output(
            ["gcloud", "compute", "instances", "list",
             "--filter", f"name={name}",
             "--format=value(zone)"],
            universal_newlines=True
        )
        zone = output.strip()
        if not zone:
            raise ValueError(f"No zone found for instance {name}")
        return zone
    except (subprocess.CalledProcessError, ValueError) as e:
        print(f"Error fetching zone for instance {name}: {e}", file=sys.stderr)
        sys.exit(1)

def scp_results(name: str, zone: str, remote_pattern: str, local_out: str) -> bool:
    """
    Copy back all files in remote_dir that match the pattern.
    
    Args:
        name: Instance name
        zone: GCP zone
        remote_pattern: Remote file pattern
        local_out: Local output directory
        
    Returns:
        True if successful, False otherwise
    """
    print(f"Copying {remote_pattern} from {name} to {local_out}")
    scp_cmd = [
        "gcloud", "compute", "scp",
        f"{name}:{remote_pattern}",
        local_out,
        "--zone", zone
    ]
    try:
        subprocess.check_call(scp_cmd)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error copying files: {e}", file=sys.stderr)
        return False