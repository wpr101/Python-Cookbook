import subprocess
out_bytes = subprocess.check_output(['netstat', '-a'])

print(out_bytes)
