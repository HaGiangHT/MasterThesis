#!/bin/bash

xterm -fg white -bg black -e 'docker run --shm-size="1024m" --gpus all --rm -it \
    -v /home/giang/AL-Yolov8/nuimages-all-samples:/input_mount:ro \
    -v /home/giang/AL-Yolov8/lightly:/lightly_mount \
    -e LIGHTLY_TOKEN="976331148fad69677c163a1d8eb788c4f42141356697e9be" \
    -e LIGHTLY_WORKER_ID="655fc9ec4cf00f266012c741" \
    lightly/worker:latest'

