with import <nixpkgs> { };

let
  # For packages pinned to a specific version
  pinnedHash = "933d7dc155096e7575d207be6fb7792bc9f34f6d"; 
  pinnedPkgs = import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/${pinnedHash}.tar.gz") { };
  pythonPackages = pinnedPkgs.python3Packages;
in pkgs.mkShell rec {
  name = "impurePythonEnv";
  venvDir = "./.venv";
  buildInputs = [
    # A Python interpreter including the 'venv' module is required to bootstrap
    # the environment.
    pythonPackages.python
    # This executes some shell code to initialize a venv in $venvDir before
    # dropping into the shell
    pythonPackages.venvShellHook
    # By preference, install packages from nixpkgs first, 
    # falling back to requirements.txt if that is not possible
    pythonPackages.six
    pythonPackages.jinja2
    pythonPackages.markupsafe
    pythonPackages.pygments
    pythonPackages.docutils
    pythonPackages.polib
    #pythonPackages.sphinx-intl
    pythonPackages.twitter
    
    pinnedPkgs.sphinx
    pinnedPkgs.transifex-client
    pinnedPkgs.argparse
    pinnedPkgs.rpl
    pinnedPkgs.gettext
    # Simple http server to test the built docs
    pinnedPkgs.httplz 
    
  ];

  # Run this command, only after creating the virtual environment
  postVenvCreation = ''
    unset SOURCE_DATE_EPOCH
    pip install -r requirements.txt 
  '';

  # Note!! Adding content to shellHook below will prevent requirements.txt
  # being installed.
  shellHook = ''
  '';
  # Now we can execute any commands within the virtual environment.
  # This is optional and can be left out to run pip manually.
  postShellHook = ''
    # allow pip to install wheels
    unset SOURCE_DATE_EPOCH
  '';

}
