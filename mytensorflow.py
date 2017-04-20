import numpy as np
import tensorflow as tf
#Model parameters
W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)
# Model input and output
x = tf.placeholder(tf.float32)
linear_model = W*x + b
y = tf.placeholder(tf.float32)
# loss
loss = tf.reduce_sum(tf.square(linear_model - y))
# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)
# training data
x_train = [1,2,3,4]
y_train = [0,-1,-2,-3]
#training loop
init = tf.global_variables_initializer()
ses = tf.Session()
ses.run(init)

for i in range(10000):
    ses.run(train, {x:x_train, y:y_train})

#evalution of the training accuracy
curr_W, curr_b, curr_loss = ses.run([W, b, loss], {x:x_train, y:y_train})
print("W: %s b: %s loss: %s")%(curr_W, curr_b, curr_loss)
