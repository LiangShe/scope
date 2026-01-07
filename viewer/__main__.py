import os
import pathlib
import sys

import uvicorn

package = str(pathlib.Path(__file__).parent)
sys.path.insert(0, package)
from config import config


def main():

  print(config)

  # Uvicorn watches cwd for changes for reload.
  os.chdir(package)

  host = '127.0.0.1' if sys.platform == 'win32' else '0.0.0.0'
  uvicorn.run(
      'server:app',
      host=host,
      port=config.port,
      reload=config.debug,
      workers=None if config.debug else config.workers,
  )


if __name__ == '__main__':
  main()
