#include <math.h>
#include <stdlib.h>
#include <stdio.h>
/*
	c= 3*10**14 # ums^-1
	h= 6.62607004*10**-22 #um^2kg s^-1
	Kb = 1.38*10**-11 #um2 kg s-2 K-1
*/


double planckWL(double T, double wl){
	double w = wl / 1.0e4;
	double c1, c2, ans;
	c1 	= 1.191042e8; //Wm-2sr-1um-1
	c2 	= 1.4387752e4;//Kum
	ans = c1/(w*w*w*w*w*(exp(c2/w/T) - 1.0));
	ans /= 1.0e4;
	return ans;
}

double getResolution(double start, double end, double R){
	return start/R;
}

int getNumPoints(double start, double end, double R){
	double resolution = start/R;
        int numPts =  (end - start) / resolution;
	return numPts;
}

int indexOfWL(double start, double end, double R, double wl_query){	
        double resolution = getResolution(start, end, R);
	int idx = (end - wl_query)/resolution;
	return idx;
}
double gaussian(double x, double mean, double std){
	double ans, arg;
	arg = (x - mean)/std;
	ans = exp(-0.5*arg*arg);
	return ans;
}
double gaussianNormFact(double std){
	double ans;
	ans = pow(std * sqrt(2.0*M_PI), -1.0 );
	return ans;
}

double normGaussian(double x, double mean, double std){
	double ans, factor;
	factor  = gaussianNormFact(std);
	ans	= factor * gaussian(x, mean, std);
	return ans;
}

void generateContinuum(double start, double end, double R, double T, double* spec){
	//Check to see if res is NULL
	//IF not
	double w;
	double resolution = getResolution(start, end, R);
	int numPts =  getNumPoints(start, end, R);
	for(int i = 0; i < numPts; i++){
		w 		= start + i*resolution;
		spec[i] = planckWL(T, w);
	}
}

/* Define R as start/dWL */
void generateWLs(double start, double end, double R, double* res){
	//Check to see if res is NULL
	//IF not
	double resolution = getResolution(start, end, R);
	int numPts =  getNumPoints(start, end, R);
	for(int i = 0; i < numPts; i++){
		res[i] = start + i*resolution;
	}
}

void generateFeature(double start, double end, double R, double mean, double std, double height, double* res){	
	double resolution = start/R;
	int numPts =  (end - start) / resolution;
	double wl = start;
	for(int i = 0; i < numPts; i++){
		res[i] += height * normGaussian(wl + i*resolution, mean, std);
	}	
}

void writeSpecToFile(double start, double end, double R, char* fileName, double* wls, double* spec){
	FILE* fPtr;
	char str[30];
	/* 
	* Open file in w (write) mode. 
	* "data/file1.txt" is complete path to create file
	*/

	fPtr = fopen(fileName, "w");
	/* fopen() return NULL if last operation was unsuccessful */
	if(fPtr == NULL)
	{
		/* File not created hence exit */
		printf("Unable to create file.\n");
		exit(EXIT_FAILURE);
	}

        double resolution = start/R;
        int numPts =  (end - start) / resolution;

	for(int i = 0; i < numPts; i++){
		sprintf(str, "%0.6f \t %0.6f\n", wls[i], spec[i]);
		/* Write data to file */
		fputs(str, fPtr);
	}


	/* Close file to save file data */
	fclose(fPtr);

	}

void normalize(double start, double end, double R, double T, double* spec){
    double w;
    double resolution = getResolution(start, end, R);
    int numPts =  getNumPoints(start, end, R);
    for(int i = 0; i < numPts; i++){
        w       = start + i*resolution;
        spec[i] /= planckWL(T, w);
    }
}

int main(){
	double* wls;
	double* spc;
	double start, end, R;
	start 	= 8000.0;
	end	= 12000.0;
	R	= 1000.0;

	int numPts = getNumPoints(start, end, R);
	wls = (double*)calloc(numPts, sizeof(double));
	spc = (double*)calloc(numPts, sizeof(double));

	generateWLs(start, end, R, wls);
	generateContinuum(start, end, R, 5800, spc);

	generateFeature(start, end, R, 9008., 10.0, -500.0, spc);	

	normalize(start, end, R, 5800, spc);

	writeSpecToFile(start, end, R, "test", wls, spc);

	free(wls);
	free(spc);
	return 0;
}
