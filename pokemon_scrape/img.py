from PIL import Image
import os

for f in os.listdir('/Users/samehphopal/new_spider/pokemon_scrape/images'):
    if f.endswith('.png'):
        i = Image.open(f)
        fn, fext =  os.path.splitext(f)
        i.save('jpg/{}.jpg'.format(fn))
        
