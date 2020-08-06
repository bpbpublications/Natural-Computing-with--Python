import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
print (mnist.train.images.shape)

from matplotlib import pyplot as plt
plt.figure()
img = mnist.train.images[0].reshape((28,28)) 
plt.imshow(img,cmap='gray')
plt.show()

print (mnist.train.labels.shape)
print (mnist.train.labels[0])
print (mnist.train.labels[0].argmax())


x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
scores = tf.matmul(x,W)+b
y = tf.nn.softmax(tf.matmul(x, W) + b)

y_ = tf.placeholder(tf.float32, [None, 10])
loss = tf.reduce_mean(-1*(tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1])))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss) 
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

y_ = tf.placeholder(tf.float32, [None, 10])
loss = tf.reduce_mean(-1*(tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1])))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss) 
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
losses = list()

for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    _,l=sess.run([train_step,loss], feed_dict={x: batch_xs, y_: batch_ys})
    losses.append(l)

plt.figure()
plt.plot(losses)
plt.xlabel('iterations')
plt.ylabel('loss')
plt.show()


predicted_probabilities=sess.run(y,feed_dict={x:mnist.train.images})
print (predicted_probabilities.shape)
print (predicted_probabilities[0])
predicted_labels = predicted_probabilities.argmax(1)
print (predicted_labels[0])
gt_labels = mnist.train.labels.argmax(1)
acc = (predicted_labels==gt_labels).mean()
print (acc)
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
print (sess.run(correct_prediction,feed_dict={x:mnist.train.images,y_:mnist.train.labels}))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print (sess.run(accuracy,feed_dict={x:mnist.train.images,y_:mnist.train.labels}))




