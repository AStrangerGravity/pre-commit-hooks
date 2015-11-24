from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import string
import subprocess
import magic

def is_textfile(filename, blocksize=512):
    f = magic.Magic(mime=True, uncompress=True)
    mime = f.from_file(filename)

    # empty files are text
    if mime == "inode/x-empty":
      return True

    if "text/" in mime:
      return True

    return False

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
