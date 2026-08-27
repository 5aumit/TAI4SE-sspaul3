
import numpy as np
import tensorflow as tf
from tensorflow.contrib import learn
from tensorflow.contrib.learn.python.learn.preprocessing import text
from tensorflow.contrib.learn.python.learn.preprocessing import CategoricalVocabulary

x_raw = []

input_text = input('사용자 평가를 문장으로 입력하세요: ')
x_raw.append(input_text)


#########
# get vocaburary dic
######
vocab_processor = learn.preprocessing.VocabularyProcessor.restore("model/vocab")
input_data = np.array(list(vocab_processor.transform(x_raw)))
print(input_data)



#########
# let's load meta graph and restore weights
######
sess=tf.Session()    
sess.run(tf.global_variables_initializer())
saver = tf.train.import_meta_graph('model/output.ckpt-1000.meta')
saver.restore(sess,tf.train.latest_checkpoint('./model'))

graph = tf.get_default_graph()

X = graph.get_tensor_by_name("X:0")
W = graph.get_tensor_by_name("weight:0")
b = graph.get_tensor_by_name("bias:0")

logits = tf.matmul(X, W) + b

hypothesis = tf.nn.softmax(logits)
prediction = tf.argmax(hypothesis, 1)


prob = sess.run(hypothesis, feed_dict={X: input_data})
pred = sess.run(prediction, feed_dict={X: input_data})


print('probability', prob)
print("Prediction: {}".format(pred))

