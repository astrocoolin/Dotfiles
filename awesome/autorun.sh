#!/usr/bin/env bash

function run {
  if ! pgrep -f $1 ;
  then
    $@&
  fi
}

run thunderbird
run light-locker
run blueman_applet
run redshift -l 43.6532:-79.3832
run compton
run tint2
