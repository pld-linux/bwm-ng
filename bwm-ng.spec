Summary:	Bandwidth monitor - display bandwidth usage on all interfaces
Summary(pl):	Bandwidth monitor - wy¶wietlanie obci±¿enia na interfejsach
Name:		bwm-ng
Version:	0.4
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.gropp.org/%{name}-%{version}.tar.gz
# Source0-md5:	4fc0839ae212bc0b805fc4adeb55a3ac
URL:		http://www.gropp.org/
BuildRequires:	libstatgrab-devel
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

%prep
%setup -q

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags} -Wall -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}
install bwm-ng $RPM_BUILD_ROOT%{_bindir}
install bwm-ng.conf-example $RPM_BUILD_ROOT%{_sysconfdir}/bwm-ng.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README changelog
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/*
