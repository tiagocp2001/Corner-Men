# Procura luvas/mãos a mais (do adversário) nos fotogramas: manchas vermelhas grandes separadas do boneco
import sys, os
from PIL import Image
import numpy as np
from scipy import ndimage
def manchas(p):
    a = np.array(Image.open(p).convert('RGBA')).astype(int)
    alpha = a[:, :, 3] > 0
    red = alpha & (a[:, :, 0] > 150) & (a[:, :, 0] > 2 * a[:, :, 1])
    lab, n = ndimage.label(red, structure=np.ones((3, 3)))
    tam = ndimage.sum(red, lab, range(1, n + 1))
    corpo, nc = ndimage.label(alpha, structure=np.ones((3, 3)))
    soltas = nc - 1                                # pedaços separados do boneco (luvas a voar, salpicos)
    return int((np.array(tam) >= 12).sum()), soltas
for pasta in sorted(sys.argv[1:]):
    r = [manchas(os.path.join(pasta, f'{i}.png')) for i in range(8)]
    luvas = max(x for x, _ in r); soltas = max(y for _, y in r)
    print(f'{pasta:28s} luvas máx {luvas}  pedaços soltos máx {soltas}', ' <-- ver' if luvas > 3 or soltas > 0 else '')
