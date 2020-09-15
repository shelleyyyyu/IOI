python evaluate.py --log_root=trained_model/logs_jdqa_v0_1 \
--w2v_data_path ./data/jdqa_data_calibration/ \
--batch_size=20 \
--test_fname ./data/jdqa_data_calibration/v0/A/tfrecords/train.tfrecords \
--result_fname ./trained_model/logs_jdqa_v0_1/train.a.txt

python evaluate.py --log_root=trained_model/logs_jdqa_v0_1 \
--w2v_data_path ./data/jdqa_data_calibration/ \
--batch_size=20 \
--test_fname ./data/jdqa_data_calibration/v0/A/tfrecords/valid.tfrecords \
--result_fname ./trained_model/logs_jdqa_v0_1/valid.a.txt

python evaluate.py --log_root=trained_model/logs_jdqa_v0_1 \
--w2v_data_path ./data/jdqa_data_calibration/ \
--batch_size=20 \
--test_fname ./data/jdqa_data_calibration/v0/B/tfrecords/train.tfrecords \
--result_fname ./trained_model/logs_jdqa_v0_1/train.b.txt

python evaluate.py --log_root=trained_model/logs_jdqa_v0_1 \
--w2v_data_path ./data/jdqa_data_calibration/ \
--batch_size=20 \
--test_fname ./data/jdqa_data_calibration/v0/B/tfrecords/valid.tfrecords \
--result_fname ./trained_model/logs_jdqa_v0_1/valid.b.txt
