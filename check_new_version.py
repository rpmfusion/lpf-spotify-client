#!/usr/bin/python3

""" Warning not complete """

import requests
import re
import os
import sys
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

# do not forget do git pull before start
result = subprocess.run("git checkout master; git pull", shell=True, capture_output=True, text=True)
print(result.stdout)

spec = open('spotify-client.spec.in').read()
#print (spec)
match = re.search(r'^Version:\s*(\S+)', spec, re.MULTILINE)
current_version = match.group(1)
match = re.search(r'^Source2:.*spotify-client_(\S+)[.]g', spec, re.MULTILINE)
current_version2 = match.group(1)
print("Current Version: %s and i686 version %s " % (current_version, current_version2))

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
}
url = "https://repository.spotify.com/pool/non-free/s/spotify-client/"
html = requests.get(url , headers=headers)
print(html.headers)
regexp = re.compile(r'spotify-client_(\d{1,2}[.]\d{1,2}[.]\d{1,3}[.]\d{1,4})([.].*)')

str_mx = re.compile('href="(spotify-client.*?i386.deb)"')
res = str_mx.findall(html.text)
deb32 = res[-1]
(version32, minor32) = regexp.findall(deb32)[0]
#print ("Version i386: %s %s %s\n" % (deb32, version32, minor32))

str_mx2 = re.compile('href="(spotify-client.*?amd64.deb)"')
res2 = str_mx2.findall(html.text)
print (res2)
#print (res2[-1])
deb64 = res2[-1]
(version64, minor64) = regexp.findall(deb64)[0]
#print ("Version amd64: %s %s %s" % (deb64, version64, minor64))
print ("Latest Versions: %s and i686 version %s \n" % (version64, version32))

if current_version != version64 or current_version2 != version32:
    str_mx4 = re.compile('(Source1:.*?)[.].*')
    spec3 = re.sub(str_mx4, r'\1%s' % minor64, spec)
    str_mx5 = re.compile('(Source2:.*?/).*')
    spec4 = re.sub(str_mx5, r'\1%s' % deb32, spec3)
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

    print("New version available! ACTION REQUIRED !!!\n\n")
    #print('rfpkg mockbuild -N --default-mock-resultdir --root fedora+rpmfusion_nonfree-41-x86_64')
    print('rfpkg --release f41 mockbuild --default-mock-resultdir -N')
else:
    print("Already updated ! no Action required\n\n")

print('rfpkg ci -c && git show && echo Press enter to push and build; read dummy; rfpkg push && rfpkg build --nowait')
print('git checkout f42 && git merge master && git push && rfpkg build --nowait; git checkout master')
print('git checkout f41 && git merge master && git push && rfpkg build --nowait; git checkout master')
print('git checkout f40 && git merge master && git push && rfpkg build --nowait; git checkout master')
print('git checkout el9 && git merge master && git push && rfpkg build --nowait; git checkout master')
