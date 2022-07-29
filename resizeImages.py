import cv2
import glob

images = [cv2.imread(file) for file in glob.glob('/home/akanksha/dataset/cherry_leaf/pictures/*.png')]
print('Original image shape is: ', images[0].shape)
# crop to 256X256 top left, top right, bottom left, bottom right, center crop
curridx = 0
for image in images:
    print(f"On image idx: {curridx}")
    #cv2.imshow('Original image', image)
    scale_percent = 60 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height) 
    # resize image
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    
    print('Resized image size is: ', image.shape)
    image_tl = image[0:256, 0:256, :]
    image_tr = image[0:256, 512:768, :]
    image_bl = image[320:576, 0:256, :]
    image_br = image[320:576, 512:768, :]

    center = [image.shape[1]/2, image.shape[0]/2]
    w = 256
    h = 256
    x = center[1] - w/2
    y = center[0] - h/2
    image_cc = image[int(y):int(y+h), int(x):int(x+w)]
    
    print('Images have been cropped to ')
    print(image_tl.shape)
    print(image_tr.shape)
    print(image_bl.shape)
    print(image_br.shape)
    print(image_cc.shape)
    filenametl = f'/home/akanksha/pytorch-CycleGAN-and-pix2pix/datasets/leaves/cherry_leaf/{curridx}_tl.png'
    filenametr = f'/home/akanksha/pytorch-CycleGAN-and-pix2pix/datasets/leaves/cherry_leaf/{curridx}_tr.png' 
    filenamebl = f'/home/akanksha/pytorch-CycleGAN-and-pix2pix/datasets/leaves/cherry_leaf/{curridx}_bl.png'
    filenamebr = f'/home/akanksha/pytorch-CycleGAN-and-pix2pix/datasets/leaves/cherry_leaf/{curridx}_br.png'
    filenamecc = f'/home/akanksha/pytorch-CycleGAN-and-pix2pix/datasets/leaves/cherry_leaf/{curridx}_cc.png'
    
    cv2.imwrite(filenametl, image_tl)
    cv2.imwrite(filenametr, image_tr)
    cv2.imwrite(filenamebl, image_bl)
    cv2.imwrite(filenamebr, image_br)
    cv2.imwrite(filenamecc, image_cc)
    

    #cv2.imshow('top left', image_tl)
    #cv2.imshow('top right', image_tr)
    #cv2.imshow('bottom left', image_bl)
    #cv2.imshow('bottom right', image_br)
    #cv2.imshow('center crop', image_cc)
    #cv2.waitKey(0)

    curridx = curridx + 1
    #cv2.destroyAllWindows()
