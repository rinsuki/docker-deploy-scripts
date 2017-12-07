#!/usr/bin/env python3
import os
import sys
import subprocess

if os.environ.get("CONTAINER_NAME") is None:
    print("please set CONTAINER_NAME env")
    exit(-1)

if os.environ.get("APP_DIR") is not None: # build and deploy
    subprocess.run([
        "git", "pull"
    ],cwd=os.environ.get("APP_DIR"))
	subprocess.run([
        "docker",
        "build",
        "-t",
        os.environ.get("APP_NAME", os.environ.get("CONTAINER_NAME"))
    ],cwd=os.environ.get("APP_DIR"))
subprocess.run([
    "docker",
    "stop",
    os.environ.get("CONTAINER_NAME")
])
subprocess.run([
    "docker",
    "rm",
    os.environ.get("CONTAINER_NAME")
])
r = subprocess.run([
    "docker",
    "run",
    "--name",
    os.environ.get("CONTAINER_NAME"),
    sys.argv[1:],
    "-d",
    os.environ.get("APP_NAME", os.environ.get("CONTAINER_NAME"))
])
exit(r.returncode())