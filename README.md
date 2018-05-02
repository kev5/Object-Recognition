# Object Recognition

The goal of this project is to use artificial intelligence algorithms/models, e.g., neural networks, to recognize and locate objects, here, IKEA products, in images of indoor scenes from "IKEA galleries." We are provided with sample photos of objects that are known to be in the scene as guidance for our recognition system. We should match as many objects as possible among the provided objects with their equivalent objects in the scene.

### Please follow these steps to Run our model:

1. Open the file detection.ipynb with Jupyter Notebook
2. Download the pre-trained model from [here](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md)
3. You may need to rename the frozen_inference_graph.pb to name_of_the_model.pb(e.g. faster_rcnn_inception_resnet_v2_atrous_coco.pb)
4. Add your images into the /testimages file. You may need to rename the image to image{#}.jpg.
5. Run the code in Jupyter Notebook to get the results (Name the output image accordingly -> last line in the detection section)

### Per Image Stats for Different Models

| Stats\Model    | MOBILENET | INCEPTIONNET  | RCNN_INCEPTION_RESNET | FASTER_RCNN  |
|----------------|-----------|---------------|-----------------------|--------------|
| Detection time | ~180ms    | ~250ms        | ~24s                  | ~40s         |
| Model Size     | ~30MB     | ~100MB        | ~250MB                | ~600MB       |

### Conclusions

What are the strengths and weaknesses of our method?

* Strength - Faster, more accurate and simpler method for multiple object detection especially when the dataset provided is sparse
* Weakness - The detection does not perform well when the object is poorly oriented or when many objects are cluttered with one another

Our Faster R-CNN model identifies and locates about 90% of the objects in a given image, without sacrificing the speed of detection.
