%global tl_name euclideangeometry
%global tl_revision 67608

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2.2
Release:	%{tl_revision}.1
Summary:	Draw geometrical constructions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/euclideangeometry
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/euclideangeometry.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/euclideangeometry.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/euclideangeometry.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides tools to draw most of the geometrical
constructions that a high school instructor or bachelor degree professor
might need to teach geometry. The connection to Euclide depends on the
fact that in his times calculations were made with ruler, compass and
also with ellipsograph. This package extends the functionalities of the
curve2e package.

