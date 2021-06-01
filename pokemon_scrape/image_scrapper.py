import cv2
import numpy as np
import urllib.request
import time

start_time = time.time()
for i in range(1, 41):
    try:
        req = urllib.request.Request(
            'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/' + '{:03d}'.format(i) + '.png')
        response = urllib.request.urlopen(req)
        binary_str = response.read()
        byte_array = bytearray(binary_str)
        numpy_array = np.asarray(byte_array, dtype="uint8")
        image = cv2.imdecode(numpy_array, cv2.IMREAD_UNCHANGED)
        cv2.imwrite("images/" + '{:04d}'.format(i) + ".png", image)
        print("Saved " + '{:04d}'.format(i) + ".png")
    except Exception as e:
        print("Error Occured for Pokemon " + '{:04d}'.format(i))
        print(str(e))
        
end_time = time.time()
print("Done")
print("Time Taken = ", end_time - start_time, "sec")
