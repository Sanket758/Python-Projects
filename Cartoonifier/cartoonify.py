import cv2


def cartoonify(file):
    img = cv2.imread(file)

    # Get the edges
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 7, 7)

    color = cv2.bilateralFilter(img, 3, 300, 300)

    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon