__author__ = 'elizajasin'

import PreProcessing as PreP

data = PreP.readData("E:/Kuliah/semester 8/NLP/Tubes/sa-tagged")
case_fold = PreP.caseFolding(data)
print(case_fold)