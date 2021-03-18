CC=gcc
file=featureProfile
exec=spec

all:
	${CC} ${file}.c -o ${exec}

clean:
	rm ${exec}

plot:
	./${exec} 
	python plotFile.py test
