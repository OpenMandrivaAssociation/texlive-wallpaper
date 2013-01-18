# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/wallpaper
# catalog-date 2007-01-20 20:21:37 +0100
# catalog-license lppl
# catalog-version 1.10
Name:		texlive-wallpaper
Version:	1.10
Release:	3
Summary:	Easy addition of wallpapers (background images) to LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/wallpaper
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wallpaper.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wallpaper.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This collection contains files to add wallpapers (background
images) to LaTeX documents. It uses the eso-pic package, but
provides simple commands to include effects such as tiling. An
example is provided, which works under both LaTeX and pdfLaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/wallpaper/wallpaper.sty
%doc %{_texmfdistdir}/doc/latex/wallpaper/README
%doc %{_texmfdistdir}/doc/latex/wallpaper/example/TGTamber.png
%doc %{_texmfdistdir}/doc/latex/wallpaper/example/auto/example.el
%doc %{_texmfdistdir}/doc/latex/wallpaper/example/example.tex
%doc %{_texmfdistdir}/doc/latex/wallpaper/example/hya.png
%doc %{_texmfdistdir}/doc/latex/wallpaper/wallpapermanual.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
