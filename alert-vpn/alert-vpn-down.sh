#!/bin/bash

docker run \
    --rm \
    --net=host \
    -e TELEGRAM_TOKEN="<Token>" \
    -e TELEGRAM_CHAT_ID="<chat_id>" \
    -e IP_CHECK="<ip>" \
    -e PORT_CHECK="<porta>" \
    -e ERROR_MESSAGE="<mensagem>" \
    alert-vpn-down:latest