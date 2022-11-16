Name:		texlive-euclideangeometry
Version:	60697
Release:	1
Summary:	Draw geometrical constructions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/euclideangeometry
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euclideangeometry.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euclideangeometry.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euclideangeometry.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides tools to draw most of the geometrical
constructions that a high school instructor or bachelor degree
professor might need to teach geometry. The connection to
Euclide depends on the fact that in his times calculations were
made with ruler, compass and also with ellipsograph. This
package extends the functionalities of the curve2e package.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/euclideangeometry
%{_texmfdistdir}/tex/latex/euclideangeometry
%doc %{_texmfdistdir}/doc/latex/euclideangeometry

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
