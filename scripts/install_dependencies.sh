#!/bin/bash
if ! command -v poetry &> /dev/null
then
	curl -sSL https://install.python-poetry.org | python3 -
fi
export PATH="/root/.local/bin:$PATH"
cd /home/ec2-user
sudo chown -R ec2-user:ec2-user /home/ec2-user/deps-dir
cd /home/ec2-user/deps-dir
sudo -u ec2-user bash -c 'cd /home/ec2-user/deps-dir && /home/ec2-user/.local/bin/poetry install'

systemctl daemon-reload

