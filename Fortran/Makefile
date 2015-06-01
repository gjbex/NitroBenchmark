F90 = gfortran
FFLAGS = -O2 -g
LDFLAGS =
LIBS =

GAUSS_OBJS = quad_func_interface.o quad_mod.o gauss_mod.o gauss_test.o

all: gauss_test.exe

gauss_test.exe: $(GAUSS_OBJS)
	$(F90) $(FFLAGS) -o $@ $(GAUSS_OBJS) $(LDFLAGS) $(LIBS)

%.o: %.f90
	$(F90) $(FFLAGS) -c -o $@ $<

clean:
	rm -f *.exe *.o *.mod core
