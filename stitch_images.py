import cv2
import os

main_folder = "photos"
myfolder = os.listdir(main_folder)
print(myfolder)

for folder in myfolder:
    path = main_folder+"/"+folder
    images = []
    myimg_list = os.listdir(path)
    print(f'Total images detected {len(myimg_list)}')
    for img in myimg_list:
        curImg = cv2.imread(f'{path}/{img}')
        curImg = cv2.resize(curImg, (0,0),None,0.2,0.2)
        images.append(curImg)

    stitcher = cv2.Stitcher.create()
    (status, result) = stitcher.stitch(images)
    if(status == cv2.STITCHER_OK):
        print('panorama generated successfully')
        cv2.imshow(folder, result)
        cv2.waitKey(1)
    else:
        print('panorama generation failled')

cv2.waitKey(0)



