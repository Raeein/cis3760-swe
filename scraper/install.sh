#!/bin/bash

echo "Installing geckodriver"

cp geckodriver-v0.34.0-linux64.tar.gz /usr/bin/
tar -xvzf /usr/bin/geckodriver-v0.34.0-linux64.tar.gz -C /usr/bin/
chmod +x /usr/bin/geckodriver

echo "geckodriver installed"

rm /usr/bin/geckodriver-v0.34.0-linux64.tar.gz