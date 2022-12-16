import numpy as np
import cv2

def mse(image1, image2):
  # Calculate the mean squared error between the two images
  err = np.sum((image1.astype("float") - image2.astype("float")) ** 2)
  err /= float(image1.shape[0] * image1.shape[1])
  return err

def psnr(image1, image2):
  # Calculate the peak signal-to-noise ratio between the two images
  mse_val = mse(image1, image2)
  if mse_val == 0:
    return float('inf')
  PIXEL_MAX = 255.0
  return 20 * np.log10(PIXEL_MAX / np.sqrt(mse_val))

# Read the two images
image1 = cv2.imread('Syahru.jpg')
image2 = cv2.imread('result9563.png')

# Calculate MSE and PSNR
mse_val = mse(image1, image2)
psnr_val = psnr(image1, image2)

print(f"MSE: {mse_val:.2f}")
print(f"PSNR: {psnr_val:.2f} dB")
