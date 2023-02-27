# Tflite model trainer

## Features

* Automatic download of open images dataset (+ conversion to voc format)
* Training of `EfficientDet` for object detection
* Save fine-tuned model in tflite model

---

## Getting started

### Requirements
* Python = `3.8`
* Linux OS (or wsl2)

### Environment

> The following pipeline of commands was tested on windows subsystem for linux (wsl) - ubuntu and python 3.8


1) Install python3.8 and virtualenv tool.

2) Create and activate virtual environment:

```
virtualenv --python=python3.8 env
```
Check if activated using `python --version` -> should print python version `3.8.x`

3) Upgrade pip

```
python -m pip install -U pip
```

4) Install requirements:

```
pip install -r requirements.txt
```

5) Install required tools:

```
sudo apt-get install libsndfile1
sudo apt install libportaudio2
```

6) Install python packages in consecutive order:

```
pip install -q --use-deprecated=legacy-resolver tflite-model-maker
pip install -q opencv-python-headless==4.1.2.30
pip uninstall -y tensorflow && pip install -q tensorflow==2.8.0
pip install numpy==1.20.3
pip install oidv6-to-voc
pip install boto3==1.24.91
pip install botocore==1.27.91
```

---

## Use

1) Download images:

```
python open_images_downloader.py --max-images=500 --class-names "Tennis ball" --data=data/dataset
```

2) Convert images:

```
oidv6-to-voc ./data/dataset/sub-train-annotations-bbox.csv -d ./data/dataset/class-descriptions-boxable.csv --imgd ./data/dataset/train --outd ./data/dataset/annotations_train

oidv6-to-voc ./data/dataset/sub-validation-annotations-bbox.csv -d ./data/dataset/class-descriptions-boxable.csv --imgd ./data/dataset/validation --outd ./data/dataset/annotations_validation

oidv6-to-voc ./data/dataset/sub-test-annotations-bbox.csv -d ./data/dataset/class-descriptions-boxable.csv --imgd ./data/dataset/test --outd ./data/dataset/annotations_test

```

3) Run `train.py` script.











