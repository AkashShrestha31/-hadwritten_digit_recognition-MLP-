import tensorflow as tf
import numpy as np
x=[[3,2,3,4],
[6,5,13,2]]
# result=tf.argmax(x,1)
# with tf.Session() as sess:
#     print(sess.run(result))
value=np.argmax(x,1)
print(value)
