# myConfig

This repository contains my configuration files.

## Getting started

Clone this repository by:
```
$ git clone git@github.com:ayalash/myConfig.git
```
Handle this repository's submodules:
```
$ git submodule update --init --recursive
$ cd vim/vim/bundle/command-t
$ rake make
```
Create needed symlinks so the expected configuration files will point to this repo's files:
```
$ myConfig/set_configuration.py
```
