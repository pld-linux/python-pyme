%define 	module	pyme
Summary:	The GPGME Interface for Python
Summary(pl):	Interfejs do GPGME dla jêzyka Python
Name:		python-%{module}
Version:	0.7.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pyme/pyme-%{version}.tar.gz
# Source0-md5:	94ec22f7f4babc5b1e9f0af8d73f05e0
URL:		http://pyme.sourceforge.net/
BuildRequires:	gpgme-devel >= 1:0.4.5
BuildRequires:	python-devel
BuildRequires:	swig
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyme is, for the most part, a direct interface to the C GPGME library.
However, it is re-packaged in a more Pythonic way - object-oriented
with classes and modules.

%description -l pl
Pyme jest, w sporej czê¶ci, bezpo¶rednim interfejsem do napisanej w
jêzyku C biblioteki GPGME. Jednak¿e jest ona spakietowana w bardziej
pythonowy sposób - zorientowany obiektowo z klasami i modu³ami.

%prep
%setup -q -n %{module}-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__make} swig \
	PYTHON=python
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name '*.py' | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog 
%dir %{py_sitedir}/pyme
%attr(755,root,root) %{py_sitedir}/pyme/_gpgme.so
%{py_sitedir}/pyme/*.py[co]
%{py_sitedir}/pyme/constants
