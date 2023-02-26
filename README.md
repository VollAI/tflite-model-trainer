# tflite-model-trainer


pip install oidv6-to-voc

https://gpiocc.github.io/learn/ml/raspberrypi/2021/09/07/martin-ku-train-custom-object-detection-model-with-tensorflow-lite-model-maker.html

oidv6-to-voc <annotation-file(s).csv>
             -d <class-names-file.csv> 
             --imgd <directory/to/your/images>
             --outd <your/output/diretory>

oidv6-to-voc ./data/dataset/paddle/train-annotations-bbox.csv -d ./data/dataset/paddle/class-descriptions-boxable.csv --imgd ./data/dataset/paddle/train --outd ./data/dataset_out
		

https://github.com/tensorflow/tensorflow/issues/51031#issuecomment-891139641


---------------------------------------------------------------

Tested on windows wsl (linux distro) with pyhon 3.8

1) Install python3.8 and virtualenv tool.

2) Set virtual environment and activate:

virtualenv --python=python3.8 env

make sure with: python --version

3) Upgrade pip

python -m pip install -U pip

4) install requirements:

pip install -r requirements.txt

5) install required tools:

sudo apt-get install libsndfile1
sudo apt install libportaudio2

6) install python packages in consecutive order:

pip install -q --use-deprecated=legacy-resolver tflite-model-maker
pip install -q opencv-python-headless==4.1.2.30
pip uninstall -y tensorflow && pip install -q tensorflow==2.8.0
pip install numpy==1.20.3
pip install oidv6-to-voc
pip install boto3==1.24.91
pip install botocore==1.27.91


----------------------------------------------------------------------

Download images:

python open_images_downloader.py --max-images=500 --class-names "Tennis ball" --data=data/dataset

Convert images:

oidv6-to-voc ./data/dataset/sub-train-annotations-bbox.csv -d ./data/dataset/class-descriptions-boxable.csv --imgd ./data/dataset/train --outd ./data/dataset/annotations_train

oidv6-to-voc ./data/dataset/sub-validation-annotations-bbox.csv -d ./data/dataset/class-descriptions-boxable.csv --imgd ./data/dataset/validation --outd ./data/dataset/annotations_validation

oidv6-to-voc ./data/dataset/sub-test-annotations-bbox.csv -d ./data/dataset/class-descriptions-boxable.csv --imgd ./data/dataset/test --outd ./data/dataset/annotations_test


-------------------------------------------------------------------------------
3) Download object detection model:

run train.py










