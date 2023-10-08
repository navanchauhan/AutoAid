#!/bin/bash
if ! command -v poetry &> /dev/null
then
	curl -sSL https://install.python-poetry.org | python3 -
fi
export PATH="/root/.local/bin:$PATH"
cd /home/ec2-user/dep-dir
/root/.local/bin/poetry install
