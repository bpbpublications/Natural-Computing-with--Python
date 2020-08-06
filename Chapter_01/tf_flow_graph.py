import tensorflow as tf

a = tf.constant(1.) 
b = tf.constant(5.)
c = tf.constant(2.)
d = tf.constant(5.)
e = tf.constant(6.)
result = ((a+b+c)*d)/6 

r = sess.run(result)
print r

x = a+b+c
y = x*d
result = y/6

print sess.run(x)
print sess.run(y)
print sess.run(result)
