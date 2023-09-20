#!/bin/bash

docker run --rm --net=host -e DISCORD_URL="<discord_url>" -e IP_CHECK="<IP to check>" -e PORT_CHECK="<port to check>" alert-vpn-down:latest