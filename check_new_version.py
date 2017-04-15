#!/usr/bin/python3

""" Warning not complete """

import requests
import re
import os
import subprocess
requests.get('http://repository.spotify.com/pool/non-free/s/spotify-client/')
a = requests.get('http://repository.spotify.com/pool/non-free/s/spotify-client/')
#print (a.text)

str_mx = re.compile('href="(spotify-client.*?i386.deb)"')
str_mx2 = re.compile('href="(spotify-client.*?amd64.deb)"')
res = str_mx.findall(a.text)
res2 = str_mx2.findall(a.text)
deb32 = res[-1]
deb64 = res2[-1]
print (deb32,deb64)
res2 = str_mx.findall(a.text)

regexp = re.compile('spotify-client_(\d{1,2}[.]\d{1,2}[.]\d{1,3})([.].*)')
(version32, minor32) = regexp.findall(deb32)[0]
(version64, minor64) = regexp.findall(deb64)[0]
print (version32, minor32, version64, minor64)

spec = open('spotify-client.spec.in').read()
#print (spec)
#str_mx3 = re.compile('(Version:\s*) .*')
#spec2 = re.sub(str_mx3, r'\1 %s' % version64, spec)
str_mx4 = re.compile('(Source1:.*?)[.].*')
spec3 = re.sub(str_mx4, r'\1%s' % minor64, spec)
str_mx5 = re.compile('(Source2:.*?)[.].*')
spec4 = re.sub(str_mx5, r'\1%s' % minor32, spec3)

open('spotify-client.spec.in', 'w').write(spec4)

def runme(cmd, env, cwd='.'):
    """Simple function to run a command and return 0 for success, 1 for
       failure.  cmd is a list of the command and arguments, action is a
       name for the action (for logging), pkg is the name of the package
       being operated on, env is the environment dict, and cwd is where
       the script should be executed from."""
    try:
        subprocess.check_call(cmd, env=env, cwd=cwd)
    except subprocess.CalledProcessError as e:
        sys.stderr.write('%s failed: %s\n' % (cmd, e))
        return 1
    return 0

enviro = os.environ
pkgcmd = ['rpmdev-bumpspec', '-n', version64, '-c', 'Update to %s%s' % (version64, minor64[:4]), 'spotify-client.spec.in']
if runme(pkgcmd, enviro):
    print('error running runme')
pkgcmd = ['rpmdev-bumpspec', '-n', version64, '-c', 'Update to %s%s' % (version64, minor64[:4]), 'lpf-spotify-client.spec']
if runme(pkgcmd, enviro):
    print('error running runme')

