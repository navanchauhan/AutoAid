#!/bin/bash
if ! command -v poetry &> /dev/null
then
	curl -sSL https://install.python-poetry.org | python3 -
fi

cd /home/ec2-user
poetry install
