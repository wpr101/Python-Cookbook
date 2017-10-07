#!/bin/bash
# versioning script
clear

echo "Make a selection"
echo "1 Create a branch"
echo "2 Checkout a branch"
echo "3 Save and push to your branch"

read choice

if (("$choice" == "1")); then
  echo "Create."
  echo "What do you want to name your branch?"
  read name

  git checkout -b "$name"
  git push -u origin new-feature

elif (("$choice" == "2")); then
  echo "checkout"

elif (("$choice" == "3")); then
  echo "save and push"
  echo "what did you change?"
  read message
  git add *
  git commit -m "$message"
  git push -u origin new-feature

fi
