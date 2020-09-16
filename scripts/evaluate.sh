CUDA_VISIBLE_DEVICES=5 nohup python evaluate.py --log_root=trained_model/logs_jdqa_v0_1 \
--w2v_data_path ./data/jdqa_data_calibration/ \
--batch_size=20 \
--test_fname ./data/jdqa_data_calibration/annotation_data/tfrecords/annotate.a.tfrecords \
--result_fname ./trained_model/logs_jdqa_v0_1/train.a.txt > ./evaluate.train.a.log 2>&1 &

CUDA_VISIBLE_DEVICES=0 nohup python evaluate.py --log_root=trained_model/logs_jdqa_v0_1 \
--w2v_data_path ./data/jdqa_data_calibration/ \
--batch_size=20 \
--test_fname ./data/jdqa_data_calibration/annotation_data/tfrecords/annotate.b.tfrecords \
--result_fname ./trained_model/logs_jdqa_v0_1/train.b.txt > ./evaluate.train.b.log 2>&1 &

#####################################################################################################################

CUDA_VISIBLE_DEVICES=0 nohup python evaluate.py --log_root=trained_model/logs_jdqa_v1_2 \
--w2v_data_path ./data/jdqa_data_calibration/ \
--batch_size=20 \
--test_fname ./data/jdqa_data_calibration/annotation_data/tfrecords/annotate.a.tfrecords \
--result_fname ./trained_model/logs_jdqa_v1_2/train.a.txt > ./evaluate.v12.train.a.log 2>&1 &

CUDA_VISIBLE_DEVICES=0 nohup python evaluate.py --log_root=trained_model/logs_jdqa_v1_2 \
--w2v_data_path ./data/jdqa_data_calibration/ \
--batch_size=20 \
--test_fname ./data/jdqa_data_calibration/annotation_data/tfrecords/annotate.b.tfrecords \
--result_fname ./trained_model/logs_jdqa_v1_2/train.b.txt > ./evaluate.v12.train.b.log 2>&1 &



##############

CUDA_VISIBLE_DEVICES=6 nohup python evaluate.py --log_root=trained_model/logs_jdqa_v1_1 \
--w2v_data_path ./data/jdqa_data_calibration/ \
--batch_size=20 \
--test_fname ./data/jdqa_data_calibration/v0/A/tfrecords/train.tfrecords \
--result_fname ./trained_model/logs_jdqa_v1_1/results/train.a.result.txt > ./evaluate.a.train.log 2>&1 &

CUDA_VISIBLE_DEVICES=7 nohup python evaluate.py --log_root=trained_model/logs_jdqa_v0_1 \
--w2v_data_path ./data/jdqa_data_calibration/ \
--batch_size=20 \
--test_fname ./data/jdqa_data_calibration/v0/B/tfrecords/train.tfrecords \
--result_fname ./trained_model/logs_jdqa_v0_1/results/train.b.result.txt > ./evaluate.b.train.log 2>&1 &

CUDA_VISIBLE_DEVICES=6 nohup python evaluate.py --log_root=trained_model/logs_jdqa_v0_1 \
--w2v_data_path ./data/jdqa_data_calibration/ \
--batch_size=20 \
--test_fname ./data/jdqa_data_calibration/annotation_data/tfrecords/test.a.tfrecords \
--result_fname ./trained_model/logs_jdqa_v0_1/results/test.a.result.txt > ./evaluate.a.test.log 2>&1 &

CUDA_VISIBLE_DEVICES=7 nohup python evaluate.py --log_root=trained_model/logs_jdqa_v0_1 \
--w2v_data_path ./data/jdqa_data_calibration/ \
--batch_size=20 \
--test_fname ./data/jdqa_data_calibration/annotation_data/tfrecords/test.b.tfrecords \
--result_fname ./trained_model/logs_jdqa_v0_1/results/test.b.result.txt > ./evaluate.b.test.log 2>&1 &


##############

CUDA_VISIBLE_DEVICES=1 nohup python evaluate.py --log_root=trained_model/logs_jdqa_v1_2 \
--w2v_data_path ./data/jdqa_data_calibration/ \
--batch_size=20 \
--test_fname ./data/jdqa_data_calibration/v0/A/tfrecords/train.tfrecords \
--result_fname ./trained_model/logs_jdqa_v1_2/results/train.a.result.txt > ./evaluate.a.train.log 2>&1 &

CUDA_VISIBLE_DEVICES=6 nohup python evaluate.py --log_root=trained_model/logs_jdqa_v1_2 \
--w2v_data_path ./data/jdqa_data_calibration/ \
--batch_size=20 \
--test_fname ./data/jdqa_data_calibration/v0/B/tfrecords/train.tfrecords \
--result_fname ./trained_model/logs_jdqa_v1_2/results/train.b.result.txt > ./evaluate.b.train.log 2>&1 &

CUDA_VISIBLE_DEVICES=1 nohup python evaluate.py --log_root=trained_model/logs_jdqa_v1_2 \
--w2v_data_path ./data/jdqa_data_calibration/ \
--batch_size=20 \
--test_fname ./data/jdqa_data_calibration/annotation_data/tfrecords/test.a.tfrecords \
--result_fname ./trained_model/logs_jdqa_v1_2/results/test.a.result.txt > ./evaluate.a.test.log 2>&1 &

CUDA_VISIBLE_DEVICES=6 nohup python evaluate.py --log_root=trained_model/logs_jdqa_v1_2 \
--w2v_data_path ./data/jdqa_data_calibration/ \
--batch_size=20 \
--test_fname ./data/jdqa_data_calibration/annotation_data/tfrecords/test.b.tfrecords \
--result_fname ./trained_model/logs_jdqa_v1_2/results/test.b.result.txt > ./evaluate.b.test.log 2>&1 &