import tensorflow as tf
tf.InteractiveSession;
row_dim = tf.constant(5)
col_dim = tf.constant(8)
print("row_dim = ", row_dim)
print("col_dim = ", col_dim, "\n")

zero_tsr = tf.zeros([row_dim, col_dim])
print(tf.Session().run(zero_tsr))

ones_tsr = tf.ones([row_dim, col_dim])
print(tf.Session().run(ones_tsr))

constant_tsr = tf.constant([1,2,3])
print(tf.Session().run(constant_tsr))

nrow = 5
ncol = 8
cnst_42 = tf.constant(42, shape=[nrow,ncol])
print(cnst_42, "\n")

zeros_similar = tf.zeros_like(constant_tsr)
print(tf.Session().run(zeros_similar),"\n")

ones_similar = tf.ones_like(constant_tsr)
print(tf.Session().run(ones_similar),"\n")

linear_tsr = tf.lin_space(start=0.0, stop=1.0, num=5)
print(tf.Session().run(linear_tsr),"\n")

randunif_tsr = tf.random_uniform([row_dim, col_dim], minval=0, maxval=1)
print(randunif_tsr)

integer_seq_tsr = tf.range(start=6, limit=15, delta=3)
#print(eval(integer_seq_tsr,"\n"))

#a = "[[1,2],[3,4],[5,6],[7,8],[9,0]]"
#b = eval(a)
#print b