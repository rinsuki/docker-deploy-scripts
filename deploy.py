#!/usr/bin/env python3
import os
import sys
import subprocess

if os.environ.get("CONTAINER_NAME") is None:
    print("please set CONTAINER_NAME env")
    exit(-1)

if os.environ.get("APP_GIT") is not None:
    subprocess.run([
        "ghq", "get", 
        os.environ["APP_GIT"]
    ])
    myenv = os.environ.copy()
    myenv["SHELL"]="/bin/pwd"
    r = subprocess.Popen([
        "ghq", "look", 
        os.environ["APP_GIT"]
    ], stdout=subprocess.PIPE, env=myenv)
    out, _ = r.communicate()
    os.environ["APP_DIR"] = out.decode("utf-8").split("\n")[-2]
    if os.environ.get("APP_GIT_SUBDIR") is not None:
        os.environ["APP_DIR"] += "/" + os.environ["APP_GIT_SUBDIR"]

if os.environ.get("APP_DIR") is not None: # build and deploy
    subprocess.run([
        "git", "pull"
    ],cwd=os.environ.get("APP_DIR"))
    subprocess.run([
        "docker",
        "build",
        "-t",
        os.environ.get("APP_NAME", os.environ.get("CONTAINER_NAME")),
        os.environ.get("APP_DIR")
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
a = [
    "docker",
    "run",
    "--name",
    os.environ.get("CONTAINER_NAME")
]
a += sys.argv[1:]
a += [
    "-d",
    os.environ.get("APP_NAME", os.environ.get("CONTAINER_NAME"))
]
r = subprocess.run(a)
exit(r.returncode)