from session import *
import sys

# Taked session file path as command line argument and passed to following method
sessionFilePath = sys.argv[1]

sessionGenerator(sessionFilePath)
