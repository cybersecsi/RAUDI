# VIM

## Official Documentation
Reference: https://github.com/vim/vim
## Description

**Vim** is a greatly improved version of the good old UNIX editor
[Vi](https://en.wikipedia.org/wiki/Vi).  Many new
features have been added: multi-level undo, syntax highlighting, command line
history, on-line help, spell checking, filename completion, block operations,
script language, etc.  There is also a Graphical User Interface (GUI)
available.  Still, Vi compatibility is maintained, those who have Vi "in the
fingers" will feel at home.
See [`runtime/doc/vi_diff.txt`](runtime/doc/vi_diff.txt) for differences with
Vi.

This editor is very useful for editing programs and other plain text files.
All commands are given with normal keyboard characters, so those who can type
with ten fingers can work very fast.  Additionally, function keys can be
mapped to commands by the user, and the mouse can be used.

Vim runs under MS-Windows (XP, Vista, 7, 8, 10), macOS, Haiku, VMS and almost
all flavours of UNIX.  Porting to other systems should not be very difficult.
Older versions of Vim run on MS-DOS, MS-Windows 95/98/Me/NT/2000, Amiga DOS,
Atari MiNT, BeOS, RISC OS and OS/2.  These are no longer maintained.

For Vim9 script see [README_VIM9](README_VIM9.md).


## Usage

```
docker run -it --rm -v <host_folder>:/data secsi/vim 
```


## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).
