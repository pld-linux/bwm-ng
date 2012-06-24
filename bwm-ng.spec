Summary:	Bandwidth monitor - display bandwidth usage on all interfaces
Summary(pl):	Bandwidth monitor - wy�wietlanie obci��enia na interfejsach
Name:		bwm-ng
Version:	0.5
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.gropp.org/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	4c5197527c985dc8b45973dfd00deca0
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

%description -l pl
Bandwidth Monitor NG to ma�y i prosty dzia�aj�cy na terminalu
tekstowym monitor wykorzystania pasma dla Linuksa, BSD i Mac OS X lub
innych system�w z interfejsem /proc/net/dev, netstat, getifaddrs,
sysctl lub libstatgrab. Mo�na wybra�, czy maj� by� pokazywane
wszystkie interfejsy, czy tylko aktualnie w��czone. Obs�ugiwane jest
wyj�cie na zwyk�� konsol�, przez curses, w CSV lub w HTML-u.
Obs�ugiwana jest nieograniczona liczba interfejs�w, b�d� one dodawane
dynamicznie w trakcie dzia�ania programu.

%prep
%setup -q

%build
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
%doc AUTHORS README changelog
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bwm-ng.conf
%{_mandir}/man1/*
