#!/bin/bash

USER_NAME=$(git config --global user.name)
git config --local user.name ${USER_NAME}

EMAIL=$(git config --global user.email)
git config --local user.email ${EMAIL}