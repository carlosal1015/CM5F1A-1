#!/usr/bin/env bash

FILE=CM5F1A_grupo_2

arara -s $FILE
zathura --mode fullscreen $FILE.pdf &
