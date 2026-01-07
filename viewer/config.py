import os
import tempfile

import elements


config = elements.Flags(
    port=int(os.environ.get('SCOPE_PORT', 8000)),
    basedir=os.environ.get('SCOPE_BASEDIR', ''),
    filesystem=os.environ.get('SCOPE_FILESYSTEM', 'elements'),
    cachedir=os.path.join(tempfile.gettempdir(), 'scope-cache'),
    cachesize=int(4e9),  # 4 GB
    maxdepth=2,
    workers=32,
    debug=False,
).parse()

assert config.basedir, config.basedir
