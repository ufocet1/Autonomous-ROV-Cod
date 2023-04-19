import subprocess

weights_path = "runs/train/exp14/weights/best.pt"
source = "0"
view_img = True
max_det = 1
conf_thres = 0.6

command = ["python", "detect.py", "--weights", weights_path, "--source", source, "--max-det", str(max_det), "--conf-thres", str(conf_thres)]

if view_img:
    command.append("--view-img")

result = subprocess.run(command, capture_output=True, text=True)

print(result.stdout)
