#origin data to txt
python ./script/process_test.py \
./data/jdqa_data_calibration/original/traindata.set1.seg \
./data/jdqa_data_calibration/original/traindata.set2.seg \
./data/jdqa_data_calibration/original/testdata.set1.seg \
./data/jdqa_data_calibration/original/testdata.set2.seg \
./data/jdqa_data_calibration/annotation_data/txt
#txt to tfrecords
python ./script/data_utils_record_test.py \
./data/jdqa_data_calibration/annotation_data/txt \
./data/jdqa_data_calibration \
./data/jdqa_data_calibration/annotation_data/tfrecords