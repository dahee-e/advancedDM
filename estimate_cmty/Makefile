
CFLAGS = -I/opt/homebrew/Cellar/gsl/2.7.1/include
LDFLAGS = -L/opt/homebrew/Cellar/gsl/2.7.1/lib
CC = gcc
LIBS = -lm -lgsl -lgslcblas
ARCH = -arch arm64

communities:communities.o readgml.o
	$(CC) $(CFLAGS) $(LDFLAGS) -o communities communities.o readgml.o $(LIBS)

communities.o:communities.c network.h readgml.h Makefile
	$(CC) $(CFLAGS) -c communities.c

readgml.o:readgml.c readgml.h network.h
	$(CC) $(CFLAGS) -c readgml.c