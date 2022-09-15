#!/usr/bin/env python
# coding: utf-8

# In[200]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
import json
import heapq


# In[201]:


pp =input('path of image file')
original_image = cv2.imread(pp)
original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

# Plot original image
plt.figure(figsize=(20,10))
plt.imshow(original_image)

# Extracting the red screen
red_scale_image = original_image[:,:,0]

# Plot original image
plt.figure(figsize=(15,10))
plt.imshow(red_scale_image, cmap='gray', vmin=0, vmax=255)


# In[202]:


def histogram_array_generator(image):
    histogram_array = {}
    for index in range(256):
        histogram_array[index] = 0
    for row in image:
        for element in row:
            histogram_array[element] += 1
    return histogram_array
def plot_histogram(array, channel):
    plt.figure(figsize=(18,8))
    plt.bar(array.keys(), array.values())
    plt.ylabel('Number of occurances')
    plt.xlabel('Pixel values')
    plt.title(channel)
    plt.show()


# In[203]:


def histogram_generator(red_array): 
    plot_histogram(red_array, 'Red channel histogram')

red_channel_histogram_array = histogram_array_generator(red_scale_image)
histogram_generator(red_channel_histogram_array)


# In[204]:


def probability_distribution_generator(array, image_dimension):
    prob_dist_array = {}
    for index in range(256):
        prob_dist_array[index] = array[index]/image_dimension
    return prob_dist_array


# In[205]:


def probability_distribution_histogram_generator(red_array):
    plot_histogram(red_array, 'Red probability distribution histogram')

red_channel_probability_distribution = probability_distribution_generator(red_channel_histogram_array, 1000*1000)
probability_distribution_histogram_generator(red_channel_probability_distribution)    




class HeapNode:
    def __init__(self, pixel, prob):
        self.pixel = pixel
        self.prob = prob
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.prob < other.prob

    def __eq__(self, other):
        if (other == None):
            return -1
        if (not isinstance(other, HeapNode)):
            return -1
        return self.prob == other.prob


# In[207]:


class Huffman_Coding:
    def __init__(self, code_dict):
        self.code_dict = code_dict
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    def make_heap(self, Code_dict):
        for key in Code_dict:      
            node = HeapNode(key, Code_dict[key])
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        while (len(self.heap) > 1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged_node = HeapNode(None, node1.prob + node2.prob)

            merged_node.left = node1
            merged_node.right = node2

            heapq.heappush(self.heap, merged_node)

    def make_codes_helper (self, root, current_code):
        if root is None:
            return 
        if root.pixel != None:
            self.codes[root.pixel] = current_code
            self.reverse_mapping[current_code] = root.pixel
            return 

        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    def make_codes (self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)

    def compress (self):
        self.make_heap(self.code_dict)
        self.merge_nodes()
        self.make_codes()
        return self.codes, self.reverse_mapping


# In[208]:


red_channel_probability_distribution['seperator'] = 0
red_huffman_coding = Huffman_Coding(red_channel_probability_distribution)
red_coded_pixels, red_reverse_coded_pixels = red_huffman_coding.compress()


# In[209]:


with open('red_channel_codes.json', 'w') as fp:
    json.dump(red_coded_pixels,fp)
with open('red_channel_decodes.json', 'w') as fp:
    json.dump(red_reverse_coded_pixels,fp)


# In[210]:


def compressor(original_image, code):
    compress_image_array = []
    for pixel_row_index in range(original_image.shape[0]):
        pixel_row = []
        for pixel_column_index in range(original_image.shape[1]):
            pixel_row.append(str(code[original_image[pixel_row_index][pixel_column_index]]))
        compress_image_array.append(pixel_row)
    return compress_image_array

red_channel_compressed_image = compressor(red_scale_image, red_coded_pixels)


# In[211]:


def byte_stream (red_stream_image, red_seperator):
    byte_stream = ""
    
    for stream_row_index in range(len(red_stream_image)):
        for stream_column_index in range(len(red_stream_image[0])):
            byte_stream += str(red_stream_image[stream_row_index][stream_column_index])
    
    byte_stream += red_seperator
    
    return byte_stream

bit_stream = byte_stream(red_channel_compressed_image, red_coded_pixels['seperator'])

print(len(bit_stream))
print(red_scale_image.shape[0]*red_scale_image.shape[1]*8)
print('Compression ratio:', (len(bit_stream)/(red_scale_image.shape[0]*red_scale_image.shape[1]*8)))

with open('bit_stream.txt', 'w') as fp:
    fp.write(bit_stream)

red_channel_decoder = json.load(open('red_channel_decodes.json', 'r'))

with open('bit_stream.txt', 'r') as fr:
    pixel_stream = fr.read()

def decoder (bit_stream, red_stream_decoder):
    code_stream = bit_stream_decode()
    if code_stream == []:
        while code_search(bit_stream, red_stream_decoder, 5) != 'seperator':
            code = code_search(bit_stream, red_stream_decoder, 5)
            code_stream.append(red_stream_decoder[code])
            bit_stream = bit_stream.replace(code, '', 1)

        code = code_search(bit_stream, red_stream_decoder, 5)
        bit_stream = bit_stream.replace(code, '', 1)
        print('Red over, Green started')

    return code_stream
def code_search (small_bit_stream, search_dict, slicing_index):
    code = small_bit_stream[:slicing_index]
    if search_dict.get(code, None) == None:
        return code_search(small_bit_stream, search_dict, slicing_index + 1)
    else:
        return code

def bit_stream_decode ():
    file_to_be_decoded = cv2.imread(pp)
    file_to_be_decoded = cv2.cvtColor(file_to_be_decoded, cv2.COLOR_BGR2GRAY)
    
    file_x, file_y = file_to_be_decoded.shape
    file_size = file_x*file_y
    
    decoded_stream = []
    for x in range(file_x):
        for y in range(file_y):
            decoded_stream.append(file_to_be_decoded[x][y])
    
    return decoded_stream
pixel_stream = decoder(bit_stream, red_channel_decoder)
with open('image_pixel_stream.txt', 'w') as fr:
    fr.write(str(pixel_stream))

with open('image_pixel_stream.txt', 'r') as fr:
    pixel_stream = fr.read()

pixel_stream = pixel_stream.replace('[', '')
pixel_stream = pixel_stream.replace(']', '')
pixel_stream = pixel_stream.split(', ')
pixel_stream = [int(pixel) for pixel in pixel_stream]
red_channel_pixel_stream = pixel_stream[:int(len(pixel_stream))]
red_channel_image = np.reshape(red_channel_pixel_stream, (1024,1024))

plt.figure(figsize=(20,10))
plt.imshow(red_channel_image,cmap='gray', vmin=0, vmax=255)                

