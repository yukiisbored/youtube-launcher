let
  pkgs = import (builtins.fetchTarball {
    url = "https://github.com/NixOS/nixpkgs/archive/60cce7e5e1fdf62421ef6d4184ee399b46209366.tar.gz";
    sha256 = "100xrb925cana1kfd0c7gwkjjalq891vfgr0rn1gl9j8gp3l3gx6";
  }) {};

  mpv = pkgs.mpv;
in
pkgs.python38Packages.buildPythonApplication {
  pname = "youtube-launcher";
  src = ./.;
  version = "0.1";

  buildInputs = [ mpv ];
  propagatedBuildInputs = with pkgs.python38Packages; [ pyqt5 ];
  nativeBuildInputs = with pkgs.libsForQt5.qt5; [ qtbase wrapQtAppsHook ];

  postPatch = ''
    substituteInPlace youtube_launcher.py \
      --replace "'mpv'" "'${mpv}/bin/mpv'"
  '';

  preFixup = ''
    makeWrapperArgs+=("''${qtWrapperArgs[@]}")
  '';
}
