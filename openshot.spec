Summary:	OpenShot - Non-Linear Video Editor for Linux
Name:		openshot
Version:	2.4.2
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	https://github.com/OpenShot/openshot-qt/archive/v%{version}.tar.gz
# Source0-md5:	d5cdf9a71a4b02d54df18a83596c49f4
URL:		http://www.openshot.org/
BuildRequires:	python3-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
Requires:	python3-PyQt5
Requires:	python3-PyQt5-uic
Requires:	python3-httplib2
Requires:	python3-libopenshot >= 0.1.8
Requires:	python3-zmq
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenShot Video Editor is a free, open-source, non-linear video editor.
It can create and edit videos and movies using many popular video,
audio, and image formats. Create videos for YouTube, Flickr, Vimeo,
Metacafe, iPod, Xbox, and many more common formats!

Features include:
 - Multiple tracks (layers) Compositing, image overlays, and watermarks
 - Support for image sequences (rotoscoping) Key-frame animation Video
 - and audio effects (chroma-key) Transitions (lumas and masks)

%prep
%setup -q -n %{name}-qt-%{version}

%build
%{py3_build}

%install
rm -rf $RPM_BUILD_ROOT

%{py3_install}

%post
%update_mime_database
%scrollkeeper_update_post

%postun
%update_mime_database
%scrollkeeper_update_postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md
%attr(755,root,root) %{_bindir}/openshot-qt
%{_datadir}/mime/packages/openshot-qt.xml
%{_datadir}/applications/openshot-qt.desktop
%{_pixmapsdir}/openshot-qt.svg
%{py3_sitescriptdir}/%{name}_qt
%{py3_sitescriptdir}/openshot*.egg-info
