Summary:	Default themes for GNOME environment
Name:		gnome-themes-standard
Version:	3.14.0
Release:	3
License:	LGPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-themes-standard/3.14/%{name}-%{version}.tar.xz
# Source0-md5:	fe121e92298b527f6f614050bddd866a
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
# gtk.gresource.xml: Error on line 41 char 1: Error processing input file with to-pixdata:
# failed to load "./assets/dnd-counter.svg": Couldn't recognize the image file format for file './assets/dnd-counter.svg'
BuildRequires:	gdk-pixbuf-rsvg
BuildRequires:	gettext-devel
BuildRequires:	gtk+-update-icon-cache
BuildRequires:	gtk+-devel >= 2:2.24.15
BuildRequires:	gtk+3-devel >= 3.14.0
BuildRequires:	intltool
BuildRequires:	librsvg-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires:	adwaita-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Default themes for GNOME 3 environment.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/*/*/*/*.la

CD=`pwd`
cd $RPM_BUILD_ROOT%{_iconsdir}
for dir in *
    do
	gtk-update-icon-cache -ft $RPM_BUILD_ROOT%{_iconsdir}/$dir
	done
cd $CD

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/2.10.0/engines/libadwaita.so
%{_datadir}/themes/Adwaita
%{_datadir}/themes/HighContrast
%{_iconsdir}/HighContrast

