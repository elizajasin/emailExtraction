__author__ = 'elizajasin'

from bs4 import BeautifulSoup as BSHTML
import PreProcessing as PreP
import TrainTest as TnT

data = PreP.readData("E:/Kuliah/semester 8/NLP/Tubes/sa-tagged")
# print(data[2])
case_fold = PreP.caseFolding(data)
print(TnT.tagging(case_fold))

#add bs4
abstract = str(case_fold[1]).find('abstract')
abstract += 9
open = False
teks = ""
arrteks = []
for isi in range(abstract, len(case_fold[1]), 1):
    # print case_fold[1][isi]
    if case_fold[1][isi] == '>':
        open = True
        if case_fold[1][isi+1] == '.':
            teks += "\n"
    if case_fold[1][isi] == '<':
        open = False
        if case_fold[1][isi+1] != '/':
            teks+="\n"
    if open:
        if case_fold[1][isi] != '>':
            teks += case_fold[1][isi]
print(teks)
waktue=[]
waktus = []
lokasi =[]
pembicara = []
# bs = BSHTML(case_fold[0])
for imel in range(len(case_fold)):
    bs = BSHTML(case_fold[imel])
    if(bs.stime == None):
        waktus.append("Tidak ditemukan waktu mulai")
    else :
        waktus.append(bs.stime.contents[0])
    if(bs.etime == None):
        waktue.append("Tidak ditemukan waktu selesai")
    else :
        waktue.append(bs.etime.contents[0])
    if (bs.location == None):
        lokasi.append("Tidak ditemukan lokasi")
    else :
        lokasi.append(bs.location.contents[0])
    if (bs.speaker == None):
        pembicara.append("Tidak ditemukan Pembicara")
    else :
        pembicara.append(bs.speaker.contents[0])
for tampil in range(len(case_fold)):
    print("isi dari dokumen %d :"%tampil)
    print("lokasi %s"%lokasi[tampil])
    print("waktu mulai %s" %waktus[tampil])
    print("waktu selesai %s" % waktue[tampil])
    print("pembicara %s \n" %pembicara[tampil])