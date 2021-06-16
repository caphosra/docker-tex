# My TeX environments on Docker

[![Deploy docker images](https://github.com/capra314cabra/docker-tex/actions/workflows/deploy.yml/badge.svg)](https://github.com/capra314cabra/docker-tex/actions/workflows/deploy.yml)

This repository contains docker images which have been installed different packages.

With it, you can start your tex life without thinking too much about what packages you have to install to launch. For professionals, you can select your environments according to your needs, such as writing a chemical paper, creating a booklet and compiling a graph.

If you want to use another environment, please make a PR :)

## Available envs

- latest (For general purposes)
- chem (For chemical purposes)
- chem-jp (For chemical purposes)

## Image infos

|item|information|
|:---|:---|
|OS|ubuntu 20.04|
|Installed tex platform|texlive|
|Package manager|tlmgr|

## Installed packages

|package name|latest|chem|chem-jp|
|:---|:---:|:---:|:---:|
|biber|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
|biblatex|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
|chemfig||:heavy_check_mark:|:heavy_check_mark:|
|collection-langjapanese|||:heavy_check_mark:|
|float|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
|here|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
|jsarticle|||:heavy_check_mark:|
|latexmk|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
|mhchem||:heavy_check_mark:|:heavy_check_mark:|
|pdflscape|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
|pdfpages|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
|platex|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
|ptex2pdf|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
|simplekv||:heavy_check_mark:|:heavy_check_mark:|
|siunitx||:heavy_check_mark:|:heavy_check_mark:|
|xcolor|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|

## How to install

Just executing a following command to get it.

```bash
$ docker pull capra314cabra/tex:latest
```
