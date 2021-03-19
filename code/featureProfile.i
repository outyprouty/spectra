%module featureProfile
%{
        extern double planckWL(double T, double wl);
        extern double getResolution(double start, double end, double R);
        extern int getNumPoints(double start, double end, double R);
        extern int indexOfWL(double start, double end, double R, double wl_query);
        extern double gaussian(double x, double mean, double std);
        extern double gaussianNormFact(double std);
        extern double normGaussian(double x, double mean, double std);
        extern void generateContinuum(double start, double end, double R, double T, double* spec);
        extern void generateWLs(double start, double end, double R, double* res);
        extern void generateFeature(double start, double end, double R, double mean, double std, double height, double* res);
        extern void writeSpecToFile(double start, double end, double R, char* fileName, double* wls, double* spec);
        extern void normalize(double start, double end, double R, double T, double* spec);
        extern void createDoubleArr(int numPts, double *arr);
        extern void freeArr(double* arr);
%}
extern double planckWL(double T, double wl);
extern double getResolution(double start, double end, double R);
extern int getNumPoints(double start, double end, double R);
extern int indexOfWL(double start, double end, double R, double wl_query);
extern double gaussian(double x, double mean, double std);
extern double gaussianNormFact(double std);
extern double normGaussian(double x, double mean, double std);
extern void generateContinuum(double start, double end, double R, double T, double* spec);
extern void generateWLs(double start, double end, double R, double* res);
extern void generateFeature(double start, double end, double R, double mean, double std, double height, double* res);
extern void writeSpecToFile(double start, double end, double R, char* fileName, double* wls, double* spec);
extern void normalize(double start, double end, double R, double T, double* spec);
extern void createDoubleArr(int numPts, double *arr);
extern void freeArr(double* arr);
