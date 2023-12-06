## Written by Ye Kyaw Thu, LU Lab., Myanmar
## for color statistic analysis
## last updated: 6 Dec 2023

## Reference: Based on Fig 2 of following paper, 
## Nakauchi S, Tamura H. Regularity of colour statistics in explaining colour composition preferences in art paintings.
## Sci Rep. 2022 Aug 26;12(1):14585. doi: 10.1038/s41598-022-18847-9. PMID: 36028748; PMCID: PMC9418166.


import argparse
import cv2
import numpy as np
from scipy.stats import skew
from skimage import color

def analyze_color_statistics(image_path):
    """
    Analyze the color statistics of the given image and print the results.
    """
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Cannot load image from {image_path}")
        return

    # Convert the image from BGR (OpenCV default) to RGB and then to CIELAB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_lab = color.rgb2lab(image_rgb)

    # Extract the a* and b* channels
    a_channel = image_lab[:, :, 1]
    b_channel = image_lab[:, :, 2]

    # Calculate statistics for a* and b* channels
    a_mean, b_mean = np.mean(a_channel), np.mean(b_channel)
    a_std, b_std = np.std(a_channel), np.std(b_channel)
    a_skew, b_skew = skew(a_channel.flatten()), skew(b_channel.flatten())
    correlation = np.corrcoef(a_channel.flatten(), b_channel.flatten())[0, 1]

    # Print the statistics
    print(f"Color Statistics for {image_path}:")
    print(f"  Mean (a*, b*): ({a_mean:.2f}, {b_mean:.2f})")
    print(f"  Std Dev (a*, b*): ({a_std:.2f}, {b_std:.2f})")
    print(f"  Skewness (a*, b*): ({a_skew:.2f}, {b_skew:.2f})")
    print(f"  Correlation (a*, b*): {correlation:.2f}")

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Analyze color statistics of an image to check its matching to nature.",
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("image_path", help="Path to the image file")
    parser.epilog = """
    Explanation of Statistics:
    - Mean: Average value of a* (green-red) and b* (blue-yellow) components.
    - Std Dev: Measure of the spread of color values around the mean.
    - Skewness: Measure of the asymmetry of the color distribution.
      Positive skew indicates a tail on the right, negative skew on the left.
    - Correlation: Measure of how two variables (a* and b*) are related.
      A positive value indicates that they tend to increase together.
    """
    args = parser.parse_args()

    # Analyze the color statistics of the provided image
    analyze_color_statistics(args.image_path)

if __name__ == "__main__":
    main()
