# You should replace these 3 lines with the output in calibration step
DIM= (1280, 720)
K=np.array([[447.12612374694214, 0.0, 599.31456138232670], [0.0, 449.81528004516485, 370.99407702722040], [0.0, 0.0, 1.0]])
D=np.array([[-0.046726001655847074], [0.064039518659715020], [-0.004295204462215256], [0.006814784599891647]])
def undistort(img_path):
    img = cv2.imread(img_path)
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    cv2.imshow("undistorted", undistorted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    for p in sys.argv[1:]:
        undistort(p)