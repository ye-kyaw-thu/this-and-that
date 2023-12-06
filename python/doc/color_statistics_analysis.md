##  Analysis of colour statistics of art paintings and natural scenes

I referred following paper:  

Nakauchi S, Tamura H. Regularity of colour statistics in explaining colour composition preferences in art paintings.   
Sci Rep. 2022 Aug 26;12(1):14585. doi: 10.1038/s41598-022-18847-9. PMID: 36028748; PMCID: PMC9418166.  

input ဝင်လာတဲ့ ပန်းချီကားကို "matching-to-nature" ဆိုတဲ့ hypothesis အောက်မှာ စစ်ဆေးဖို့အတွက် python code ကို ရေးကြည့်ခဲ့တယ်။ အဲဒီအတွက်က ပုံရဲ့ color statistics ကို ထုတ်ကြည့်ဖို့လိုအပ်တယ်။   

- အရင်ဆုံး RGB ကနေ CIELAB color space ကို ပြောင်းရတယ်
- ပြီးမှ mean, standard deviation, skewness နဲ့ CIELAB color component တွေ ဖြစ်တဲ့ a* နဲ့ b* တို့ရဲ့ correlation ကို တွက်တယ်
  
## --help

```
(base) ye@lst-gpu-3090:~/exp/demo/color_statistics$ python ./color_statistics_analysis.py --help
usage: color_statistics_analysis.py [-h] image_path

Analyze color statistics of an image to check its matching to nature.

positional arguments:
  image_path  Path to the image file

optional arguments:
  -h, --help  show this help message and exit

    Explanation of Statistics:
    - Mean: Average value of a* (green-red) and b* (blue-yellow) components.
    - Std Dev: Measure of the spread of color values around the mean.
    - Skewness: Measure of the asymmetry of the color distribution.
      Positive skew indicates a tail on the right, negative skew on the left.
    - Correlation: Measure of how two variables (a* and b*) are related.
      A positive value indicates that they tend to increase together.
```

## Some running results

Impression Sunrise by Claude Monet:  
![Impression Sunrise](https://www.claude-monet.com/images/paintings/impression-sunrise.jpg)  
```
(base) ye@lst-gpu-3090:~/exp/demo/color_statistics$ time python ./color_statistics_analysis.py ./pic/impression-sunrise_by_ClaudeMonet.jpg 
Color Statistics for ./pic/impression-sunrise_by_ClaudeMonet.jpg:
  Mean (a*, b*): (-4.93, 2.26)
  Std Dev (a*, b*): (3.69, 7.00)
  Skewness (a*, b*): (2.93, 0.50)
  Correlation (a*, b*): 0.53

real	0m1.495s
user	0m0.934s
sys	0m1.940s
```

The Fighting Temeraire by Joseph Mallord William Turner:  
![The Fighting Temeraire](https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/The_Fighting_Temeraire%2C_JMW_Turner%2C_National_Gallery.jpg/1024px-The_Fighting_Temeraire%2C_JMW_Turner%2C_National_Gallery.jpg)  

```
(base) ye@lst-gpu-3090:~/exp/demo/color_statistics$ time python color_statistics_analysis.py ./pic/969px-The_Fighting_Temeraire,_JMW_Turner,_National_Gallery.jpg
Color Statistics for ./pic/969px-The_Fighting_Temeraire,_JMW_Turner,_National_Gallery.jpg:
  Mean (a*, b*): (1.86, 13.31)
  Std Dev (a*, b*): (3.53, 9.06)
  Skewness (a*, b*): (1.65, -0.05)
  Correlation (a*, b*): 0.40

real	0m0.404s
user	0m0.966s
sys	0m1.884s
```

Starry Night by Van Gogh:  

![Starry Night by Van Gogh](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1024px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg)

```
(base) ye@lst-gpu-3090:~/exp/demo/color_statistics$ time python ./color_statistics_analysis.py ./pic/606px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg
Color Statistics for ./pic/606px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg:
  Mean (a*, b*): (0.63, -12.30)
  Std Dev (a*, b*): (8.02, 18.79)
  Skewness (a*, b*): (0.72, 0.60)
  Correlation (a*, b*): -0.77

real	0m0.348s
user	0m0.885s
sys	0m1.909s
```


