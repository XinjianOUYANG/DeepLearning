#include "opencv2/opencv.hpp"
#include "opencv2/contrib/contrib.hpp"


using namespace cv;

int main(int argc, char **argv)
{
	const int kClassNum = 2; // ������
	const int kWidth = 512, kHeight = 512;
	Vec3b red(0, 0, 255), green(0, 255, 0), blue(255, 0, 0);
	Mat image = Mat::zeros(kHeight, kWidth, CV_8UC3);  
	// ѵ��������ǩ����
	int labels[150];
	for (int i  = 0 ; i < 75; i++)
		labels[i] = 0;
	for (int i = 75; i < 150; i++)
		labels[i] = 1;
	std::vector<int> trainResponse;   
	for (int i = 0; i < 150; i++)
		trainResponse.push_back(labels[i]);
	// ѵ������������������
	double trainDataArray[150][2];
	RNG rng;
	for (int i = 0; i < 75; i++)
	{
		trainDataArray[i][0] = 350 +rng.gaussian(30);
		trainDataArray[i][1] = 350 + rng.gaussian(30);
	}
	for (int i = 75; i < 150; i++)
	{
		trainDataArray[i][0] = 150 + rng.gaussian(30);
		trainDataArray[i][1] = 150 + rng.gaussian(30);
	}
	Mat trainData(150, 2, CV_64FC1, trainDataArray);
	// ����LDAͶӰ��ͶӰ��Ϊһά�ģ���kClassNum - 1
	LDA lda(trainData, trainResponse, kClassNum - 1);
	Mat eigenVector = lda.eigenvectors().clone(); // ��ȡ��������
	vector<Mat> classMean(kClassNum);  
	vector<int> classCount(kClassNum); 
// ����Ĵ�������������ÿ����ľ�ֵ����ͶӰ���ֵ
	for (int i = 0; i < kClassNum; i++)  
	{  
		classMean[i] = Mat::zeros(1, trainData.cols, CV_64FC1);  //��ʼ�����о�ֵΪ0  
		classCount[i] = 0;  //ÿһ���е�������
	}  
	Mat sample;  
	for (int i = 0;i < trainData.rows; i++)  
	{	// �ȼ���ÿ�����������������ۼ�ֵ  
		sample = trainData.row(i);  
		if(labels[i]==0)    
		{     
			add(classMean[0], sample, classMean[0]);  
			classCount[0]++;  
		}  
		else   
		{  
			add(classMean[1], sample, classMean[1]);  
			classCount[1]++;  
		}  
	}  
// Ȼ�����ÿ���������������õ���ֵ����
	for (int i = 0; i < kClassNum; i++)   
		classMean[i].convertTo(classMean[i], CV_64FC1, 
1.0/static_cast<float>(classCount[i]));  
	// ������ͶӰ�������
	vector<Mat> cluster(kClassNum);
	// ����������ͶӰ������ģ���������һά��
	// ���ֵ��ͶӰ������ˣ��õ�ͶӰ��������ģ���������һά�ĵ�
	for (int i = 0; i < kClassNum; i++)  
		cluster[i] = classMean[i]*eigenVector;  
	// ��ͼ�������е����Ԥ��
	for (int i = 0; i < image.rows; i++)
	{
		for (int j = 0; j < image.cols; j++)
		{
			Mat sampleMat = (Mat_<double>(1, 2) << j, i); 
			Mat projection = Mat::zeros(1,1,CV_64FC1);
// �ȼ�������������ͶӰ
			projection = sampleMat*eigenVector; 
			double temp = projection.ptr<double>(0)[0];
			// Ȼ��Ƚ����ĸ����ͶӰ���ĸ��ӽ���ȷ��������
			int response = (fabs(temp - cluster[0].ptr<double>(0)[0]) < fabs(temp - 
cluster[1].ptr<double>(0)[0])) ? 0 : 1; 
			if (response == 0)
				image.at<Vec3b>(i, j) = green;
			else 
				image.at<Vec3b>(i, j) = blue;
		}
	}
// ��ʾ����ѵ������
	for (int i = 0; i < trainData.rows; i++)
	{
		const double* v = trainData.ptr<double>(i);
		Point pt = Point((int)v[0], (int)v[1]);

		if (labels[i] == 0)
			circle(image, pt, 5, Scalar::all(0), -1, 8); 
		else
			circle(image, pt, 5, Scalar::all(255), -1, 8);
	}
	imshow("LDA classifier demo", image);
	waitKey(0);
	return 0;
}