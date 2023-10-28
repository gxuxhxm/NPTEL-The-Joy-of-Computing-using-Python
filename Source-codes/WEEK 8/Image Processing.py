import cv2

# Read the input image
input_image = cv2.imread("input.jpg")

# Check if the image was read successfully
if input_image is None:
    print("Could not open or read the image")
else:
    # Apply image enhancement technique
    enhanced_image = cv2.detailEnhance(input_image)

    # Save the enhanced image
    cv2.imwrite("enhanced_image.jpg", enhanced_image)
    print("Image enhancement completed and saved as enhanced_image.jpg")