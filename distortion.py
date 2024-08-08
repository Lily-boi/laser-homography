import cv2
import numpy as np

# Global variables
drawing = False  # true if mouse is pressed
ix, iy = -1, -1  # initial x,y positions
draw_img = np.ones((500, 500, 3), np.uint8) * 255  # white canvas
points = [[0.3005272448062897, 0.7422680258750916],
[0.663151741027832,0.7535145282745361],
[0.32396018505096436,0.25023430585861206],
[0.642647922039032,0.27647608518600464]]

# Mouse callback function for drawing
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, draw_img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.line(draw_img, (ix, iy), (x, y), (0, 0, 0), 2)
            ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(draw_img, (ix, iy), (x, y), (0, 0, 0), 2)

# Mouse callback function for defining points
def select_points(event, x, y, flags, param):
    global points

    if event == cv2.EVENT_LBUTTONDOWN and len(points) < 4:
        points.append((x, y))
        cv2.circle(point_img, (x, y), 5, (0, 0, 255), -1)

# Create the drawing window
cv2.namedWindow('Draw Here')
cv2.setMouseCallback('Draw Here', draw_circle)

# Create the point selection window
point_img = np.ones((500, 500, 3), np.uint8) * 255  # white canvas
cv2.namedWindow('Select 4 Points')
cv2.setMouseCallback('Select 4 Points', select_points)

while True:
    cv2.imshow('Draw Here', draw_img)
    cv2.imshow('Select 4 Points', point_img)
    
    # When 4 points are selected, perform the warp
    if len(points) == 4:
        original_points = np.array([[0, 0], [1, 0], [0, 1], [1, 1]], dtype='float32')
        target_points = np.array(points, dtype='float32')
        
        # Compute the homography matrix
        H, _ = cv2.findHomography(original_points, target_points)
        print(H)
        
        # Warp the drawing according to the selected points
        warped_img = cv2.warpPerspective(draw_img, H, (500, 500))
        
        # Display the warped image
        cv2.imshow('Warped Image', warped_img)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
