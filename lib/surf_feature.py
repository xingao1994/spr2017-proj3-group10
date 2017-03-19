{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "# kps: 4950, descriptors: (4950, 64)\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import cv2\n",
    "import os\n",
    "os.chdir('/Users/zixuan/Desktop/5243 ADS/proj3/training_data/raw_images/')\n",
    "img = cv2.imread('image_1.jpg')\n",
    "gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)\n",
    "surf = cv2.xfeatures2d.SURF_create()\n",
    "(kps, descs) = surf.detectAndCompute(gray, None)\n",
    "print(\"# kps: {}, descriptors: {}\".format(len(kps), descs.shape))\n",
    "img=cv2.drawKeypoints(gray,kps, img)\n",
    "cv2.imwrite('surf_keypoints.jpg',img)\n",
    "descs_list = descs.tolist()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [conda root]",
   "language": "python",
   "name": "conda-root-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
