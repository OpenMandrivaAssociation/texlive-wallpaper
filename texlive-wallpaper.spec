Name:		texlive-wallpaper
Version:	15878
Release:	1
Summary:	Easy addition of wallpapers (background images) to LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/wallpaper
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wallpaper.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wallpaper.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
