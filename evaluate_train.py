import pickle
import os,sys,random

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import numpy as np
import time
from datetime import datetime
from nvidia_helper import get_available_gpu
from config import get_args
from data_utils_record import get_record_parser, get_batch_dataset
from metrics import recall_2at1, recall_at_k, precision_at_k, MRR, MAP
from model import model
random.seed(1234)
np.random.seed(1234) 

FLAGS = get_args()


if __name__ == "__main__":

    if FLAGS.auto_gpu:
       index_of_gpu = get_available_gpu()
       FLAGS.gpu = 'gpu:' + str(index_of_gpu)
       print('Use GPU {}'.format(index_of_gpu))
    else:
       index_of_gpu = 0
    os.environ["CUDA_VISIBLE_DEVICES"] =str(index_of_gpu)

    # Output directory for models and summaries
    out_dir = os.path.abspath(os.path.join(os.path.curdir, FLAGS.log_root))
    print("Writing to {}\n".format(out_dir))

    # Checkpoint directory. Tensorflow assumes this directory already exists so we need to create it
    checkpoint_dir = os.path.abspath(os.path.join(out_dir, "checkpoints"))
    checkpoint_prefix = os.path.join(checkpoint_dir, "model")
    if not os.path.exists(checkpoint_dir):
        os.makedirs(checkpoint_dir)

    with tf.device("/%s" % FLAGS.gpu):
        session_conf = tf.ConfigProto(
            allow_soft_placement=FLAGS.allow_soft_placement,
            log_device_placement=FLAGS.log_device_placement)
        session_conf.gpu_options.allow_growth = True
        sess = tf.Session(config=session_conf)

        # Load pretrained word embeddings
        print("Loading pretrained word embeddings ...")
        init_embeddings_path = './%s/word_emb_matrix.pkl'%(FLAGS.w2v_data_path)
        with open(init_embeddings_path, 'rb') as f:
            embeddings = np.array(pickle.load(f))
        FLAGS.vocab_size = embeddings.shape[0]

        word2idx_path = './%s/word_dict.pkl'%(FLAGS.w2v_data_path)
        word2idx = pickle.load(open(word2idx_path, 'rb'))
        idx2word = {value: key for key, value in word2idx.items()}
        with sess.as_default():
            test_record_file = './%s/train.tfrecords'%(FLAGS.data_path)
            parser = get_record_parser(FLAGS)
            test_dataset = get_batch_dataset(test_record_file, parser, FLAGS.batch_size, FLAGS.num_threads, FLAGS.capacity, True)
            test_iterator = test_dataset.make_initializable_iterator()
            
            sess.run(test_iterator.initializer)

            test_handle = sess.run(test_iterator.string_handle())
            handle = tf.placeholder(tf.string, shape=[])
            iterator = tf.data.Iterator.from_string_handle(handle, test_dataset.output_types, test_dataset.output_shapes)

            model = model(iterator, FLAGS)


            global_step = tf.Variable(0, name="global_step", trainable=False)
            saver = tf.train.Saver()
            print(checkpoint_dir)
            print(tf.train.latest_checkpoint(checkpoint_dir))
            saver.restore(sess, tf.train.latest_checkpoint(checkpoint_dir))

            def dev_step():
                acc = []
                losses = []
                context_list = []
                response_list = []
                pred_scores = []
                pred_labels = []
                ture_labels = []
                count = 0
                while True:
                    try:
                        feed_dict = {
                            handle: test_handle, 
                            model.is_training:False,
                            model.dropout_keep_prob: 1.0
                        }
                        context, response, step, loss, accuracy, y_pred, target = sess.run(
                            [model.context, model.response, global_step, model.loss, model.accuracy, model.y_pred, model.target], feed_dict)
                        acc.append(accuracy)
                        losses.append(loss)

                        context_list += list(context)
                        response_list += list(response)
                        pred_scores += list(y_pred[:, 1])
                        pred_labels += list([0 if (scores[0] > scores[1]) else 1 for scores in y_pred])
                        ture_labels += list(target)

                        count +=1
                        if count % 1000 == 0:
                            print(count)
                    except tf.errors.OutOfRangeError:
                        break

                MeanAcc = sum(acc) / len(acc)
                MeanLoss = sum(losses) / len(losses)

                with open(os.path.join(out_dir, 'result_train_set.txt'), 'w') as f:
                    for context, response, score1, score2, score3 in zip(context_list, response_list, pred_scores, pred_labels, ture_labels):
                        context_str = ' '.join([idx2word[c]for c in context[0] if c != 0])
                        response_str = ' '.join([idx2word[r] for r in response if r != 0])
                        f.writelines(str(context_str) + '\t' + str(response_str) + '\t' + str(score1) + '\t' + str(score2) + '\t' + str(score3) + '\n')
                print("MeanAcc: %.4f" %MeanAcc)

            dev_step()






