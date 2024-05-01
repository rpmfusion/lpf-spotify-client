# %%bal will not work here, lazy evaluation needed.

#devel branch
#global github_repo https://github.com/leamas/spotify-make/archive/%{commit}
%global github_repo https://github.com/sergiomb2/spotify-make/archive/%{commit}
# devel branch
%global commit      62e266b593e4031a9a9209fbd17f287cc4cfb7a5
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%define         target_pkg %(t=%{name}; echo ${t#lpf-})

Name:           lpf-spotify-client
                # Upstream spotify version, verbatim.
Version:        1.2.31.1205
Release:        1%{?dist}
Summary:        Spotify music player native client package bootstrap

License:        MIT
URL:            https://github.com/leamas/spotify-make
Group:          Development/Tools
ExclusiveArch:  i686 x86_64
#BuildArch:      noarch
%global debug_package %{nil}

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
* Wed May 01 2024 Valentin Maerten <maerten.valentin@gmail.com> - 1.2.31.1205-1
- Update to 1.2.31.1205.g4d59ad7c

* Mon Dec 18 2023 Sérgio Basto <sergio@serjux.com> - 1.2.26.1187-1
- Update to 1.2.26.1187.g36b715a1

* Mon Oct 30 2023 Sérgio Basto <sergio@serjux.com> - 1.2.22.982-1
- Update to 1.2.22.982.g794acc0a

* Thu Aug 31 2023 Sérgio Basto <sergio@serjux.com> - 1.2.18.999-1
- Update to 1.2.18.999.g9b38fc27

* Tue Jun 20 2023 Sérgio Basto <sergio@serjux.com> - 1.2.13.661-1
- Update to 1.2.13.661.ga588f749

* Mon May 29 2023 Sérgio Basto <sergio@serjux.com> - 1.2.9.743-1
- Update to 1.2.9.743.g85d9593d

* Mon Apr 03 2023 Sérgio Basto <sergio@serjux.com> - 1.2.8.923-1
- Update to 1.2.8.923.g4f94bf0d

* Tue May 03 2022 Sérgio Basto <sergio@serjux.com> - 1.1.84.716-2
- Update to 1.1.84.716.gc5f8b819-2
- Exclude from provides all internal shared libraries

* Tue May 03 2022 Sérgio Basto <sergio@serjux.com> - 1.1.84.716-1
- Update to 1.1.84.716.gc5f8b819

* Sat Mar 26 2022 Sérgio Basto <sergio@serjux.com> - 1.1.80.699-1
- Update to 1.1.80.699.gc3dac750

* Wed Nov 24 2021 Sérgio Basto <sergio@serjux.com> - 1.1.72.439-1
- Update to 1.1.72.439.gc253025e

* Sun Sep 26 2021 Sérgio Basto <sergio@serjux.com> - 1.1.68.632-1
- Update to 1.1.68.632.g2b11de83

* Thu Sep 02 2021 Sérgio Basto <sergio@serjux.com> - 1.1.67.586-1
- Update to 1.1.67.586.gbb5ef64e

* Thu Apr 29 2021 Leigh Scott <leigh123linux@gmail.com> - 1.1.56.595-1
- Update to 1.1.56.595.g2d2da0de

* Tue Mar 23 2021 Sérgio Basto <sergio@serjux.com> - 1.1.55.498-1
- Update to 1.1.55.498.gf9a83c60

* Fri Sep 18 2020 Sérgio Basto <sergio@serjux.com> - 1.1.42.622-1
- Update to 1.1.42.622.gbd112320

* Mon Apr 27 2020 Sérgio Basto <sergio@serjux.com> - 1.1.26.501-1
- Update to 1.1.26.501.gbe11e53b

* Fri Oct 18 2019 Sérgio Basto <sergio@serjux.com> - 1.1.10.546-3
- Fix commit of spotify-make in spotify-client.spec.in

* Sat Sep 28 2019 Sérgio Basto <sergio@serjux.com> - 1.1.10.546-2
- Update spotify-make rfbz#5395

* Thu Jul 25 2019 Leigh Scott <leigh123linux@gmail.com> - 1.1.10.546-1
- Update to 1.1.10.546.ge08ef575

* Sun May 05 2019 Sérgio Basto <sergio@serjux.com> - 1.1.5.153-1
- Update to 1.1.5.153.gf614956d

* Sat Feb 16 2019 Sérgio Basto <sergio@serjux.com> - 1.1.0.237-1
- Update to 1.1.0.237.g378f6f25

* Tue Jan 29 2019 Sérgio Basto <sergio@serjux.com> - 1.0.98.78-1
- Update to 1.0.98.78.gb45d2a6b

* Sat Jan 12 2019 Sérgio Basto <sergio@serjux.com> - 1.0.96.181-1
- Update to 1.0.96.181.gf6bc1b6b

* Tue Dec 11 2018 Sérgio Basto <sergio@serjux.com> - 1.0.94.262-1
- Update to 1.0.94.262.g3d5c231c

* Sat Oct 27 2018 Sérgio Basto <sergio@serjux.com> - 1.0.92.390-1
- Update to 1.0.92.390.g2ce5ec7d

* Thu Sep 20 2018 Sérgio Basto <sergio@serjux.com> - 1.0.89.313-1
- Update to 1.0.89.313.g34a58dea

* Fri Aug 31 2018 Sérgio Basto <sergio@serjux.com> - 1.0.88.353-1
- Update to 1.0.88.353.g15c26ea1

* Tue Jun 26 2018 Sérgio Basto <sergio@serjux.com> - 1.0.80.480-1
- Update to 1.0.80.480.g51b03ac3

* Fri May 04 2018 Sérgio Basto <sergio@serjux.com> - 1.0.79.223-1
- Update to 1.0.79.223.g92622cc2

* Thu Apr 12 2018 Sérgio Basto <sergio@serjux.com> - 1.0.77.338-2
- Requires exclude libcurl-gnutls.so.4 and centos-redhat-libcurl-gnutls-workaround

* Wed Apr 11 2018 Sérgio Basto <sergio@serjux.com> - 1.0.77.338-1
- Update to 1.0.77.338.g758ebd78

* Sun Mar 25 2018 Sérgio Basto <sergio@serjux.com> - 1.0.77.336-1
- Update to 1.0.77.336.g0d3547d9

* Sat Mar 03 2018 Sérgio Basto <sergio@serjux.com> - 1.0.72.117-1
- Update to 1.0.72.117.g6bd7cc73

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.0.70.399-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Sérgio Basto <sergio@serjux.com> - 1.0.70.399-1
- Update to 1.0.70.399.g5ffabd56

* Mon Jan 01 2018 Sérgio Basto <sergio@serjux.com> - 1.0.69.336-1
- Update to 1.0.69.336.g7edcc575

* Sun Nov 26 2017 Sérgio Basto <sergio@serjux.com> - 1.0.67.582-1
- Update to 1.0.67.582.g19436fa3

* Sat Nov 04 2017 Sérgio Basto <sergio@serjux.com> - 1.0.66.478-1
- Update to 1.0.66.478.g1296534d

* Tue Oct 24 2017 Sérgio Basto <sergio@serjux.com> - 1.0.64.407-1
- Update to 1.0.64.407.g9bd02c2d

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.0.59.395-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Sérgio Basto <sergio@serjux.com> - 1.0.59.395-1
- Update to 1.0.59.395.ge6ca9946

* Sat Jun 24 2017 Sérgio Basto <sergio@serjux.com> - 1.0.57.474-2
- do src.rpm just to work in the same arch that was build and just download one
  source instead 2

* Sat Jun 24 2017 Sérgio Basto <sergio@serjux.com> - 1.0.57.474-1
- Update to 1.0.57.474.gca9c9538

* Sun Jun 11 2017 Sérgio Basto <sergio@serjux.com> - 1.0.55.487-2
- ExclusiveArch:  i686 x86_64 , /usr/lib64/spotify-client/spotify only provided
  for i386 and x86_64

* Wed May 24 2017 Sérgio Basto <sergio@serjux.com> - 1.0.55.487-1
- Update to 1.0.55.487.g256699aa

* Mon May 15 2017 Sérgio Basto <sergio@serjux.com> - 1.0.53.758-2
- Improve version numbers

* Sat Apr 15 2017 Sérgio Basto <sergio@serjux.com> - 1.0.53-1
- Update to 1.0.53.758

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.0.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 13 2017 Pedro Albuquerque Santos <petersaints@gmail.com.com> - 1.0.49-2
- Update to spotify-client_1.0.49.125.g72ee7853-111_amd64.deb and spotify-client_1.0.49.125.g72ee7853-22_i386.deb

* Sun Feb 12 2017 Sérgio Basto <sergio@serjux.com> - 1.0.49-1
- Update to 1.0.49

* Wed Feb 01 2017 Sérgio Basto <sergio@serjux.com> - 1.0.48-1
- Update to 1.0.48

* Tue Jan 17 2017 Sérgio Basto <sergio@serjux.com> - 1.0.47-1
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
