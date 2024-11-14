#!/bin/bash


#while true; do
#  {
#
    xterm -fg white -bg black -e 'docker run --shm-size="1024m" --gpus all --rm -it \
        -v /home/giang/ServerClient/Server_Client_NoneF/client0_dataset:/input_mount:ro \
        -v /home/giang/ServerClient/Server_Client_NoneF/lightly:/lightly_mount \
        -e LIGHTLY_TOKEN="976331148fad69677c163a1d8eb788c4f42141356697e9be" \
        -e LIGHTLY_WORKER_ID="65ba3cba5ca670c73d222aa8" \
        lightly/worker:latest'

    xterm -fg white -bg black -e 'docker run --shm-size="1024m" --gpus all --rm -it \
        -v /home/giang/ServerClient/Server_Client_NoneF/client1_dataset:/input_mount:ro \
        -v /home/giang/ServerClient/Server_Client_NoneF/lightly:/lightly_mount \
        -e LIGHTLY_TOKEN="976331148fad69677c163a1d8eb788c4f42141356697e9be" \
        -e LIGHTLY_WORKER_ID="65ba3cfa5ca670c73d226ee5" \
        lightly/worker:latest '

    xterm -fg white -bg black -e 'docker run --shm-size="1024m" --gpus all --rm -it \
        -v /home/giang/ServerClient/Server_Client_NoneF/client2_dataset:/input_mount:ro \
        -v /home/giang/ServerClient/Server_Client_NoneF/lightly:/lightly_mount \
        -e LIGHTLY_TOKEN="976331148fad69677c163a1d8eb788c4f42141356697e9be" \
        -e LIGHTLY_WORKER_ID="65c63b9b5ca670c73dd60625" \
        lightly/worker:latest'

    xterm -fg white -bg black -e 'docker run --shm-size="1024m" --gpus all --rm -it \
        -v /home/giang/ServerClient/Server_Client_NoneF/client3_dataset:/input_mount:ro \
        -v /home/giang/ServerClient/Server_Client_NoneF/lightly:/lightly_mount \
        -e LIGHTLY_TOKEN="976331148fad69677c163a1d8eb788c4f42141356697e9be" \
        -e LIGHTLY_WORKER_ID="65c63ba55ca670c73dd606e3" \
        lightly/worker:latest'

    xterm -fg white -bg black -e 'docker run --shm-size="1024m" --gpus all --rm -it \
      -v /home/giang/ServerClient/Server_Client_NoneF/client4_dataset:/input_mount:ro \
      -v /home/giang/ServerClient/Server_Client_NoneF/lightly:/lightly_mount \
      -e LIGHTLY_TOKEN="976331148fad69677c163a1d8eb788c4f42141356697e9be" \
      -e LIGHTLY_WORKER_ID="65c63bae5ca670c73dd60773" \
      lightly/worker:latest'

    xterm -fg white -bg black -e 'docker run --shm-size="1024m" --gpus all --rm -it \
      -v /home/giang/ServerClient/Server_Client_NoneF/client5_dataset:/input_mount:ro \
      -v /home/giang/ServerClient/Server_Client_NoneF/lightly:/lightly_mount \
      -e LIGHTLY_TOKEN="976331148fad69677c163a1d8eb788c4f42141356697e9be" \
      -e LIGHTLY_WORKER_ID="65c63bb75ca670c73dd60824" \
      lightly/worker:latest'

    xterm -fg white -bg black -e 'docker run --shm-size="1024m" --gpus all --rm -it \
      -v /home/giang/ServerClient/Server_Client_NoneF/client6_dataset:/input_mount:ro \
      -v /home/giang/ServerClient/Server_Client_NoneF/lightly:/lightly_mount \
      -e LIGHTLY_TOKEN="976331148fad69677c163a1d8eb788c4f42141356697e9be" \
      -e LIGHTLY_WORKER_ID="65c63bc35ca670c73dd60905" \
      lightly/worker:latest'

    xterm -fg white -bg black -e 'docker run --shm-size="1024m" --gpus all --rm -it \
      -v /home/giang/ServerClient/Server_Client_NoneF/client7_dataset:/input_mount:ro \
      -v /home/giang/ServerClient/Server_Client_NoneF/lightly:/lightly_mount \
      -e LIGHTLY_TOKEN="976331148fad69677c163a1d8eb788c4f42141356697e9be" \
      -e LIGHTLY_WORKER_ID="65c63bcb5ca670c73dd60a0f" \
      lightly/worker:latest'

    xterm -fg white -bg black -e 'docker run --shm-size="1024m" --gpus all --rm -it \
        -v /home/giang/ServerClient/Server_Client_NoneF/client8_dataset:/input_mount:ro \
        -v /home/giang/ServerClient/Server_Client_NoneF/lightly:/lightly_mount \
        -e LIGHTLY_TOKEN="976331148fad69677c163a1d8eb788c4f42141356697e9be" \
        -e LIGHTLY_WORKER_ID="65c63bd55ca670c73dd60aca" \
        lightly/worker:latest'

    xterm -fg white -bg black -e 'docker run --shm-size="1024m" --gpus all --rm -it \
      -v /home/giang/ServerClient/Server_Client_NoneF/client9_dataset:/input_mount:ro \
      -v /home/giang/ServerClient/Server_Client_NoneF/lightly:/lightly_mount \
      -e LIGHTLY_TOKEN="976331148fad69677c163a1d8eb788c4f42141356697e9be" \
      -e LIGHTLY_WORKER_ID="65c7af2f5ca670c73d0baadc" \
      lightly/worker:latest'

#    sleep 300
#  } 2>&1 | tee >(grep -q "Killed" && echo "Restarting workers...")
#done
#sleep 300


#lightly-serve \
#  input_mount=/home/giang/ServerClient/client1_dataset \
#  lightly_mount=/home/giang/ServerClient/lightly \
#  host=localhost \
#  port=3456
