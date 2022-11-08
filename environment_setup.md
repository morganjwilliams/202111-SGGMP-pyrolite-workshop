# Setting up an Environment with Anaconda

This document gives a high-level overview of what you'll need to get these
notebooks (or other similar ones) running on your own computer.

## Get a Python Distribution

There are few options for getting a Python distribution onto your local computer.
I tend to use Anaconda where possible, and I recommend this to scientists
and those looking to use Python from a data-science perspective. You can also
download Python from the [official website](https://www.python.org/downloads/)
or pursue an alternative distribution. For our purposes, we'll use Anaconda
(optionally with a few other tools):
1. Get a [distribution of Anaconda](https://www.anaconda.com/products/distribution),
  which will provide Python bundled together with a range of packages useful
  for scientific and data science purposes.
2. Run through the install process (consider restarting, especially on Windows).
  You should now have access to `conda` in a terminal.
  * On Windows, you should now find `Anaconda Prompt (Anaconda3)` or similar
      in your start menu.
  * On Linux (your terminal of choice) and MacOS (Terminal, or your
      post-installed terminal of choice), it's more likely that installing
      Anaconda has added some additional lines to your shell profile which
      automatically *activates* the base environment.


## Set up an Environment

A key recommendation which might save you headaches down the line is to use the
concepts of 'environments'. Environments in a simple sense can be thought of as
managed separate instances/versions of Python together with accompanying
third-party packages. By using separate environments for different projects,
you can deal with otherwise difficult conflicts (e.g. this project needs this
specific version, but it'll break something in another). This practice should also
help you avoid critical errors which are typically easier solved by removing the
whole distribution and starting again (document how environments are created,
in case it does come to this down the line...).

Anaconda (or `conda`) has it's own environment manager, and there are some lower
level Pythonic ones which each do slightly different things (e.g. `venv`,
`pipenv`, `pyenv`). Within Anaconda, by default when installing it creates a
`base` distribution (you should see `(base)` in your terminal prompt; on
Windows this will likely be `(base)  C:\Users\...`).

Different environment managers use different formats for on-disk representations
of requirements. The Python package manager `pip` uses a list of
packages (and optionally versions) in `requirements.txt`, but `conda` uses
an `environment.yml` file in which you can specify:
* A name for the environment
* Where to get packages from (`channels`); in some cases you can specify e.g.
  internal repositories. For our purposes we'll use `conda-forge` and `defaults`.
* The `dependencies` -  packages to install using `conda`, and for things which aren't available
  via those channels, the packages to install using `pip`.

#### Suggestions: Before you Start

* If you're working in a commercial environment, check with your local IT team
  about licensing of Anaconda (if it doesn't exist, consider using something else
  or asking for it).
* Have a look at the
  [`conda` documentation](https://docs.conda.io/projects/conda/en/latest/index.html),
  and in particular
  [the bits around managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
* Consider installing [`mamba`](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html)
  for faster environment solving (the processing of working out which combination
  of package versions will work together, within the constraints you give).
    * `conda install -c conda-forge mamba`
* Consider whether you want to install some *general* tools
  (where versions likely do not matter much) in your base environment.
  I tend to do this for things like `git`, `black` (a code formatter) and some
  utilities for Jupyterlab (a spellchecker, notebook formatter). If you're just
  making one new environment, this isn't necessary.

#### Creating the Environment from This Workshop

To create the environment for this workshop, you'll need the `./binder/environment.yml` file. You can download this from the repo, or copy and paste it
to a local text file which you rename to `environment.yml`. Put it in a place you can find it later (maybe a folder for what you want to work on under `<USER>/Documents/` or similar).

* Open an terminal and navigate to the directory in which you left the environment file (`cd` to change directory, e.g. `cd C:\Users\<USER>\Documents\<PROJECT>\` on windows).
* If you have installed `mamba` in your base directory:
  * `mamba env create -f environment.yml`
* Otherwise, if you're using base `conda`:
  * `conda env create -f environment.yml`
* To be able to see this environment within Jupyter (the dropdown top-right in
  Jupyterlab), you can now install/register the respective `ipython` kernel
  (note that `python` may need to be `python3` depending on your operating
  system):
  * `python -m ipykernel install --user --name sggmp-workshop-env`
* Check that the environment created OK and you can work within it:
  * `conda activate sggmp-workshop-env` | Activate the environment.
  * `python` | Launches an interactive Python shell where you can type Python commands.
    * Type `exit()` or `CTRL-Z` to exit, at least on Windows.

## Working with the Environment

To boot up an environment and start work on a project, I usually proceed via the
following steps:
* Spin up a terminal as noted above (e.g. `Anaconda Prompt` on Windows)
* Activate the environment:
  * `conda activate sggmp-workshop-env`
* Launch any programs you want to work in from here, e.g. Jupyter lab:
  * `jupyter lab`
* When you're finished and want to move to another project/environment, first
  deactivate the one you're in:
  * `conda deactivate sggmp-workshop-env`

## Some Quick Final Tips

* As you get more comfortable writing code and moving out of notebooks,
  try and find a good code editor/integrated development environment
  which suits you. Anaconda ships with Spyder, but there are many alternatives
  (e.g. Visual Studio Code is pretty common on Windows).
* Whenever modifying environments (e.g. installing new packages,
  removing packages, updating packages etc), make sure you're in the right environment (and ideally, not in `base`...).
* `mamba` has saved me many hours of the programming equivalent
  of 'watching paint dry' waiting for packages to download and install.
* If you're working with other peoples code, or simply trying to keep track of
  your own evolving project, I'd suggest getting to terms with the basics of
  `git` and some standard workflows for managing versions and branches of
  code repositories.
* Keep in touch, happy to provide some support on the pyrolite front, with
  hopefully some future workshops down the line. The
  [documentation](https://pyrolite.rtfd.io) should be your first point of call
  though.
* I'm also happy to discuss work in the open (e.g. on open GitHub repositories)
  and some good practices around those kinds of things if you're keen.
