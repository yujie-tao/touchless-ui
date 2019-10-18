# Touchless UI
Touchless UI is a hand gesture based user interaction program. It currently supports two hand gestures to control a youtube video's play and stop.

This program is built on a customized version of mediapipe and the interaction is running on the headless browser Pyppeteer.

## Installation
1. Clone repository
``
$ git clone --recursive https://github.com/yujie-tao/touchless-ui.git

``

2. Setup environment

### Mediapipe
Follow the instruction of [mediapipe](https://github.com/yujie-tao/mediapipe/blob/master/mediapipe/docs/install.md#installing-on-macos) to install environment for your system.

Only CPU version is now needed.

Key components are:
* bazel
* OpenCV

### Pyppeteer

``
$ python -m pip install -U git+https://github.com/yujie-tao/pyppeteer.git

``

## Initialization
1. Gesture tracking

``
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

``


2. Gesture detection


``
$ python detection.py

``


## Architecture