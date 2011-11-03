# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/wallpaper
# catalog-date 2007-01-20 20:21:37 +0100
# catalog-license lppl
# catalog-version 1.10
Name:		texlive-wallpaper
Version:	1.10
Release:	1
Summary:	Easy addition of wallpapers (background images) to LaTeX documents, including tiling
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/wallpaper
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wallpaper.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wallpaper.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This collection contains files to add wallpapers (background
images) to LaTeX documents. It uses the eso-pic package, but
provides simple commands to include effects such as tiling. An
example is provided, which works under both LaTeX and pdfLaTeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}