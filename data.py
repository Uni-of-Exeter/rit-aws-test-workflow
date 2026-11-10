import argparse
import torch
from torchvision import datasets, transforms


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("data_path")
    args = ap.parse_args()

    dataset1 = datasets.MNIST(args.data_path, train=True, download=True)
    train_loader = torch.utils.data.DataLoader(dataset1)
    print(train_loader)

if __name__ == '__main__':
    main()
