import sys
import numpy as np
# print(sys.version_info)
# print(np.version.full_version)
# print(np.show_config())

x = np.arange(0, 50)
y = np.flip(x, axis=0)
y = np.flipud(x)
print(x)
print(y)
