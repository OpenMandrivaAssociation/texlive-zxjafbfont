# revision 28539
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-zxjafbfont
Version:	20131009
Release:	9
Summary:	TeXLive zxjafbfont package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zxjafbfont.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zxjafbfont.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive zxjafbfont package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/zxjafbfont/zxjafbfont.sty
%doc %{_texmfdistdir}/doc/latex/zxjafbfont/LICENSE
%doc %{_texmfdistdir}/doc/latex/zxjafbfont/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
