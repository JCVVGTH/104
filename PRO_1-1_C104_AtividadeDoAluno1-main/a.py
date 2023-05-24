import cv2



img = cv2.imread("solar-system.jpg")






cv2.putText(img,  
           "sol",
           (100, 80),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )

cv2.putText(img,  
           "mercurio",
           (120, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )

cv2.putText(img,  
           "venus",
           (200, 80),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )

cv2.putText(img,  
           "terra",
           (300, 80),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )

cv2.putText(img,  
           "marte",
           (420, 80),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "jupiter",
           (590, 80),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "saturno",
           (750, 80),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "urano",
           (900, 80),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "netuno",
           (1100, 80),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )


cv2.imshow("resultado",img)

cv2.imwrite("solar.jpg",img)



cv2.waitKey(0)


