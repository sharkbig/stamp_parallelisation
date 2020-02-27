# StaMPSv4.0 parallelisation code with python

## Introduction

This reporisation realize the parallelisation in StaMPSv4.0.


## Requirement

1. matlab 2019b
2. StaMPSv4.0
3. Python2.7 and install:
	* matlab API
	* multiprocessing

## Recommendation 

1. CPU: 8 core (or more)
2. RAM: 8G (enough)


## Usage: stamps -j[1] -s[0] -e[8]
Working directory: excute at the parent directory of all PATCH.
<options>
	-j: number of process assign, default 1.
	-s: start step of stamps, default 0. (the latest step)
	-e: end step of stamps, default 8. (the last step)
