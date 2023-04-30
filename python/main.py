import sys
import cv2 as cv

args = sys.argv[1:]

print(args)

dosya_adi = "resim.png"

resim = cv.imread(dosya_adi)
yeni_resim = resim
if args[0] != 'undefined'and args[1] != 'undefined':
    yukseklik = int(args[0])
    genislik = int(args[1])
    yeni_resim = cv.resize(resim, (genislik, yukseklik))


if args[6] != 'undefined':
    dondur = int(args[6])
    (h, w) = yeni_resim.shape[:2]
    center = (w / 2, h / 2)
    M = cv.getRotationMatrix2D(center, dondur, 1.0)
    yeni_resim = cv.warpAffine(yeni_resim, M, (w, h))


if args[2] != 'undefined'and args[3] != 'undefined' and args[4] != 'undefined'and args[5] != 'undefined':
    x1 = int(args[2])
    y1 = int(args[3])
    x2 = int(args[4])
    y2 = int(args[5])
    yeni_resim = yeni_resim[y1:y2, x1:x2]



if args[7] != 'undefined':
    cevir = int(args[7])
    if cevir == 90:
        yeni_resim = cv.rotate(yeni_resim, cv.ROTATE_90_CLOCKWISE)
    elif cevir == 180:
        yeni_resim = cv.rotate(yeni_resim, cv.ROTATE_180)



cv.imwrite("yeni_resim.png", yeni_resim)
