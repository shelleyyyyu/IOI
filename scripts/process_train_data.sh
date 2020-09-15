#origin data to txt
python ./script/process_train.py \
./data/jdqa_data_calibration/original/traindata.set2.seg \
./data/jdqa_data_calibration/v0/B/txt
#txt to tfrecords
python ./script/data_utils_record_train.py \
./data/jdqa_data_calibration/v0/B/txt \
./data/jdqa_data_calibration \
./data/jdqa_data_calibration/v0/B/tfrecords