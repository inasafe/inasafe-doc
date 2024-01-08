[![][InaSAFEImage]][website]

[![Build Status](https://travis-ci.org/inasafe/inasafe-doc.svg?branch=develop)](https://travis-ci.org/inasafe/inasafe-doc)

# InaSAFE Documentation

PDF versions of the Documentation are available here: http://inasafe.org/pdf/

## Preparing your Environment

The general workflow we recommend is:

1. Install the nix package manager
2. Checkout this project
3. Open this folder in a shell / terminal application
4. Open a nix-shell to install the build environment

### Install Nix package manager

If you are on ubuntu, windows (under WSL2) or macOS you can install the nix
package manager which will fetch all the dependencies needed to build this
project.

To do this, please go to the [Nix Download Page]() and follow the instructions
under `Nix: the package manager` as appropriate to your operating system.

A special note for NixOS users:

If you are a NixOS user, you already have the nix package manager. You can
additionally install [direnv](https://github.com/nix-community/nix-direnv)
which will create a seamless entry into the development environment.

### Checkout this project

You need to have a local copy of this project in order to build the documentation. To do that you can do:

```
# cd to your home dir
cd
# create a dev dir and move into it
mkdir dev
cd dev
# clone/copy the sources into it and go into the dir
git clone https://github.com/inasafe/inasafe-doc
```

### Open the project in your terminal

Open your favourite terminal and enter into this documentation folder:

```
cd pystac-nix
```

### Install the build environment

Now we can set up the build environment. Note that it will fetch a bunch of
packages from the internet, so having a good internet connection will help a
lot here.

```
nix-shell
```

Note: As mentioned above, if you have direnv set up on NixOS, you can skip this
step, it is automatic.

When the setup process completes, you will see something like this in your shell:


```
direnv: loading ~/dev/inasafe-doc/.envrc
direnv: using nix
Using venvShellHook
Executing venvHook
Skipping venv creation, './.venv' already exists
Finished executing venvShellHook
direnv: export +AR +AS +CC +CONFIG_SHELL +CXX +DETERMINISTIC_BUILD +GETTEXTDATADIRS +GETTEXTDATADIRS_FOR_TARGET +GSETTINGS_SCHEMAS_PATH +HOST_PATH +IN_NIX_SHELL +LD +NIX_BINTOOLS +NIX_BINTOOLS_WRAPPER_TARGET_HOST_x86_64_unknown_linux_gnu +NIX_BUILD_CORES +NIX_BUILD_TOP +NIX_CC +NIX_CC_WRAPPER_TARGET_HOST_x86_64_unknown_linux_gnu +NIX_CFLAGS_COMPILE +NIX_ENFORCE_NO_NATIVE +NIX_HARDENING_ENABLE +NIX_LDFLAGS +NIX_SSL_CERT_FILE +NIX_STORE +NM +OBJCOPY +OBJDUMP +PYTHONHASHSEED +PYTHONNOUSERSITE +PYTHONPATH +RANLIB +READELF +SIZE +SSL_CERT_FILE +STRINGS +STRIP +SYSTEM_CERTIFICATE_PATH +TEMP +TEMPDIR +TMP +TMPDIR +VIRTUAL_ENV +VIRTUAL_ENV_PROMPT +XML_CATALOG_FILES +_PYTHON_HOST_PLATFORM +_PYTHON_SYSCONFIGDATA_NAME +__structuredAttrs +buildInputs +buildPhase +builder +cmakeFlags +configureFlags +depsBuildBuild +depsBuildBuildPropagated +depsBuildTarget +depsBuildTargetPropagated +depsHostHost +depsHostHostPropagated +depsTargetTarget +depsTargetTargetPropagated +doCheck +doInstallCheck +mesonFlags +name +nativeBuildInputs +out +outputs +patches +phases +postShellHook +postVenvCreation +preferLocalBuild +propagatedBuildInputs +propagatedNativeBuildInputs +shell +shellHook +stdenv +strictDeps +system +venvDir ~GI_TYPELIB_PATH ~PATH ~XDG_DATA_DIRS
```

You can further validate that everything is set up correctly by running 


```
pip freeze
```

You should see a list of packages similar to those listed below:

```
six==1.16.0
```


## Building the docs
 
We are now going to use that inasafe-doc directory as source and output directory for the HTML


```
scripts/english_build.sh
```

## Viewing the docs

After building the docs, you can run a lightweight web server to view the
generated web pages:

```
httplz docs/output/html/en/
```


[InaSAFEImage]: http://inasafe.org/en/_static/img/logo.png
[website]: http://inasafe.org/


Tim Sutton

2024