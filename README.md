# rit-aws-test-workflow

Demonstration workflow for batch testing in AWS

At the moment, just adapted from github.com/pytorch/examples for the sake of demonstrating a workflow in AWS. It can also be used elsewhere for a consistent experience (e.g. HPC)

The installation and usage goes something like this:

```
# Activate your conda if needed, and install
# This is split between conda and pip for convenience in different environments
source ~/miniforge3/bin/activate
conda env create -n test-workflow -f environment.yml
conda activate test-workflow
pip install -r requirements.yml

# Run the workflow (use conda activate again between sessions)
python data.py ./data
python train.py --epochs 4 ./data
```

You should end up with some logging, fairly quickly: 

```
Train Epoch: 1 [0/60000 (0%)]	Loss: 2.299823
Train Epoch: 1 [640/60000 (1%)]	Loss: 1.734947
Train Epoch: 1 [1280/60000 (2%)]	Loss: 0.916945
Train Epoch: 1 [1920/60000 (3%)]	Loss: 0.661129
...
Train Epoch: 4 [59520/60000 (99%)]	Loss: 0.005004

Test set: Average loss: 0.0341, Accuracy: 9882/10000 (99%)
```
