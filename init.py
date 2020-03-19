#!/usr/bin/python
import os
from github import Github
from sh import git, pushd

mirror_base_url = open("mirror_url", "r").read()[:-1]
origin_token = open("origin_token", "r").read()[:-1]
origin_ssh_key = os.path.dirname(os.path.realpath(__file__)) + "/origin_key"

try:
  os.mkdir("./repos", mode=0o700)
except FileExistsError:
  pass

# origin should be a GitHub repository
for repo in Github(origin_token).get_user().get_repos():
    d = f"./repos/{repo.name}"
    try:
      os.mkdir(d, mode=0o700)
    except FileExistsError:
      continue
    with pushd(d):
      git.init("--bare")
      # add origin remote
      git.remote.add("origin", repo.ssh_url)
      # set ref
      git.config("remote.origin.fetch", "+refs/heads/*:refs/heads/*")
      git.config("remote.origin.fetch", "+refs/tags/*:refs/tags/*", "--add")
      git.config("remote.origin.mirror", "true")
      git.fetch("origin", _env={"GIT_SSH_COMMAND": f"ssh -i {origin_ssh_key}"})
      # add remote url
      git.remote.add("mirror", mirror_base_url+repo.name+".git", "--mirror")
      print(f"repo added {repo.name}")
