%global tl_name zxjafbfont
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Fallback CJK font support for xeCJK
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/japanese/zxjafbfont
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zxjafbfont.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zxjafbfont.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Fallback CJK font support for xeCJK

