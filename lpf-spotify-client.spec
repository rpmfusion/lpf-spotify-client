# %%bal will not work here, lazy evaluation needed.

#devel branch
%global github_repo https://github.com/leamas/spotify-make/archive/%{commit}
%global github_repo https://github.com/robxu9/spotify-make/archive/%{commit}
%global commit      8597389ba7bf755418e8746b9c20af51e4be2bc0
%global commit      a0048ec7c5c6acf4ca584348684150b91328227d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%define         target_pkg %(t=%{name}; echo ${t#lpf-})

Name:           lpf-spotify-client
                # Upstream spotify version, verbatim.
Version:        1.0.47
Release:        1%{?dist}
Summary:        Spotify music player native client package bootstrap

License:        MIT
URL:            https://github.com/leamas/spotify-make
Group:          Development/Tools
BuildArch:      noarch
                # There's no source, only a spec building the target package.
Source0:        spotify-client.spec.in
# http://community.spotify.com/t5/Help-Desktop-Linux-Mac-and/What-license-does-the-linux-spotify-client-use/td-p/173356/highlight/true/page/2
Source1:        eula.txt
Source2:        LICENSE
Source3:        README
Source4:        %{github_repo}/spotify-make-%{shortcommit}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  lpf >= 0.1
Requires:       lpf >= 0.1

%description
Bootstrap package allowing the lpf system to build the non-redistributable
spotify-client package.

The package is only available on ix86 and x86_64 hosts.

See:  http://www.spotify.com/se/blog/archives/2010/07/12/linux/


%prep
%setup -cT
cp %{SOURCE2} LICENSE
cp %{SOURCE3} README


%build


%install
# lpf-setup-pkg [eula] <topdir> <specfile> [sources...]
/usr/share/lpf/scripts/lpf-setup-pkg %{SOURCE1} %{buildroot} %{SOURCE0} %{SOURCE4}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%check
%lpf_check %{SOURCE0}


%post
%lpf_post

%postun
%lpf_postun

%lpf_triggerpostun

%files
%doc README
%license LICENSE
%{_datadir}/applications/%{name}.desktop
%{_datadir}/lpf/packages/%{target_pkg}
%attr(775,pkg-build,pkg-build) /var/lib/lpf/packages/%{target_pkg}


%changelog
* Tue Jan 17 2017 Pedro Albuquerque Santos <petersaints@gmail.com> - 1.0.47-1
- Update to 1.0.47

* Tue Dec 20 2016 Sérgio Basto <sergio@serjux.com> - 1.0.45-1
- Update to 1.0.45

* Wed Dec 14 2016 Sérgio Basto <sergio@serjux.com> - 1.0.44-1
- Update to 1.0.44

* Tue Dec 06 2016 Sérgio Basto <sergio@serjux.com> - 1.0.43-1
- Update to 1.0.43

* Thu Nov 10 2016 Sérgio Basto <sergio@serjux.com> - 1.0.42.151.g19de0aa6-1
- Update to 1.0.42.151.g19de0aa6

* Sun Sep 18 2016 Sérgio Basto <sergio@serjux.com> - 1.0.37.152.gc83ea995-1
- Update to 1.0.37.152.gc83ea995_42

* Wed Aug 31 2016 Sérgio Basto <sergio@serjux.com> - 1.0.36.120.g536a862f-2
- Add license tag

* Wed Aug 31 2016 Sérgio Basto <sergio@serjux.com> - 1.0.36.120.g536a862f-1
- Update to 1.0.36.120.g536a862f
- Remove require ffmpeg-compat
- Fix warning: %triggerpostun .: usage: . filename [arguments]

* Fri Jul 29 2016 Sérgio Basto <sergio@serjux.com> - 1.0.32.96.g3c8a06e6-1
- Update Spotify to 1.0.32.96.g3c8a06e6-37 for amd64, -3 for i386
- Move spotify-make to main package, no need dowload it every time
- Use branch devel of spotify-make, supports and install Spotify 1.0.32 correctly
- Update scriptlets https://fedoraproject.org/wiki/Packaging:Scriptlets#Icon_Cache
- Update __requires_exclude with libcurl.so and remove which aren't in use
  anymore
- Use Robxu9 commit.

* Wed May 06 2015 Sérgio Basto <sergio@serjux.com> - 0.9.17.1.g9b85d43.7-1
- Update to 0.9.17.1.g9b85d43.7 and fix rfbz #3408

* Fri Nov 21 2014 Alec Leamas <leamas.alec@gmail.com> - 0.9.11.27.g2b1a638.81-2
- Fix typo (3408)

* Tue Oct 28 2014 Alec Leamas <leamas@nowhere.net> - 0.9.11.27.g2b1a638.81-1
- Rebuilt from current amd64 version + new bundled libs in spotify-make
- Note: the actually installed version for i386 hosts is still 0.9.4.183

* Tue Feb 18 2014 Alec Leamas <leamas@nowhere.net> - 0.9.4.183.g644e24e.428-8
- Updating spec scriptlets, use new macros.
- Adding missing R: ffmpeg-compat and R:python2 to target package.
- Update bogus README copied from skype.

* Sun Jan 12 2014 Alec Leamas <leamas@nowhere.net> - 0.9.4.183.g644e24e.428-7
- Adding missing Requires: dbus-x11 to target package.

* Fri Dec 27 2013 Alec Leamas <leamas@nowhere.net> - 0.9.4.183.g644e24e.428-6
- Rebuild after F20 branching

* Wed Nov 27 2013 Alec Leamas <leamas@nowhere.net> - 0.9.4.183.g644e24e.428-5
- Updating %%triggerpostun

* Tue Nov 26 2013 Alec Leamas <leamas@nowhere.net> - 0.9.4.183.g644e24e.428-4
- Updating %%triggerun and %%postun.

* Tue Nov 26 2013 Alec Leamas <leamas@nowhere.net> - 0.9.4.183.g644e24e.428-3
- Updating %%postun
- Making description to free-format text.

* Tue Nov 26 2013 Alec Leamas <leamas@nowhere.net> - 0.9.4.183.g644e24e.428-2
- Adding %%triggerpostun
- Updating description

* Thu Oct 24 2013 Alec Leamas <leamas@nowhere.net> - 0.9.4.183.g644e24e.428-1
- Updating for  new upstream release.
- Adding LICENSE
- Updating URL:
- Smaller review fixes (layout etc.).
- Adding comment for eula.txt
- Adding README, final review remark fix.

* Sun May 05 2013 Alec Leamas <leamas@nowhere.net> - 0.9.0.133.gd18ed58.259-2
- Initial release
