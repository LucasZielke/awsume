import os
import pathlib
from shutil import which

DEFAULT_ALIAS = 'alias awsume="source awsume"'
PYENV_ALIAS = r'alias awsume="source \$(pyenv which awsume)"'
PYENV_FISH_ALIAS = """function awsume
    source (pyenv which awsume.fish) $argv;
end
"""
FISH_ALIAS = """function awsume
    source (which awsume.fish) $argv;
end
"""


def main(shell: str, alias_file: str):
    alias_file = str(pathlib.Path(alias_file).expanduser())
    if shell == "fish":
        alias = PYENV_FISH_ALIAS if which("pyenv") else FISH_ALIAS
    else:
        alias = PYENV_ALIAS if which("pyenv") else DEFAULT_ALIAS

    basedir = os.path.dirname(alias_file)
    if basedir and not os.path.exists(basedir):
        os.makedirs(basedir)

    with open(alias_file, "a+") as af:
        if alias in af.read():
            print("Alias already in " + alias_file)
        else:
            af.write("\n#AWSume alias to source the AWSume script\n")
            af.write(alias)
            af.write("\n")
            print("Wrote alias to " + alias_file)
