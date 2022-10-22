import cv2 

imagen = cv2.imread("marte.jpg")
imagen1 = cv2.imread("mercurio.jpg")
imagen2 = cv2.imread("neptuno.jpg")
imagen3 = cv2.imread("saturno.png")
imagen4 = cv2.imread("sol.jpg")
imagen5 = cv2.imread("tierra.jpg")
imagen6 = cv2.imread("urano.jpg")
imagen7 = cv2.imread("venus.jpg")

cv2.imshow("LOL",imagen)
cv2.imshow("LOL2",imagen1)
cv2.imshow("LOL3",imagen2)
cv2.imshow("LOL4",imagen3)
cv2.imshow("LOL5",imagen4)
cv2.imshow("LOL6",imagen5)
cv2.imshow("LOL7",imagen6)
cv2.imshow("LOL8",imagen7)

cv2.putText(imagen, "Marte", (110,180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255) )
cv2.imshow("LOL",imagen)

cv2.putText(imagen1, "Mercurio", (110,180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255) )
cv2.imshow("LOL2",imagen1)

cv2.putText(imagen2, "Neptuno", (110,180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255) )
cv2.imshow("LOL3",imagen2)

cv2.putText(imagen3, "Saturno", (110,180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255) )
cv2.imshow("LOL4",imagen3)

cv2.putText(imagen4, "Sol", (110,180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255) )
cv2.imshow("LOL5",imagen4)

cv2.putText(imagen5, "Tierra", (110,180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255) )
cv2.imshow("LOL6",imagen5)

cv2.putText(imagen6, "Urano", (110,180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255) )
cv2.imshow("LOL7",imagen6)

cv2.putText(imagen7, "Venus", (110,180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255) )
cv2.imshow("LOL8",imagen7)

cv2.waitKey(0)