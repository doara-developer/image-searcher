#!/bin/bash

readonly TARGET=./app
readonly TEST_FOLDER=./__test__

if [ $# -ne 1 ]; then
    echo "argument is not enough or too many."
elif [ $1 = test ]; then
    poetry run pytest -v $TEST_FOLDER
elif [ $1 = coverage ]; then
    poetry run pytest -v --cov=$TARGET --cov-report=html $TEST_FOLDER
elif [ $1 = bandit ]; then
    poetry run bandit -r $TARGET
elif [ $1 = flake8 ]; then
    poetry run flake8 $TARGET
fi
