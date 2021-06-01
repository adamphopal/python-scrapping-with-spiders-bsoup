import cv2
import numpy as np
import urllib.request
import time
import threading
import math


def getPokemon(start, end):
    print("Started worker for range :", start, "to", end)
    for i in range(start, end):
        try:
            url = 'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/' + \
                '{:03d}'.format(i) + '.png'
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            binary_str = response.read()
            byte_array = bytearray(binary_str)
            numpy_array = np.asarray(byte_array, dtype="uint8")
            image = cv2.imdecode(numpy_array, cv2.IMREAD_UNCHANGED)
            cv2.imwrite("images2/" + '{:04d}'.format(i) + '.png', image)
            #print("Saved " + '{:04d}'.format(i) + '.png')
        except Exception as e:
            print(str(e))

#change the thread_count and image_count
start_time = time.time()
thread_count = 16
image_count = 801
thread_list = []
#each thread contains 50 images, and there will be 16 threads
for i in range(thread_count):
    start = math.floor(i * image_count / thread_count) + 1 #0, 50, 
    end = math.floor((i + 1) * image_count / thread_count) + 1 #50, 100, 
    thread_list.append(threading.Thread(target=getPokemon, args=(start, end)))

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()
#thread_list, with 16 threads, to maangae all 450 images
#Started worker for range : 1 to 29
#Started worker for range : 29 to 57
#Started worker for range : 57 to 85
#Started worker for range : 85 to 113
#Started worker for range : 113 to 141
#Started worker for range : 141 to 169
#Started worker for range : 169 to 197
#Started worker for range : 197 to 226
#Started worker for range : 226 to 254
#Started worker for range : 254 to 282
#Started worker for range : 282 to 310
#Started worker for range : 310 to 338
#Started worker for range : 338 to 366
#Started worker for range : 366 to 394
#Started worker for range : 394 to 422
#Started worker for range : 422 to 451

end_time = time.time()
print("Done")
print("Time taken : " + str(end_time - start_time) + "sec")


