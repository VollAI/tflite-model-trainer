import os

import numpy as np
from tflite_model_maker import model_spec, object_detector
from tflite_model_maker.config import ExportFormat, QuantizationConfig

EPOCHS = 2
BATCH_SIZE = 5

if __name__ == "__main__": 
    train_ds = object_detector.DataLoader.from_pascal_voc(
        images_dir="./data/dataset/train",
        annotations_dir="./data/dataset/annotations_train",
        label_map=["Tennis ball"],
    )

    validation_ds = object_detector.DataLoader.from_pascal_voc(
        images_dir="./data/dataset/validation",
        # annotations_dir="./data/dataset/annotations_validation",
        annotations_dir="./data/dataset/annotations_test",
        label_map=["Tennis ball"],
    )

    test_ds = object_detector.DataLoader.from_pascal_voc(
        images_dir="./data/dataset/test",
        annotations_dir="./data/dataset/annotations_test",
        label_map=["Tennis ball"],
    )

	# options: "efficientdet_liteX", where X ele [0, 1, 2, 3, 4]
    spec = model_spec.get('efficientdet_lite1')


    model = object_detector.create(
        train_data=train_ds, 
        model_spec=spec, 
        # epochs=EPOCHS, 
        # batch_size=BATCH_SIZE, 
        train_whole_model=False, 
        validation_data=validation_ds)

    # model.evaluate(test_ds)

    model.export(export_dir='./data/models')

    # TODO: check for quantization
    # https://pub.towardsai.net/object-detection-at-the-edge-with-tf-lite-model-maker-e635a17b0854
