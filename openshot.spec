Summary:	OpenShot - Non-Linear Video Editor for Linux
Name:		openshot
Version:	1.4.3
Release:	4
License:	GPL v3
Group:		X11/Applications
Source0:	http://launchpad.net/openshot/1.4/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	5ec82a7e8b7700ee4a359458aedf19e9
Patch0:		%{name}-locale_dir.patch
Patch1:		openshot-bug-722285.patch
URL:		http://www.openshot.org/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
Requires:	python-httplib2
Requires:	python-mlt
Requires:	python-pygoocanvas
Requires:	python-pygtk-glade
Requires:	python-pygtk-gtk
Requires:	python-pygtk-pango
Requires:	python-pyxdg
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
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}{/gnome/help,/omf},%{_localedir}}

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

# clean up and move locales to the system localedir
rm -r $RPM_BUILD_ROOT/%{py_sitescriptdir}/%{name}/locale/OpenShot
rm $RPM_BUILD_ROOT/%{py_sitescriptdir}/%{name}/locale/README
rm $RPM_BUILD_ROOT/%{py_sitescriptdir}/%{name}/locale/*/LC_MESSAGES/*.po
mv $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/locale/* \
	$RPM_BUILD_ROOT/%{_localedir}
rmdir $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/locale

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

rm $RPM_BUILD_ROOT%{_prefix}/lib/mime/packages/%{name}

cp -R docs/gnome $RPM_BUILD_ROOT%{_datadir}/gnome/help/%{name}
cp -R docs/omf $RPM_BUILD_ROOT%{_datadir}/omf/%{name}

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ady,gaa,jv,shn}

%find_lang %{name} --all-name --with-gnome --with-omf

%post
%update_mime_database
%scrollkeeper_update_post

%postun
%update_mime_database
%scrollkeeper_update_postun

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/openshot
%attr(755,root,root) %{_bindir}/openshot-render
%{_datadir}/mime/packages/*
%{_mandir}/man1/openshot.1*
%{_mandir}/man1/openshot-render.1*
%{_pixmapsdir}/openshot.svg
%{_desktopdir}/openshot.desktop
%{py_sitescriptdir}/%{name}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/openshot*.egg-info
%endif
