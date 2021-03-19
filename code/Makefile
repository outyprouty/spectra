CC=gcc
fileBase=featureProfile
exec=spec
pyHead=/usr/local/Cellar/python@3.9/3.9.2_1/Frameworks/Python.framework/Versions/3.9/include/python3.9


all:
#	${CC} ${file}.c -o ${exec}
	#Ask SWIG to create example_wrap.c file
	swig -python -o ${fileBase}_wrap.c ${fileBase}.i
	#Compile the example.c code into obj file
	${CC} -c -fPIC ${fileBase}.c -o ${fileBase}.o
	#Compile example_wrap.c into example_wrap object file
	${CC} -c -fPIC ${fileBase}_wrap.c -o ${fileBase}_wrap.o -I${pyHead}
	#Combine these obejcts files with the linker
	ld -bundle -flat_namespace -undefined suppress -o _${fileBase}.so *.o

clean:
	rm ${exec}

plotN:
	./${exec} a
	python plotFile.py test

plotU:
	./${exec}
	python plotFile.py test
