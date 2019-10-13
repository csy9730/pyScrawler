from ctypes import c_ubyte, cast, POINTER  ,c_void_p,addressof
import numpy as np

buf = (c_ubyte * 400)()
bitmap_size = (80, 20, 3)
bytes_count = bitmap_size[0]*bitmap_size[1]*bitmap_size[2]
pointer_data = c_void_p(addressof(buf))
#定义一个指向数组的指针
array_pointer = cast(pointer_data, POINTER(c_ubyte*bytes_count))
np_arr = np.frombuffer(array_pointer.contents, dtype=np.uint8, count=bytes_count)
np_arr = np_arr.reshape(bitmap_size)
print( np_arr.shape )