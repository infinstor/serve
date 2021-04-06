import os
import sys
import subprocess

model_run_id = None
model_name = None
for x in range(1, len(sys.argv)):
    print('Processing arg=' + str(sys.argv[x]), flush=True)
    if (sys.argv[x].startswith('--model-run-id=')):
        model_run_id = sys.argv[x][len('--model-run-id='):]
        print('model_run_id=' + str(model_run_id), flush=True)
    elif (sys.argv[x].startswith('--model-name=')):
        model_name = sys.argv[x][len('--model-name='):]
        print('model_name=' + str(model_name), flush=True)

if (not model_run_id and not model_name):
    raise Exception('Error model-run-id or model-name must be specified')

if (model_run_id):
    subprocess.run(['/home/ec2-user/anaconda3/bin/mlflow', 'models', 'serve', '-m', 'runs:/' + model_run_id + '/model', '-h', '0.0.0.0'], env=os.environ)
else:
    subprocess.run(['/home/ec2-user/anaconda3/bin/mlflow', 'models', 'serve', '-m', 'models:/' + model_name + '/', '-h', '0.0.0.0'], env=os.environ)
