Summary:	Bandwidth monitor - display bandwidth usage on all interfaces
Summary(pl.UTF-8):	Bandwidth monitor - wyświetlanie obciążenia na interfejsach
Name:		bwm-ng
Version:	0.6.1
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.gropp.org/bwm-ng/%{name}-%{version}.tar.gz
Patch0:		%{name}-procfile.patch
URL:		http://www.gropp.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstatgrab-devel >= 0.91
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bandwidth Monitor NG is a small and simple console-based bandwidth
monitor for Linux, BSD, and Mac OS X, or other systems with either
/proc/net/dev, netstat (Linux and BSD), getifaddrs, sysctl, or
libstatgrab. You can choose whether to show all interfaces or only
those interfaces that are up. Output is possible as plain console,
curses, CSV, or HTML. Unlimited interfaces are supported and will be
added dynamically while running.

%description -l pl.UTF-8
Bandwidth Monitor NG to mały i prosty działający na terminalu
tekstowym monitor wykorzystania pasma dla Linuksa, BSD i Mac OS X lub
innych systemów z interfejsem /proc/net/dev, netstat, getifaddrs,
sysctl lub libstatgrab. Można wybrać, czy mają być pokazywane
wszystkie interfejsy, czy tylko aktualnie włączone. Obsługiwane jest
wyjście na zwykłą konsolę, przez curses, w CSV lub w HTML-u.
Obsługiwana jest nieograniczona liczba interfejsów, będą one dodawane
dynamicznie w trakcie działania programu.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} \
	CFLAGS="%{rpmcflags} -Wall -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man1}

install src/bwm-ng $RPM_BUILD_ROOT%{_bindir}
install bwm-ng.conf-example $RPM_BUILD_ROOT%{_sysconfdir}/bwm-ng.conf
install bwm-ng.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS bwm-ng.css
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bwm-ng.conf
%{_mandir}/man1/*
