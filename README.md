pypiece
=======

Wrapper around pip for use with flaky connections.

Basic idea behind it is that default behaviour of `pip` to download all packages at one
and compile them can get pretty frustrating in situations, where single error in 
downloading or installing a package can result in repeating whole process all
over again.

`pypiece` tries to get around that by trying to download and install each package
separately, by calling `pip` for each line of requirements.txt. In the end it
outputs list of successfully installed packages and ones that failed.

Usage
-----

<pre>
pypiece < requirements file > < -- PIP options >
</pre>

Available options:
  
 - `--pip` - specify pip binary to use
 -  `--retries <N>` - try to reinstall failing package _N_ times (default: 3).
 -  `--venv <name>` - install to virtualenvwrapper created virtual environment _name_.

pip arguments
-------------
If `--` is found in command line, then all arguments
after it will be passed unchanged to `pip` executable on every call.

For example, 
<pre>pypiece requirements.txt -- -i https://my.pypi.repo</pre>

is equivalent to 
<pre>pip install -r requirements.txt -i https://my.pypi.repo</pre>

Examples
--------

<pre>pypiece requirements.txt</pre>
We will try to install every package found in _requirements.txt_ one by one, retrying 
3 times if necessary.

<pre>pypiece --venv test requirements.txt</pre>
`pypiece` will try to find virtualenv _test_ in directory specified by _WORKON_HOME_ 
variable. If successful, it will use `pip` from this virtualenv.

<pre>pypiece --pip my_env/bin/pip requirements.txt</pre>
`pypiece` will try to use provided `pip` binary for installation purposes.
