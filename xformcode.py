import os
import sys
import subprocess

for x in range(1, len(sys.argv)):
    print('Processing arg=' + str(sys.argv[x]), flush=True)
    if (sys.argv[x].startswith('--model-run-id=')):
        model_run_id = sys.argv[x][len('--model-run-id='):]
        print('model_run_id=' + str(model_run_id), flush=True)

if (not model_run_id):
    raise Exception('need model_run_id')

subprocess.run(['/opt/conda/bin/mlflow', 'models', 'serve', '-m', 'runs:/' + model_run_id + '/model', '-h', '0.0.0.0'], env=os.environ)
