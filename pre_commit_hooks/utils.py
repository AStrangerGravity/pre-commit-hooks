from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import string
import subprocess

# Taken from: http://code.activestate.com/recipes/173220-test-if-a-file-or-string-is-text-or-binary/

KNOWN_BINARY_FILE_EXT = ['.pdf']
ALLOWED_NON_PRINTABLE_THRESHOLD = 0.15

def is_textfile(filename, blocksize=512):
    if any(filename.endswith(ext) for ext in KNOWN_BINARY_FILE_EXT):
        return False
    return is_text(open(filename).read(blocksize))

def is_text(stuff):
    if "\0" in stuff:
        return False
    if not stuff:  # Empty files are considered text
        return True
    # Get the non-text characters (maps a character to itself then
    # use the 'remove' option to get rid of the text characters.)
    non_printable_chars = ''.join(c for c in stuff if c not in string.printable)
    return len(non_printable_chars) / len(stuff) < ALLOWED_NON_PRINTABLE_THRESHOLD

class CalledProcessError(RuntimeError):
    pass

def added_files():
    return set(cmd_output(
        'git', 'diff', '--staged', '--name-only', '--diff-filter', 'A',
    ).splitlines())

def cmd_output(*cmd, **kwargs):
    retcode = kwargs.pop('retcode', 0)
    popen_kwargs = {'stdout': subprocess.PIPE, 'stderr': subprocess.PIPE}
    popen_kwargs.update(kwargs)
    proc = subprocess.Popen(cmd, **popen_kwargs)
    stdout, stderr = proc.communicate()
    stdout, stderr = stdout.decode('UTF-8'), stderr.decode('UTF-8')
    if retcode is not None and proc.returncode != retcode:
        raise CalledProcessError(cmd, retcode, proc.returncode, stdout, stderr)
    return stdout
