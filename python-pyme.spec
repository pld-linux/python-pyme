%include	/usr/lib/rpm/macros.python
%define 	module pyme

Summary:	The GPGME Interface for Python.
Summary(pl):	Interfejs do GPGME dla jêzyka Python.
Name:		python-%{module}
Version:	0.5.1
Release:	1
License:	GPL
Group:		Libraries/Python
######		Unknown group!
#Source0:	http://gopher.quux.org:70/devel/pyme/pyme_0.5.1.tar.gz
Source0:	http://gopher.quux.org:70/devel/%{module}/%{module}_%{version}.tar.gz
URL:		http://gopher.quux.org:70/devel/pyme
BuildRequires:	gpgme-devel
BuildRequires:	python-devel

Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

Pyme is, for the most part, a direct interface to the C GPGME library.
However, it is re-packaged in a more Pythonic way -- object-oriented
with classes and modules.

%description -l pl
Pyme jest, w sporej czê¶ci, bezpo¶rednim interfejsem do napisanej w
jêzyku C biblioteki GPGME. Jednak¿e, jest spakietowana w bardziej
pythonowy sposób - zorientowany obiektowo z klasami i modu³ami.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CLFAGS
# python setup.py # build, or what ?

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python setup.py install \
        --root=$RPM_BUILD_ROOT --optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc CREDITS ChangeLog README doc
#%{py_sitedir}/%{module}/*.so
#%{py_sitedir}/%{module}/*.py?
%{py_sitedir}/%{module}
