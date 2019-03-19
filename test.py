import cmap.io.gct as gct
import numpy as np
filename = 'bgedv2_QNORM.gctx'
print(filename)
obj = gct.GCT(filename)
obj.read()
genes = map(lambda x: x.split('.')[0], obj.get_cids())

print(np.shape(genes))

