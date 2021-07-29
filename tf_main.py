import tensorflow as tf
import cProfile

tf.executing_eagerly()

#node 생성
node1 = tf.constant(5., tf.float32)
node2 = tf.constant(5.)
node3 = tf.add(node1, node2)

print("node1 : " , node1, " \nnode2 : " ,node2, "\nnnode3 : ", node3)

a = tf.Variable(tf.ones(shape=(2,2)), name="A")
b = tf.Variable(tf.ones(shape=(2)), name="B")

@tf.function
def forward(x):
    return a * x + b

out_a = forward([1,0])
print(out_a)