# Touchless UI
Touchless UI is a hand gesture-based user interaction program. It allows the user to interact with youtube videos by using intuitive hand gestures. At the proof of concept stage, this program currently supports interactions to play and stop a video. I will extend it to other gestures and applications in the future.

Touchless UI is built on a customized version of [mediapipe](https://github.com/yujie-tao/mediapipe/), and the interaction is running on a headless browser. Mediapipe is a multimodal applied ML pipeline that supports us with hand landmarks. I classify different gestures by using a SVM model and then connect it to specific experience within the browser. The headless browser allows me to make use of existing user experience on webspace and add a new layer of interaction on it.


![touchless-ui](https://user-images.githubusercontent.com/32469005/67163794-3179cb00-f341-11e9-99f2-5f6c99c20437.gif)


## Installation
### Clone repository
```
git clone --recursive https://github.com/yujie-tao/touchless-ui.git
```

### Setup environment

1. Mediapipe

Follow the instruction of [mediapipe](https://github.com/yujie-tao/mediapipe/blob/master/mediapipe/docs/install.md#installing-on-macos) to install environment for your system. Currently only supports CPU. 

Key components are:
* Bazel
* OpenCV

2. Headless browser

```python
python -m pip install -U git+https://github.com/yujie-tao/pyppeteer.git

```

## Initialization
1. Gesture tracking

```
# Video from webcam running on desktop CPU
$ bazel build -c opt --define MEDIAPIPE_DISABLE_GPU=1 \
    mediapipe/examples/desktop/hand_tracking:hand_tracking_cpu

# It should print:
#Target //mediapipe/examples/desktop/hand_tracking:hand_tracking_cpu up-to-date:
#  bazel-bin/mediapipe/examples/desktop/hand_tracking/hand_tracking_cpu
#INFO: Elapsed time: 22.645s, Forge stats: 13356/13463 actions cached, 1.5m CPU used, 0.0s queue time, 819.8 MB ObjFS output (novel bytes: 85.6 MB), 0.0 MB local output, Critical Path: 14.43s, Remote (87.25% of the time): [queue: 0.00%, network: 14.88%, setup: 4.80%, process: 39.80%, fetch: 18.15%]
#INFO: Streaming build results to: http://sponge2/360196b9-33ab-44b1-84a7-1022b5043307
#INFO: Build completed successfully, 12517 total actions

$ export GLOG_logtostderr=1
# This will open up your webcam as long as it is connected and on
# Any errors is likely due to your webcam being not accessible

$ bazel-bin/mediapipe/examples/desktop/hand_tracking/hand_tracking_cpu \
    --calculator_graph_config_file=mediapipe/graphs/hand_tracking/hand_tracking_desktop_live.pbtxt
```


2. Gesture detection


```python
python detection.py

```
