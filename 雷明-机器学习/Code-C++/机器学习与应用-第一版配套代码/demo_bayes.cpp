#include "opencv2/opencv.hpp"
#include "opencv2/contrib/contrib.hpp"


using namespace cv;

int main(int argc, char **argv)
{
	const int kWidth = 512; // ������ͼ��Ŀ��
	const int kHeight = 512; // ������ͼ��ĸ߶�
	Vec3b red(0, 0, 255), green(0, 255, 0), blue(255, 0, 0); // ��ʾ��������3����ɫ
	// ������ʾ��������ͼ��
	Mat image = Mat::zeros(kHeight, kWidth, CV_8UC3);  
	// Ϊѵ��������ǩ��ֵ
	int labels[30];
	for (int i  = 0 ; i < 10; i++)
		labels[i] = 1; // ǰ��10������Ϊ��1��
	for (int i = 10; i < 20; i++)
		labels[i] = 2; // �м�10������Ϊ��2��
	for (int i = 20; i < 30; i++)
		labels[i] = 3; // ���10������Ϊ��3��
	Mat trainResponse(30, 1, CV_32SC1, labels);
	// ����ѵ������������������
	float trainDataArray[30][2];
	RNG rng; // �������������
	for (int i = 0; i < 10; i++)
	{
// �������ɵ�1����������������
// x��y��������̬�ֲ������������������������ֵ
// gaussian��������ָ����׼���ֵΪ0����̬�ֲ����������׼��Ϊ30
		trainDataArray[i][0] = 250 + static_cast<float>(rng.gaussian(30));
		trainDataArray[i][1] = 250 + static_cast<float>(rng.gaussian(30));
	}
	for (int i = 10; i < 20; i++)
	{
// ���ɵ�2����������������
		trainDataArray[i][0] = 150 + static_cast<float>(rng.gaussian(30));
		trainDataArray[i][1] = 150 + static_cast<float>(rng.gaussian(30));
	}
	for (int i = 20; i < 30; i++)
	{
// ���ɵ�3����������������
		trainDataArray[i][0] = 320 + static_cast<float>(rng.gaussian(30));
		trainDataArray[i][1] = 150 + static_cast<float>(rng.gaussian(30));
	}
	Mat trainData(30, 2, CV_32FC1, trainDataArray);
	CvNormalBayesClassifier bayesClassifier;
	// ѵ����Ҷ˹������
	bayesClassifier.train(trainData, trainResponse);
	// ��ͼ�������е�(i, j)����������(x, y)����Ԥ�⣬������i��y��j��x
	for (int i = 0; i < image.rows; i++)
	{
		for (int j = 0; j < image.cols; j++)
		{
// ���ɲ���������������
			Mat sampleMat = (Mat_<float>(1, 2) << j, i); 	
// �ñ�Ҷ˹����������Ԥ��
			float response = bayesClassifier.predict(sampleMat); 
// ����Ԥ������ʾ��ͬ����ɫ
			if (response == 1)
				image.at<Vec3b>(i, j) = red;
			else if (response == 2)
				image.at<Vec3b>(i, j) = green;
			else
				image.at<Vec3b>(i, j) = blue;
		}
	}
	// ��ʾѵ������	
	for (int i = 0; i < trainData.rows; i++)
	{
		const float* v = trainData.ptr<float>(i);
		Point pt = Point((int)v[0], (int)v[1]);
		if (labels[i] == 1)
			circle(image, pt, 5, Scalar::all(0), -1, 8); 
		else if (labels[i] == 2)
			circle(image, pt, 5, Scalar::all(128), -1, 8);
		else
			circle(image, pt, 5, Scalar::all(255), -1, 8);
	}
// ��ʾ������ͼ��ˮƽ����Ϊx����ֱ����Ϊy
	imshow("Bayessian classifier demo", image);
	waitKey(0);
	return 0;
}