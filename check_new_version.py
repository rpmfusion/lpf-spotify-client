#!/usr/bin/python3

""" Warning not complete """

import requests
import re
import os
import subprocess

def runme(cmd, env, cwd='.'):
    """Simple function to run a command and return 0 for success, 1 for
       failure.  cmd is a list of the command and arguments, action is a
       name for the action (for logging), pkg is the name of the package
       being operated on, env is the environment dict, and cwd is where
       the script should be executed from."""
    try:
        subprocess.check_call(cmd, env=env, cwd=cwd, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        sys.stderr.write('%s failed: %s\n' % (cmd, e))
        return 1
    return 0

text = "cat spotify-client.spec.in | grep ^Version"
texts = text.split('|')
text0 = texts[0].strip().split(' ')
#print(text0)
text1 = texts[1].strip().split(' ')
#print(text1)

ps1 = subprocess.run(text0, check=True, capture_output=True)
ps2 = subprocess.run(text1, input=ps1.stdout, capture_output=True)
print("Current %s" % ps2.stdout.decode())

html = requests.get('http://repository.spotify.com/pool/non-free/s/spotify-client/')
#print (html.text)

str_mx = re.compile('href="(spotify-client.*?i386.deb)"')
str_mx2 = re.compile('href="(spotify-client.*?amd64.deb)"')
res = str_mx.findall(html.text)
res2 = str_mx2.findall(html.text)
deb32 = res[-1]
deb64 = res2[-1]
regexp = re.compile('spotify-client_(\d{1,2}[.]\d{1,2}[.]\d{1,3}[.]\d{1,3})([.].*)')
(version64, minor64) = regexp.findall(deb64)[0]
print ("deb64 = %s\nVersions: %s %s" % (deb64, version64, minor64))
print ("Latest Version: %s" % version64)
(version32, minor32) = regexp.findall(deb32)[0]
#print ("deb32 = %s\nVersions: %s %s\n" % (deb32, version32, minor32))
print ("Latest deb32 Version: %s \n" % version32)

spec = open('spotify-client.spec.in').read()
#print (spec)
#str_mx3 = re.compile('(Version:\s*) .*')
#spec2 = re.sub(str_mx3, r'\1 %s' % version64, spec)
str_mx4 = re.compile('(Source1:.*?)[.].*')
spec3 = re.sub(str_mx4, r'\1%s' % minor64, spec)
str_mx5 = re.compile('(Source2:.*?/).*')
spec4 = re.sub(str_mx5, r'\1%s' % deb32, spec3)

if spec != spec3:
    open('spotify-client.spec.in', 'w').write(spec4)
    enviro = os.environ
    pkgcmd = ['rpmdev-bumpspec', '-n', version64, '-c', 'Update to %s%s' % (version64, minor64[:10]),
        'spotify-client.spec.in']
    #pkgcmd = ['rpmdev-bumpspec -n %s -c "Update to %s%s" spotify-client.spec.in' % (version64, version64, minor64[:4])]
    if runme(pkgcmd, enviro):
        print('error running runme')
    pkgcmd = ['rpmdev-bumpspec', '-n', version64, '-c', 'Update to %s%s' % (version64, minor64[:10]),
        'lpf-spotify-client.spec'] # 2>/dev/null
    if runme(pkgcmd, enviro):
        print('error running runme')

    print("New version available!")
    print('rfpkg mockbuild -N --default-mock-resultdir --root fedora-35-x86_64-rpmfusion_nonfree'
        % version64)
else:
    print("Already updated !")

print('rfpkg ci -c && git show && echo Press enter to push and build; read dummy; rfpkg push && rfpkg build --nowait')
print('git checkout f36 && git merge master && git push && rfpkg build --nowait; git checkout master')
print('git checkout f35 && git merge master && git push && rfpkg build --nowait; git checkout master')
print('git checkout f34 && git merge master && git push && rfpkg build --nowait; git checkout master')
print('git checkout el8 && git merge master && git push && rfpkg build --nowait; git checkout master')
