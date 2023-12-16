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
pystac==1.9.0
python-dateutil==2.8.2
six==1.16.0
```


## Building the docs
 
We are now going to use that inasafe-doc directory as source and output directory for the 


```
scripts/pre_translate.sh
scripts/post_translate.sh 
scripts/english_build.sh
```

You can also build the docs for a single language:

```
scripts/post_translate.sh id html
```

## Viewing the docs

After building the docs, you can run a lightweight web server to view the
generated web pages:

```
httplz docs/output/html/
```


Translating the english InaSAFE Documentation
=============================================

Every language has it's own maintainer, please contact them,
if you want to help. You find a list of current language maintainers at the
end of this document. If your language is not listed, join our community by
sending a mail to <inasafe-users+subscribe@googlegroups.com> and ask for
help.

HowTo for language maintainers
------------------------------

* get an account on github.com
* install required tools on your computer
* login to github and create a fork of the inasafe-doc repository that other
  translators can work with.

Translators now can create their own fork from the forked repository of the
maintainer, commit their translations to their own forked repository and send
pull request to the language maintainer's repository. Once the maintainer
receives a pull request, he should check the changes, accept the pull request
and merge the changes with the official inasafe-doc repository.

Workflow for adding a new language
----------------------------------

* add your locale code in the pre_translate.sh script in the line with 'LOCALE='
* run 'scripts/pre_translate.sh'. There will be a new directory in the i18n
  directory for your language, containing the po-files for all source files
* create an empty(!) directory in the resources directory for your language. The
  idea is to ONLY put images in exact the same directory structure if you
  want an image to be 'translated'. As default the english one will be used
  from the 'en' directory, and only if there is an translated one it will be
  found and used.
* add your locale code in the post_translate.sh script in the line with
  'LOCALE='

HowTo for translators
---------------------

* get an account on github.com
* install required tools on your computer
* login to github and create a fork of the inasafe-doc repository from your
  language maintainer.
* git clone your forked inasafe-doc repository to your computer
* run './scripts/pre_translate.sh &lt;language&gt;' locally to build the
  translation files
* translate the .po files locally and use an offline editor.
  [QtLinguist](https://code.google.com/p/qtlinguistdownload/)
  being the highly recommended choice.
* with the english documentation from ./docs/source/ run '
  ./scripts/post_translate.sh languagecode' locally again to check your
  translation
* files translated need to be "synchronized" with the ones in the directory of
  the forked repo. Commit your changes to your private forked repository and
  create a pull request on github. It means that you send a request to the
  owners of the repository you forked (language maintainer) asking him to
  accept your translations and move them to the "original repository". For
  doing that go on github.com, browse on the directory of your repository and
  click pull request (https://help.github.com/articles/using-pull-requests).
* your language maintainer will take care that every significant translation go
  into the master repository.
* Generally, as soon as you finish editing one or more .po files, you should
  commit as soon as possible the edits to the git repository,
  in order to minimize the possibility of conflicts.

The maintainer and translator should update and check the translations
regularly. Therefore you should 'git pull' when you start to work and run the
'scripts/pre_translate.sh &lt;language&gt;' and 'scripts/post_translate.sh
&lt;language&gt;' script after every significant change in the documentation.
This will generate and update the .po files needed for translations. If all
is fine, take care, that the translation go into the repository of your
language maintainer.

[InaSAFEImage]: http://inasafe.org/en/_static/img/logo.png
[website]: http://inasafe.org/
